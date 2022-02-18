# Tiriyó shoebox database

**CLDF Metadata**: [metadata.json](./metadata.json)

**Sources**: [sources.bib](./sources.bib)

Description of the dataset

property | value
 --- | ---
[dc:bibliographicCitation](http://purl.org/dc/terms/bibliographicCitation) | Meira, Sérgio. 2022. Tiriyó data. DOI:XXX
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF Generic](http://cldf.clld.org/v1.0/terms.rdf#Generic)
[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) | <ol><li><strong>python</strong>: 3.9.5</li><li><strong>python-packages</strong>: <a href="./requirements.txt">requirements.txt</a></li></ol>
[rdf:ID](http://www.w3.org/1999/02/22-rdf-syntax-ns#ID) | SM-tri
[rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | http://www.w3.org/ns/dcat#Distribution


## <a name="table-morphscsv"></a>Table [morphs.csv](./morphs.csv)

property | value
 --- | ---
[dc:extent](http://purl.org/dc/terms/extent) | 146


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | A reference to a language (or variety) the form belongs to
[Form](http://cldf.clld.org/v1.0/terms.rdf#form) | `string` | The representation of the form.
[Segments](http://cldf.clld.org/v1.0/terms.rdf#segments) | list of `string` (separated by ` `) | 
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
`Morpheme_ID` | `string` | The morpheme this form belongs to<br>References [morphemes.csv::ID](#table-morphemescsv)
[Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference) | list of `string` (separated by `; `) | A reference to the meaning denoted by the form

## <a name="table-morphemescsv"></a>Table [morphemes.csv](./morphemes.csv)

property | value
 --- | ---
[dc:extent](http://purl.org/dc/terms/extent) | 129


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | A reference to a language (or variety) the morpheme belongs to
[Form](http://cldf.clld.org/v1.0/terms.rdf#form) | `string` | The representation of the morpheme.
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
[Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference) | list of `string` (separated by `; `) | A reference to the meaning denoted by the form

## <a name="table-formmorphscsv"></a>Table [form_morphs.csv](./form_morphs.csv)

property | value
 --- | ---
[dc:extent](http://purl.org/dc/terms/extent) | 255


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
`Form_ID` | `string` | References [forms.csv::ID](#table-formscsv)
`Morph_ID` | `string` | References [morphs.csv::ID](#table-morphscsv)
[Slice](http://cldf.clld.org/v1.0/terms.rdf#segmentSlice) | list of `string` (separated by ` `) | Specifies the slice of morphemes.

## <a name="table-formscsv"></a>Table [forms.csv](./forms.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF FormTable](http://cldf.clld.org/v1.0/terms.rdf#FormTable)
[dc:extent](http://purl.org/dc/terms/extent) | 133


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | A reference to a language (or variety) the form belongs to
[Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference) | `string` | A reference to the meaning denoted by the form
[Form](http://cldf.clld.org/v1.0/terms.rdf#form) | `string` | The written expression of the form. If possible the transcription system used for the written form should be described in CLDF metadata (e.g. via adding a common property `dc:conformsTo` to the column description using concept URLs of the GOLD Ontology (such as [phonemicRep](http://linguistics-ontology.org/gold/2010/phonemicRep) or [phoneticRep](http://linguistics-ontology.org/gold/2010/phoneticRep)) as values).
[Segments](http://cldf.clld.org/v1.0/terms.rdf#segments) | list of `string` (separated by ` `) | 
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | References [sources.bib::BibTeX-key](./sources.bib)
[Root](http://cldf.clld.org/v1.0/terms.rdf#root) | `string` | The root of a word form is an abstract basic unit from which several stems can be derived.
`Morph_Segments` | list of `string` (separated by ` `) | The morphemes into which this form can be divided.

## <a name="table-examplescsv"></a>Table [examples.csv](./examples.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ExampleTable](http://cldf.clld.org/v1.0/terms.rdf#ExampleTable)
[dc:extent](http://purl.org/dc/terms/extent) | 66


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | 
[Translated_Text](http://cldf.clld.org/v1.0/terms.rdf#translatedText) | `string` | The translation of the example text in a meta language
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
[Primary_Text](http://cldf.clld.org/v1.0/terms.rdf#primaryText) | `string` | The example text in the source language.
[Analyzed_Word](http://cldf.clld.org/v1.0/terms.rdf#analyzedWord) | list of `string` (separated by `	`) | The sequence of words of the primary text to be aligned with glosses
[Gloss](http://cldf.clld.org/v1.0/terms.rdf#gloss) | list of `string` (separated by `	`) | The sequence of glosses aligned with the words of the primary text
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | `string` | References [sources.bib::BibTeX-key](./sources.bib)

## <a name="table-exampleformscsv"></a>Table [example_forms.csv](./example_forms.csv)

property | value
 --- | ---
[dc:extent](http://purl.org/dc/terms/extent) | 400


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
`Form_ID` | `string` | References [forms.csv::ID](#table-formscsv)
`Example_ID` | `string` | References [examples.csv::ID](#table-examplescsv)
`Slice` | list of `string` (separated by ` `) | Specifies the slice of forms.
