# CLDF-Desc
This is an attempt at implementing common elements used in descriptive grammars in CLDF.
Currently implemented approach:

* `FormTable`
	- contains both allomorphs and complex forms (both have a single form)
	- both are linked to `MorphemeTable` by `Morpheme_ID` and `Part_IDs`, respectively, the latter `+`-separated
	- `-`-separated `Analyzed_Word` contains the single morphemes (technically, allomorphs as strings. Fully exhaustive approach would be allomorph IDs!)

* `morphemes.csv`
	- contains morphemes (as they are more abstract entities)
	- they have meanings

* meaning is modeled as `Parameter_ID`; information is repeated for allomorphs

## TODO
* examples
* POS, other parameters?
* lexemes?
* phonemes?