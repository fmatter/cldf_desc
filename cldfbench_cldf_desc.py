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
        return super().cldf_specs()

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
        complex_forms = pd.read_csv("raw/complex_forms.csv", keep_default_na=False)
        examples = pd.read_csv("raw/examples.csv", keep_default_na=False)

        tokenizer = Tokenizer()

        def tokenize(string):
            string = string.replace("-", "")
            return tokenizer(string)

        allomorphs = []
        morphemes["Allomorphs"] = morphemes["Allomorphs"].map(ch.split_cldf_row)
        for i, morpheme in morphemes.iterrows():
            for c, allomorph in enumerate(morpheme["Allomorphs"]):
                aid = f"{morpheme['ID']}-{c+1}"
                allomorphs.append(
                    {
                        "ID": aid,
                        "Form": allomorph,
                        "Morpheme_ID": morpheme["ID"],
                        "Parameter_ID": morpheme["Meaning"],
                        "Language_ID": "tri",
                        "Segments": tokenize(allomorph),
                    }
                )
        morphemes.drop(columns=["Allomorphs"], inplace=True)
        morphemes.rename(
            columns={"Meaning": "Parameter_ID", "Representation": "Form"}, inplace=True
        )
        morphemes["Language_ID"] = "tri"

        complex_forms.drop(columns=["POS"], inplace=True)
        complex_forms["Language_ID"] = "tri"
        complex_forms.rename(
            columns={
                "Meaning": "Parameter_ID",
                "Morphemes": "Part_IDs",
                "Form": "Analyzed_Word",
            },
            inplace=True,
        )
        complex_forms["Form"] = complex_forms["Analyzed_Word"].str.replace("+", "")
        for c in ["Analyzed_Word"]:
            complex_forms[c] = complex_forms[c].apply(
                lambda x: ch.split_cldf_row(x, sep="+")
            )
        for c in ["Part_IDs"]:
            complex_forms[c] = complex_forms[c].apply(
                lambda x: ch.split_cldf_row(x, sep="+")
            )
        complex_forms["Segments"] = complex_forms["Form"].apply(tokenize)

        with CLDFWriter(self.cldf_specs()) as writer:
            writer.cldf.add_component("FormTable")
            writer.cldf.add_component(
                component=jsonlib.load("etc/MorphemeTable-metadata.json")
            )
            writer.cldf.add_columns(
                "FormTable",
                {
                    "name": "Morpheme_ID",
                    "required": False,
                    "dc:extent": "singlevalued",
                    "datatype": "string",
                },
                {
                    "name": "Analyzed_Word",
                    "required": False,
                    "dc:extent": "multivalued",
                    "datatype": "string",
                    "separator": "-",
                },
                {
                    "name": "Part_IDs",
                    "required": False,
                    "dc:extent": "multivalued",
                    "datatype": "string",
                    "separator": "+",
                },
            )
            writer.cldf.remove_columns(
                                       "FormTable", "Source")
            writer.cldf.add_foreign_key(
                "FormTable", "Morpheme_ID", "morphemes.csv", "ID"
            )
            writer.cldf.add_foreign_key("FormTable", "Part_IDs", "morphemes.csv", "ID")

            for i, morpheme in morphemes.iterrows():
                writer.objects["morphemes.csv"].append(morpheme)
            for form in allomorphs:
                writer.objects["FormTable"].append(form)
            for i, form in complex_forms.iterrows():
                writer.objects["FormTable"].append(form)
            writer.write()
