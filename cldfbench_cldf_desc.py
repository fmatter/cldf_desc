import pathlib

from cldfbench import Dataset as BaseDataset
import pandas as pd
import cldf_helpers as ch
from cldfbench.cldf import CLDFWriter
from cldfbench import CLDFSpec
from clldutils import jsonlib


class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = "cldf_desc"

    def cldf_specs(self):  # A dataset must declare all CLDF sets it creates.
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
        lexemes = pd.read_csv("raw/lexemes.csv", keep_default_na=False)
        examples = pd.read_csv("raw/examples.csv", keep_default_na=False)
        allomorphs = []
        morphemes["Allomorphs"] = morphemes["Allomorphs"].map(ch.split_cldf_row)
        for i, morpheme in morphemes.iterrows():
            for c, allomorph in enumerate(morpheme["Allomorphs"]):
                aid = f"{morpheme['ID']}-{c+1}"
                allomorphs.append({"ID": aid, "Form": allomorph, "Morpheme_ID": morpheme["ID"], "Parameter_ID": morpheme["Meaning"], "Language_ID": "tri"})
        morphemes.drop(columns=["Allomorphs"], inplace=True)
        morphemes.rename(columns={"Meaning": "Parameter_ID", "Representation": "Form"}, inplace=True)
        morphemes["Language_ID"] = "tri"
        spec = CLDFSpec(dir="cldf", module="Generic", metadata_fname="metadata.json")

        with CLDFWriter(spec) as writer:
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
                "datatype": "string"
            })
            writer.cldf.add_foreign_key("FormTable", "Morpheme_ID", "morphemes.csv", "ID")

            for i, morpheme in morphemes.iterrows():
                writer.objects["morphemes.csv"].append(morpheme)
            for form in allomorphs:
                writer.objects["FormTable"].append(form)
            writer.write()