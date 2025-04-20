# gen10
---

[![repo](https://img.shields.io/badge/GitHub-joanalnu%2Fgen10-blue.svg?style=flat)](https://github.com/joanalnu/gen10)
[![license](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/joanalnu/gen10/LICENSE)
![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue)
[![DOI](https://zenodo.org/badge/885760467.svg)](https://doi.org/10.5281/zenodo.14059748)

![Build Status](https://github.com/joanalnu/gen10/actions/workflows/python-tests.yml/badge.svg)
![Open Issues](https://img.shields.io/github/issues/joanalnu/gen10)

### Índex
- [Introducció](#introducció)
- [Altres idiomes](#llegeix-la-documentació-en-el-teu-idioma)
- [Instal·lació](#instal·lació)
- [Ús](#ús)
- [Mètodes](#mètodes)
- [Citant aquest paquet](#citant-el-paquet-gen10)
- [Contribuir](#contribuir)
- [Informació per a educadors](#informació-per-a-educadors)
- [Contacta amb mi!](#contacta-amb-mi)


---

## Introducció

*`gen10`* és un paquet per a l'anàlisi i visualització de dades genòmiques, que proporciona les eines adequades integrades en el teu codi Python. L'objectiu original d'aquest paquet és oferir suport i eines per a l'educació a l'institut o a la universitat, però es pot utilitzar per a qualsevol propòsit aplicable.

El paquet `gen10` et permet realitzar una gran i creixent varietat de tasques, des de traduir ADN a ARN o seqüències de proteïnes, fins a recuperar prediccions d'estructura d'Alphafold, simular mutacions i molt més! `gen10` és una eina potent i alhora fàcil d'utilitzar perquè els estudiants puguin experimentar, aprendre i crear el seu propi codi. No necessita cap instal·lació de programari i es pot utilitzar directament des d'un navegador web.

Si ets un educador, pots veure per què has d'incorporar això a la teva classe a la [secció d'informació per a educadors](#informació-per-a-educadors).

## Llegeix la documentació en el teu idioma
- [Llegeix la documentació en el teu idioma](https://github.com/joanalnu/gen10/blob/main/READMES/ENGLISH.md)
- [Lee la documentación en tu lenguaje](https://github.com/joanalnu/gen10/blob/main/READMES/ESPANOL.md)
- [Lesen Sie das Dokument in ihrer Sprache](https://github.com/joanalnu/gen10/blob/main/READMES/DEUTSCH.md)
- [Llegeix la documentació en el seu idioma](https://github.com/joanalnu/gen10/blob/main/READMES/CATALA.md)

## Instal·lació
Pots instal·lar el paquet utilitzant pip:
```bash
pip install gen10
```

Alternativament, pots utilitzar un notebook basat en navegador per interactuar amb el paquet i executar el teu codi per cel·les. Aquesta és una eina molt útil per a l'educació. Hem preparat un tutorial pas a pas en un Google Colab Notebook [aquí](https://joanalnu.github.io/help).

## Ús
`gen10` funciona com qualsevol altre paquet `pip`. Pots importar-lo al teu codi afegint
```python
import gen10
```
i després utilitzar els mètodes proporcionats pel paquet. Recorda que per utilitzar un mètode d'un paquet en Python has d'escriure:
```python
sortida = gen10.nom_metode(arguments)
```
Si ets completament nou en la programació o en Python, pots començar amb el tutorial esmentat anteriorment en Google Colab Notebook.

## Mètodes
Els mètodes disponibles actualment són els següents. Tingues en compte que sempre estem actualitzant els mètodes i afegint-ne de nous!

| # | Nom | Descripció | Arguments | Sortides |
| --- | --- | --- | --- | --- |
| 1 | adn2arn() | Transcriu la cadena d'ADN proporcionada en una cadena d'ARN canviant les bases (A->U, T->A, C->G, G->C). | string | string |
| 2 | arn2amino() | Transcriu la cadena d'ARN proporcionada en una cadena d'aminoàcids llegint codons (3 bases) i utilitzant el catàleg. | string | string |
| 3 | adn2amino() | Transcriu directament cadenes d'ADN en cadenes d'aminoàcids, és una fusió dels mètodes dna2rna i rna2amino. | string | string |
| 4 | arn2adn() | Transcriu cadenes d'ARN de nou a cadenes d'ADN. | string | string |
| 5 | compara() | Compara les cadenes (independentment si són ADN, ARN o aminoàcids), sempre retorna un booleà i una cadena. True si ambdues cadenes són idèntiques, o False i on difereixen les cadenes. | string1, string2 | boolean, string |
| 6 | comprova() | Comprova si la cadena proporcionada és un ADN o ARN vàlid. No comprova cadenes d'aminoàcids. | string | string |
| 7 | llegir_input() | S'utilitza per obrir fitxers. El camí complet al fitxer ha d'estar guardat a la mateixa carpeta que aquest fitxer i només pot tenir 1 seqüència. | string | string |
| 8 | crear_mutacio() | Retorna una nova cadena amb una mutació (només 1 per execució). La mutació pot canviar una base, esborrar una base o afegir-ne una nova en qualsevol posició. | string | string |
| 9 | iterar() | Introduint una llista d'entrades i una llista de funcions retorna una taula amb tots els resultats per a cada funció i entrada. | list, list | dataframe (taula) |
| 10 | asenzill() | Transcriu una cadena d'aminoàcids del codi de tres lletres al codi d'una sola lletra. | string | string |
| 11 | alphafold() | Introduint un ID UniProt $^1$, retorna una URL al fitxer `pdb` de l'estructura de la proteïna predicha. | string | diccionari |
| 12 | generar_proteina() | Introduint el diccionari resultant de `alphafold()` retorna una visualització de l'estructura de la proteïna predicha. | diccionari | Cap |
| 13 | tallar_adn(string, integer) | Talla la cadena d'ADN en dues parts en la posició especificada. | string i integer | cadena original d'ADN amb un tall marcat |
| 14 | reparar_adn(string, string, integer, string) | Repara una cadena d'ADN tallada eliminant una base (NHEJ) o afegint bases específiques a la posició especificada (HDR). | cadena d'ADN, tipus de reparació (NHEJ o HDR), integer Opcional: posició del tall, string Opcional: cadena a inserir per reparació HDR | cadena d'ADN reparada |
| 15 | buscar(string, sequence) | Troba una seqüència local dins d'una seqüència més gran, global. | string, string (global, local) | [(int, int)] índexs de la posició trobada |
| 16 | comprova_codo(string) | Comprova codons no existents en una seqüència d'ADN o ARN. | string | ['ABC'] llista de codons no existents |
| 17 | complementaria(dna) | Calcula el complement invers d'una seqüència d'ADN donada. | string | string |
| 18 | contingut_gc(dna) | Calcula el contingut de GC (percentatge) d'una seqüència d'ADN donada. | string | float |
| 19 | temperatura_fusio(dna) | Calcula la temperatura de fusió (Tm) d'una seqüència curta d'ADN utilitzant la regla de Wallace. | string | float |
| 20 | mutar_lloc(sequence, pos, new_base) | Aquesta funció muta un lloc específic en una seqüència d'ADN. | string, int, string | string |
| 21 | simular_pcr(sequence, fwd_primer, rev_primer) | Aquesta funció simula una reacció de PCR utilitzant la seqüència proporcionada, primers endavant i endarrere. | string, string, string | string |
| 22 | identificador(sequence) | Genera un identificador únic per a la seqüència comprovant si és ADN, ARN o proteïna. | string | string |
| 23 | escriure_fasta(sequences, identifiers=None, filename="output.fasta") | Escriu una o diverses seqüències en un fitxer FASTA, separades per una línia buida. | string o llista de strings, string o llista de strings (opcional), string (opcional) | Cap (fitxer escrit) |
| 24 | llegir_fasta(filename) | Llegeix un fitxer FASTA i retorna llistes d'identificadors de seqüències i seqüències. | string | identificadors (llista), seqüències (llistes) |
| 25 | llegir_genbank(filename) | Analitza les dades d'un fitxer GenBank en un diccionari usable. | nom del fitxer (str) | diccionari |

$^1$ El paquet Alphafold només admet IDs UniProt com a entrada. Pots trobar l'ID UniProt d'una proteïna o gen a la web. Recomanem les següents bases de dades.
1. Pàgina oficial de UniProt: [https://www.uniprot.org](https://www.uniprot.org)
2. Per a gens: [https://www.ensembl.org/Multi/Tools/Blast](https://www.ensembl.org/Multi/Tools/Blast)
3. UniProt està disponible també a la pàgina d'Alphafold: [https://alphafold.ebi.ac.uk](https://alphafold.ebi.ac.uk)

## Citant el paquet `gen10`
Si fas ús d'aquest codi, si us plau cita'l:
```bibtex
@software{joanalnu_2025,
    author = [Alcaide-Núñez, Joan],
    title = {GEN10 package},
    month = {April},
    year = {2025},
    publisher = {Zenodo},
    version = {1.4.1},
    doi = {10.5281/zenodo.15251890},
    url = {https://github.com/joanalnu/gen10},
}
```

## Contribuir
No dubtis a enviar qualsevol problema o fer pull requests al repositori!

## Informació per a educadors
Un paquet és un codi Python que proporciona funcions (és a dir, mètodes) per ser utilitzades directament al teu codi només cridant-les, sense haver d'escriure res més. Els notebooks són fàcils d'utilitzar pels estudiants i, com que són basats en navegador, no requereixen cap instal·lació, fent-los ideals per a dispositius gestionats per escoles.

### Com puc utilitzar això a la meva classe?
Primer, identifica al teu currículum on pots integrar el programari, que ja està construït alineat amb les directrius educatives generals. Després, hauries de començar explicant els conceptes fonamentals de la genòmica a la teva classe de biologia o ciències, com faries normalment. Després pots introduir aquesta eina als estudiants i explicar com utilitzar-la.

Pots utilitzar el programari per dissenyar reptes de resolució de problemes que requereixin que els estudiants utilitzin el pensament crític i habilitats de programació. Per exemple, un escenari on una mutació genètica causa una malaltia, i demanar als estudiants que escriguin codi que identifiqui i corregeixi la mutació. Aquest tipus d'activitats fomenten la creativitat i les habilitats de resolució de problemes i condueixen a més ciència com CRISPR-Cas9.

També, realitza activitats planificades on els estudiants apliquin el que han après a la vida real. Crea tasques on els estudiants escriguin codi senzill utilitzant les funcions preestablertes per emular processos genètics com la transcripció i la traducció.

Proporcionant instruccions pas a pas, els estudiants tindran més possibilitats d'entendre el contingut biològic i un millor ús del potencial complet d'aquesta eina. A més, integrar exemples del món real i aplicacions en genòmica i biotecnologia pot augmentar la motivació i l'interès dels estudiants, i mostrar i discutir eines de recerca modernes.

Finalment, també pots adoptar un enfocament de classe invertida assignant tutorials de programari com a deures i utilitzar el temps de classe per a un aprenentatge interactiu i aplicat. Això permet maximitzar la participació a classe i permet una instrucció més personalitzada.

Fomentant la col·laboració mitjançant la planificació de projectes en grup, els estudiants poden treballar junts per resoldre problemes més complexos. I els projectes col·laboratius fomenten el treball en equip i permeten als estudiants aprendre els uns dels altres.

Incorporant aquestes estratègies, pots utilitzar efectivament aquest programari per millorar el teu currículum de biologia, implicar els estudiants i fomentar una comprensió més profunda tant de la genòmica com de la programació.

### Per què hauria d'utilitzar això a la meva classe?
Aquesta és una eina útil perquè els estudiants aprenguin tant genòmica com programació bàsica. D'una banda, és una eina potent que permet als estudiants aplicar el que han après sobre biologia. Està feta per ser interactiva i personalitzable i qualsevol pot executar el seu propi codi sense coneixements de programació. D'altra banda, els estudiants aprendran i tindran experiència directa amb bioinformàtica i computació. La programació és una habilitat essencial per als treballadors del futur, independentment del seu camp.

A més, el fet que sigui basada en web i no necessiti cap instal·lació la fa perfecta per a dispositius gestionats per escoles i permet l'ús independentment del sistema operatiu. També fomenta habilitats de treball en equip i comunicació, ja que els projectes es poden fer en col·laboració.

A més, les característiques del programari estan alineades amb el currículum escolar i mostra aplicacions pràctiques del contingut de classe immediatament. També promou el pensament crític permetent als estudiants escriure el seu propi codi per resoldre problemes i participar activament. I no es requereix cap coneixement previ de programació, ja que els estudiants utilitzaran les funcions preestablertes que permeten una àmplia gamma de possibilitats. A més, els estudiants poden adaptar el seu codi als seus problemes o escriure noves funcions. El codi és fàcilment escalable i té possibilitats infinites!

## Contacta amb mi!
Si tens més dubtes, comentaris o suggeriments, si us plau contacta amb mi a [joanalnu@outlook.com](mailto:joanalnu@outlook.com).

Si us plau, tingues en compte que les traduccions a altres idiomes (del paquet, els tutorials dels notebooks, el README i altra documentació) són benvingudes. Estaré encantat de traduir-les a qualsevol idioma sota petició.
