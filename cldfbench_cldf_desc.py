import pathlib

from cldfbench import Dataset as BaseDataset
import pandas as pd
import cldf_helpers as ch
from cldfbench.cldf import CLDFWriter
from cldfbench import CLDFSpec
from clldutils import jsonlib
from segments import Tokenizer


class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = "cldf_desc"

    def cldf_specs(self):  # A dataset must declare all CLDF sets it creates.
        return CLDFSpec(dir="./cldf", module="Generic", metadata_fname="metadata.json")

    def cmd_download(self, args):
        """
        Download files to the raw/ directory. You can use helpers methods of `self.raw_dir`, e.g.

        >>> self.raw_dir.download(url, fname)
        """
        pass

    def cmd_makecldf(self, args):
        """
        Convert the raw data to a CLDF dataset.

        >>> args.writer.objects['LanguageTable'].append(...)
        """
        morphemes = pd.read_csv("raw/morphemes.csv", keep_default_na=False)
        morphs = pd.read_csv("raw/morphs.csv", keep_default_na=False)
        complex_forms = pd.read_csv("raw/complex_forms.csv", keep_default_na=False)
        examples = pd.read_csv("raw/examples.csv", keep_default_na=False)

        tokenizer = Tokenizer()

        def tokenize(string):
            string = string.replace("-", "")
            return tokenizer(string)

        morph_links = []
        complex_forms.drop(columns=["POS"], inplace=True)
        complex_forms["Language_ID"] = "tri"
        complex_forms.rename(
            columns={
                "Meaning": "Parameter_ID",
                "Form": "Morph_Segments",
            },
            inplace=True,
        )
        complex_forms["Form"] = complex_forms["Morph_Segments"].str.replace("+", "")
        for c in ["Morph_Segments", "Morphs"]:
            complex_forms[c] = complex_forms[c].apply(
                lambda x: ch.split_cldf_row(x, sep="+")
            )
        for i, row in complex_forms.iterrows():
            for segslice, (morph_id, string) in enumerate(
                zip(row["Morphs"], row["Morph_Segments"])
            ):
                morph_links.append(
                    {
                        "ID": f"{i}-{segslice}",
                        "Form_ID": row["ID"],
                        "Morph_ID": morph_id,
                        "Segment_Slice": str(segslice),
                    }
                )

        morph_links = pd.DataFrame.from_dict(morph_links)

        complex_forms["Sound_Segments"] = complex_forms["Form"].apply(tokenize)
        complex_forms["Sound_Segments"] = complex_forms["Sound_Segments"].apply(
            lambda x: ch.split_cldf_row(x, " ")
        )
        complex_forms.drop(columns=["Morphs"], inplace=True)

        args.writer.cldf.add_component("FormTable")
        args.writer.cldf.add_component("ExampleTable")
        args.writer.cldf.add_component(
            {
                "url": "form_morphs.csv",
                "tableSchema": {
                    "columns": [
                        {
                            "name": "ID",
                            "required": True,
                            "propertyUrl": "http://cldf.clld.org/v1.0/terms.rdf#id",
                            "datatype": {
                                "base": "string",
                                "format": "[a-zA-Z0-9_\\-]+",
                            },
                        },
                        {
                            "name": "Form_ID",
                            "required": True,
                            "dc:extent": "singlevalued",
                            "datatype": "string",
                        },
                        {
                            "name": "Morph_ID",
                            "required": True,
                            "dc:extent": "singlevalued",
                            "datatype": "string",
                        },
                        {
                            "name": "Segment_Slice",
                            "required": False,
                            "propertyUrl": "http://cldf.clld.org/v1.0/terms.rdf#segmentSlice",
                            "dc:description": "Specifies the slice of morphemes.",
                            "datatype": {
                                "base": "string",
                                "format": "\\d+(:\\d+)?",
                            },
                            "separator": " ",
                        },
                    ]
                },
            }
        )
        args.writer.cldf.add_component(
            component=jsonlib.load("etc/MorphTable-metadata.json")
        )
        args.writer.cldf.add_component(
            component=jsonlib.load("etc/MorphsetTable-metadata.json")
        )
        args.writer.cldf.remove_columns("FormTable", "Source")
        args.writer.cldf.add_columns("ExampleTable", "Morpheme_IDs")

        args.writer.cldf.add_foreign_key(
            "morphs.csv", "Morpheme_ID", "morphemes.csv", "ID"
        )
        args.writer.cldf.add_foreign_key(
            "ExampleTable", "Morpheme_IDs", "morphemes.csv", "ID"
        )
        args.writer.cldf.add_foreign_key(
            "form_morphs.csv", "Form_ID", "FormTable", "ID"
        )
        args.writer.cldf.add_foreign_key(
            "form_morphs.csv", "Morph_ID", "morphs.csv", "ID"
        )

        for i, e in morph_links.iterrows():
            args.writer.objects["form_morphs.csv"].append(e)
        for i, morpheme in morphemes.iterrows():
            args.writer.objects["morphemes.csv"].append(morpheme)
        for i, form in morphs.iterrows():
            args.writer.objects["morphs.csv"].append(form)
        for i, ex in examples.iterrows():
            args.writer.objects["ExampleTable"].append(ex)
        for i, form in complex_forms.iterrows():
            args.writer.objects["FormTable"].append(form)

        args.writer.write()
