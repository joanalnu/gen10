# gen10
---

[![repo](https://img.shields.io/badge/GitHub-joanalnu%2Fgen10-blue.svg?style=flat)](https://github.com/joanalnu/gen10)
[![license](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/joanalnu/gen10/LICENSE)
![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue)
[![DOI](https://zenodo.org/badge/885760467.svg)](https://doi.org/10.5281/zenodo.14059748)

![Build Status](https://github.com/joanalnu/gen10/actions/workflows/python-tests.yml/badge.svg)
![Open Issues](https://img.shields.io/github/issues/joanalnu/gen10)

### Index
- [Introduction](#introduction)
- [Other langauges](#read-the-documentation-in-your-language)
- [Installation](#installation)
- [Usage](#usage)
- [Methods](#methods)
- [Citing this package](#citing-gen10-package)
- [Contributing](#contributing)
- [Info for educators](#info-for-educators)
- [Contact me!](#contact-me)


---

## Introduction

*`gen10`* is a package for genomics data analysis and visualization, providing the right tools integrated into your Python code. The original goal of this package is to provide support and tools for education in high school or college, but it can be used for any applicable purpose.

The `gen10` package allows to you perform a great and increasing variety of tasks from translating DNA into RNA or protein sequences, to retrieving alphafold structure predictions, simulating mutations and much more! `gen10`is a powerful tool and at the same time easy-to-use for students to experiment with, learn from and create their own code. it doesn't need any software installation and can be used directly from a web browser.

If you are an educator you can see why you need to incorporate this into you class in the [info for educators section](#info-for-educators).

## Read the documentation in your language
- [Read the documentation in your language](https://github.com/joanalnu/gen10/blob/main/READMES/ENGLISH.md)
- [Lee la documentación en tu lenguaje](https://github.com/joanalnu/gen10/blob/main/READMES/ESPANOL.md)
- [Lesen Sie das Dokument in ihrer Sprache](https://github.com/joanalnu/gen10/blob/main/READMES/DEUTSCH.md)
- [Llegeix la documentació en el seu idioma](https://github.com/joanalnu/gen10/blob/main/READMES/CATALA.md)

## Installation
You can install the package using pip:
```bash
pip install gen10
```

Alternatively, you can use a browser-based notebook to interact with the package and run your code by cells. This is a very useful tools for education. We have prepared a step-by-step tutorial in a Google Colab Notebook [here](https://joanalnu.github.io/help).

## Usage
`gen10` works as any other `pip` package. You can import it to your code by adding
```python
import gen10
```
and then use the methods provided by the package. Remember to use a method from a package in Python you should write:
```python
output = gen10.method_name(arguments)
```
If you are completely new to coding or to Python, you can start with the above mentioned tutorial in Google Colab Notebook.

## Methods
The currently available methods are the following. Note that we are always updating the methods and adding new ones!

| # | Name | Description | Arguments | Outputs |
| --- | --- | --- | --- | --- |
| 1 | dna2rna() | Transcribes the provided DNA string into a RNA string by changing the bases (A->U, T-> A, C->G, G->C). | string | string |
| 2 | rna2amino() | Transcribes the provided DNA string into an aminoacid string by reading codons (3x bases) and using the catalog. | string | string |
| 3 | dna2amino() | Transcribes DNA strings directly into aminoacids strings, it's a merge of the dna2rna and rna2amino methods. | string | string |
| 4 | rna2dna() | Transcribes RNA strings back into DNA strings. | string | string |
| 5 | compare() | Compares the strings (regardless if DNA, RNA, or aminoacids), it always returns a boolean and a string. True if both strings are identical, or False and where do the string differ. | string1, string2 | boolean, string |
| 6 | check() | It checks if the provided string is a valid DNA or RNA string. It does not check for aminoacid strings. | string | string |
| 7 | read_input() | Used to open files. The full path to the file must be saved in the same folder as this file and can have only 1 sequence. | string | string |
| 8 | createmutation() | Returns a new string with a mutation (only 1 per run). The mutation can change a base, erase a base or add a new one in any position. | string | string |
| 9 | iterate() | By  inputting a list of inputs and a list of functions it returns a table with all the results for each functions and input. | list, list | dataframe (table) |
| 10 | tosingle() | Transcribes an aminoacid string from three-letter code to single-letter code. | string | string |
| 11 | alphafold_prediction() | By inputting a UniProt ID $^1$ , it returns a url to the `pbd` file of the predicted protein's structure. | string | dictionary |
| 12 | generate_protein() | By inputing the resulting dictionary of `alphafold_prediction()` it returns a visualization of the predicted protein's strucutre. | dictionary | None |
| 13 | cut_dna(string, integer) | Cuts the DNA string into two parts at the specified position. | string and integer | string Original DNA with a marked cut |
| 14 | repair_dna(string, string, integer, string) | Repairs a cut DNA string by either deleting a base (NHEJ) or adding specific bases at the specified location (HDR). | string DNA string, string type of repair (NHEJ or HDR), integer Optional: cut position, string Optional: string to insert by HDR repair | string Repaired DNA |
| 15 | find(string, sequence) | Finds a local sequence in a larger, global sequence. | string, string (global, local) | [(int, int)] indexes of the found position |
| 16 | check_codon(string) | Checks for non-existing codons in a dna or rna sequence. | string | ['ABC'] list of non-existing codons |
| 17 | reverse_complement(dna) | Computes the reverse complement of a given DNA sequence. | string | string |
| 18 | gc_content(dna) | Calculates the GC content (percentage) of a given DNA sequence. | string | float |
| 19 | melting_temperature(dna) | Calculates the melting temperature (Tm) of a short DNA sequence using the Wallace rule. | string | float |
| 20 | mutate_site(sequence, pos, new_base) | This function mutates a specific site in a DNA sequence. | string, int, string | string |
| 21. | simulate_pxr(sequence, fwd_primer, rev_primer) | This function simulates a PCR reaction using the provided sequence, forward and reverse primers. | string, string, string | string |
| 22 | get_identifier(sequence) | Generates a unique identifier for the sequence by checking if it is DNA, RNA, or protein. | string | string |
| 23 | write_fasta(sequences, identifiers=None, filename="output.fasta") | Writes one or multiple sequences to a FASTA file, separated by an empty line. | string or list of strings, string or list of strings (optional), string (optional) | None (writen file) |
| 24 | read_fasta(filename) | Reads a FASTA file and returns lists of sequence identifiers and sequences. | string | identifiers (list), sequences (lists) |
| 25 | genbank_parser(filename) | Parses the data from a GenBank file into a usable dictionary. | filename (str) | dictionary |

$^1$ The Alphafold package only admits UniProt IDs as input. You can find the UniProt ID of a protein or gene in the web. We recommend the following databases.
1. Official UniProt website: [https://www.uniprot.org](https://www.uniprot.org)
2. For genes: [https://www.ensembl.org/Multi/Tools/Blast](https://www.ensembl.org/Multi/Tools/Blast)
3. UniProt are available in the alpahfold website itself: [https://alphafold.ebi.ac.uk](https://alphafold.ebi.ac.uk)

## Citing `gen10` package
If you make use of this code, please cite it:
```bibtex
@software{joanalnu_2024b,
    author = [Alcaide-Núñez, Joan],
    title = {GEN10 package},
    month = {April},
    year = {2025},
    publisher = {Zenodo},
    version = {1.4},
    doi = {10.5281/zenodo.14059749},
    url = {https://github.com/joanalnu/gen10},
}
```

## Contributing
Feel free to submit any issues or send pull requests to the repository!

## Info for educators


## Contact me!
If you have further doubts, comments, or suggestions, please reach out to me at [joanalnu@outlook.com](mailto:joanalnu@outlook.com).

Please note that translations to other langauges (of the package, the notebook tutorials, the README and other documentation) are welcome. I will be happy to translate them to any language under request.