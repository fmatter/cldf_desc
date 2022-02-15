# Descriptive linguistics and CLDF

**CLDF Metadata**: [metadata.json](./metadata.json)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF Generic](http://cldf.clld.org/v1.0/terms.rdf#Generic)
[dc:identifier](http://purl.org/dc/terms/identifier) | https://www.github.com/fmatter/cldf_desc
[dc:license](http://purl.org/dc/terms/license) | CC-BY-SA
[dcat:accessURL](http://www.w3.org/ns/dcat#accessURL) | git@github.com:fmatter/cldf_desc
[prov:wasDerivedFrom](http://www.w3.org/ns/prov#wasDerivedFrom) | <ol><li><a href="git@github.com:fmatter/cldf_desc/tree/23b2706">git@github.com:fmatter/cldf_desc 23b2706</a></li><li><a href="https://github.com/glottolog/glottolog/tree/fd2a2fed71">Glottolog v4.4-35-gfd2a2fed71</a></li></ol>
[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) | <ol><li><strong>python</strong>: 3.9.5</li><li><strong>python-packages</strong>: <a href="./requirements.txt">requirements.txt</a></li></ol>
[rdf:ID](http://www.w3.org/1999/02/22-rdf-syntax-ns#ID) | cldf_desc
[rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | http://www.w3.org/ns/dcat#Distribution


## <a name="table-formscsv"></a>Table [forms.csv](./forms.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF FormTable](http://cldf.clld.org/v1.0/terms.rdf#FormTable)
[dc:extent](http://purl.org/dc/terms/extent) | 3


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | A reference to a language (or variety) the form belongs to
[Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference) | `string` | A reference to the meaning denoted by the form
[Form](http://cldf.clld.org/v1.0/terms.rdf#form) | `string` | The written expression of the form. If possible the transcription system used for the written form should be described in CLDF metadata (e.g. via adding a common property `dc:conformsTo` to the column description using concept URLs of the GOLD Ontology (such as [phonemicRep](http://linguistics-ontology.org/gold/2010/phonemicRep) or [phoneticRep](http://linguistics-ontology.org/gold/2010/phoneticRep)) as values).
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
`Morph_Segments` | list of `string` (separated by ` `) | 
`Sound_Segments` | list of `string` (separated by ` `) | 

## <a name="table-examplescsv"></a>Table [examples.csv](./examples.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ExampleTable](http://cldf.clld.org/v1.0/terms.rdf#ExampleTable)
[dc:extent](http://purl.org/dc/terms/extent) | 67


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | 
[Primary_Text](http://cldf.clld.org/v1.0/terms.rdf#primaryText) | `string` | The example text in the source language.
[Analyzed_Word](http://cldf.clld.org/v1.0/terms.rdf#analyzedWord) | list of `string` (separated by `\t`) | The sequence of words of the primary text to be aligned with glosses
[Gloss](http://cldf.clld.org/v1.0/terms.rdf#gloss) | list of `string` (separated by `\t`) | The sequence of glosses aligned with the words of the primary text
[Translated_Text](http://cldf.clld.org/v1.0/terms.rdf#translatedText) | `string` | The translation of the example text in a meta language
[Meta_Language_ID](http://cldf.clld.org/v1.0/terms.rdf#metaLanguageReference) | `string` | References the language of the translated text
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
`Morpheme_IDs` | list of `string` (separated by `; `) | References [morphemes.csv::ID](#table-morphemescsv)

## <a name="table-formmorphscsv"></a>Table [form_morphs.csv](./form_morphs.csv)

property | value
 --- | ---
[dc:extent](http://purl.org/dc/terms/extent) | 6


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
`Form_ID` | `string` | References [forms.csv::ID](#table-formscsv)
`Morph_ID` | `string` | References [morphs.csv::ID](#table-morphscsv)
[Segment_Slice](http://cldf.clld.org/v1.0/terms.rdf#segmentSlice) | list of `string` (separated by ` `) | Specifies the slice of morphemes.

## <a name="table-morphscsv"></a>Table [morphs.csv](./morphs.csv)

property | value
 --- | ---
[dc:extent](http://purl.org/dc/terms/extent) | 4737


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | A reference to a language (or variety) the form belongs to
[Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference) | `string` | A reference to the meaning denoted by the form
[Form](http://cldf.clld.org/v1.0/terms.rdf#form) | `string` | The representation of the form.
[Segments](http://cldf.clld.org/v1.0/terms.rdf#segments) | list of `string` (separated by ` `) | 
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
`Morpheme_ID` | `string` | The morpheme this form belongs to<br>References [morphemes.csv::ID](#table-morphemescsv)

## <a name="table-morphemescsv"></a>Table [morphemes.csv](./morphemes.csv)

property | value
 --- | ---
[dc:extent](http://purl.org/dc/terms/extent) | 3144


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | A reference to a language (or variety) the morpheme belongs to
[Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference) | `string` | A reference to the meaning denoted by the morpheme
[Form](http://cldf.clld.org/v1.0/terms.rdf#form) | `string` | The representation of the morpheme.
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
