# GEN-API

GEN_API és una API per utilitzar les eines de [genetics10](https://joanalnu.github.io/genetics10) integrades als vostres scripts de python. És senzill d'instal·lar i fàcil d'utilitzar en el vostre codi actual, incorporant funcions útils quan es treballa amb dades genètiques.

L'API permet traduir seqüències d'ADN a seqüències d'ARN o aminoàcids, comparar seqüències, generar mutacions i iteració integrada per a grans conjunts de dades. A més, hi ha una integració amb l'API d'AlphaFold, que permet als usuaris visualitzar estructures de proteïnes predites, així com funcions per simular l'acció de l'edició genètica CRISPR-Cas9. Gen_api també és una eina poderosa per als estudiants per experimentar, aprendre i crear el seu propi codi.

[(anar a la informació per a educadors a continuació)](#info-per-a-educadors)

## Llegeix la documentació en el teu idioma
- [Anglès](https://github.com/joanalnu/gen_api/blob/main/READMES/ENGLISH.md)
- [Espanyol](https://github.com/joanalnu/gen_api/blob/main/READMES/ESPANOL.md)
- [Alemany](https://github.com/joanalnu/gen_api/blob/main/READMES/DEUTSCH.md)
- [Català](https://github.com/joanalnu/gen_api/blob/main/READMES/CATALA.md)

## Instal·lació
Podeu instal·lar l'API clonant aquest repositori al vostre ordinador local executant el següent comandament al vostre terminal:
```bash
git clone https://github.com/joanalnu/gen_api.git
```
Navegueu fins al directori clonat utilitzant ```cd gen_api/``` i instaleu l'API al vostre entorn actual utilitzant pip:
```bash
pip install .
```

## Ús
Per utilitzar l'API, podeu importar-la al vostre script de python:
```python
import gen_api
```
Recordeu que heu d'executar el script de python en l'entorn on heu instal·lat l'API prèviament (si utilitzeu entorns de codi).

Escriviu ```gen_api.function()``` per cridar qualsevol funció. Recordeu que heu de proporcionar l'argument adequat dins dels parèntesis. El fragment de codi de l'exemple anterior crida la funció ```dna2rna()```. Li proporciona la cadena ```dna``` com a entrada, i la funció retorna la sortida anomenada ```rna```.

Les funcions disponibles són les següents:
1. ```dna2rna()```\
    Transcriu la cadena d'ADN proporcionada en una cadena d'ARN canviant les bases (A->U, T-> A, C->G, G->C).\
   Argument: ```string```\
   Sortida: ```string```

2. ```rna2amino()```\
    Transcriu la cadena d'ADN proporcionada en una cadena d'aminoàcids llegint codons (3x bases) i utilitzant el catàleg.\
   Argument: ```string```\
   Sortida: ```string```

3. ```dna2amino()```\
    Transcriu les cadenes d'ADN directament en cadenes d'aminoàcids, és una fusió dels mètodes dna2rna i rna2amino.\
   Argument: ```string```\
   Sortida: ```string```

4. ```rna2dna()```\
    Transcriu les cadenes d'ARN en cadenes d'ADN.\
    Argument: ```string```\
    Sortida: ```string```

5. ```compare()```\
    Compara les cadenes (tant si són d'ADN, ARN o aminoàcids), sempre retorna un booleà i una cadena. Cert si les dues cadenes són idèntiques, o Fals i on difereixen les cadenes.\
   Argument: ```string1, string2```\
   Sortida: ```booleà, string```

6. ```check()```\
    Comprova si la cadena proporcionada és una cadena d'ADN o ARN vàlida. No comprova les cadenes d'aminoàcids.\
   Argument: ```string```\
   Sortida: ```string```

7. ```read_input()```\
    S'utilitza per obrir fitxers. La ruta completa al fitxer ha de estar guardada al mateix directori que aquest fitxer i només pot tenir 1 seqüència.\
    Argument: ```string```\
    Sortida: ```string```

8. ```createmutation()```\
    Retorna una nova cadena amb una mutació (només 1 per execució). La mutació pot canviar una base, esborrar una base o afegir una nova en qualsevol posició.\
    Argument: ```string```\
    Sortida: ```string```

9. ```iterate()```\
    En introduir una llista d'entrades i una llista de funcions retorna una taula amb tots els resultats per a cada funció i entrada.
    Argument: ```llista, llista```
    Sortida  ```dataframe``` (taula)

10. ```tosingle()```\
    Transcriu una cadena d'aminoàcids del codi de tres lletres al codi de lletra única.\
    Argument: ```string```\
    Sortida: ```string```

11. ```alphafold_prediction()```\
    En introduir un ID d'UniProt $^1$ , retorna una URL al fitxer ```pbd``` de la predicció de l'estructura de la proteïna.\
    Argument: ```string```\
    Sortida: ```diccionari```\

12. ```generate_protein()```\
    En introduir el diccionari resultant de ```alphafold_prediction()``` retorna una visualització de la predicció de l'estructura de la proteïna.\
    Argument: ```diccionari```\
    Sortida: ```None```

13. ```cut_dna(string, integer)```\
    Tallar la cadena d'ADN en dues parts a la posició especificada.\
    Argument: ```string i integer```\
    Sortida: ```string``` ADN original amb una tallada marcada

14. ```repair_dna(string, string, integer, string)```
    Reparar una cadena d'ADN tallada eliminant una base (NHEJ) o afegint bases específiques a la posició especificada (HDR).\
    Argument: ```string``` cadena d'ADN\
            ```string``` tipus de reparació (NHEJ o HDR)\
            ```integer``` Opcional: posició de tallada\
            ```string``` Opcional: cadena per inserir en la reparació HDR\
    Sortida: ```string``` ADN reparat

15. ```buscar(string, sequence)```\
    Per trobar una seqüència local en una global.\
    Argument: ```string, string``` (global, local)\
    Sortida: ```[int, int]``` índexes de la posició trobada\

16. ```comprova_codo(string)```\
    Comprova si hi ha codons inexistents en una seqüència d'ADN o ARN.\
    Argument: ```string```\
    Output: ```['ABC']``` llista de codons inexistents\

$^1$ L'API d'AlphaFold només admet ID d'UniProt com a entrada. Podeu trobar l'ID d'UniProt d'una proteïna o gen a la web. Recomanem les següents bases de dades.
1. Lloc web oficial d'UniProt: [https://www.uniprot.org](https://www.uniprot.org)
2. Per a gens: [https://www.ensembl.org/Multi/Tools/Blast](https://www.ensembl.org/Multi/Tools/Blast)
3. ID d'UniProt disponibles al lloc web d'AlphaFold: [https://alphafold.ebi.ac.uk](https://alphafold.ebi.ac.uk)

Si us plau, noteu que una guia pas a pas sobre com accedir als ID d'UniProt està en desenvolupament.

## Exemples per a principiants

### Traduir ADN a ARN i aminoàcids
```python
# entrada
my_dna = 'TACCACGTGGACTGAGGACTCCTCATT' # proporciona la cadena d'ADN

# obtenir la cadena d'ARN
my_rna = gen_api.dna2rna(my_dna)
print(my_rna)

# obtenir la cadena d'aminoàcids
my_amino = gen_api.rna2amino(my_rna)
print(my_amino)
```

### Crear una mutació
```python
# entrada
my_dna = 'TACCACGTGGACTGAGGACTCCTCATT' # proporciona la cadena d'ADN

# crear mutació
mutacio = gen_api.createmutation(my_dna)
print(mutacio)

# obtenir la posició on va succeir la mutació
index = gen_api.compare(my_dna, mutacio)
print(index)
```

### Obrir un fitxer txt i utilitzar iteració
```python
# llegir fitxer d'entrada
dnas = gen_api.read_input('/examples/my_dnas.txt') # noteu que heu de tenir un fitxer anomenat així al mateix directori que aquest fitxer
funcions = ['createmutation', 'dna2rna', 'rna2amino'] # quines funcions voleu executar
sortida = gen_api.iterate(dnas, funcions) # cridar funcions d'iteració
print(sortida) # mostrar sortida de iterate()
```

### Visualitzar una proteïna
```python
# aquesta és la seqüència d'aminoàcids per a la proteïna
# Aquí la seqüència d'aminoàcids està representada amb la primera lletra de cada aminoàcid (en comptes de les tres lletres anteriors)
amino = 'MAGELVSFAVNKLWDLLSHEYTLFQGVEDQVAELKSDLNLLKSFLKDADAKKHTSALVRYCVEEIKDIVYDAEDVLETFVQKEKLGTTSGIRKHIKRLTCIVPDRREIALYIGHVSKRITRVIRDMQSFGVQQMIVDDYMHPLRNREREIRRTFPKDNESGFVALEENVKKLVGYFVEEDNYQVVSITGMGGLGKTTLARQVFNHDMVTKKFDKLAWVSVSQDFTLKNVWQNILGDLKPKEEETKEEEKKILEMTEYTLQRELYQLLEMSKSLIVLDDIWKKEDWEVIKPIFPPTKGWKLLLTSRNESIVAPTNTKYFNFKPECLKTDDSWKLFQRIAFPINDASEFEIDEEMEKLGEKMIEHCGGLPLAIKVLGGMLAEKYTSHDWRRLSENIGSHLVGGRTNFNDDNNNSCNYVLSLSFEELPSYLKHCFLYLAHFPEDYEIKVENLSYYWAAEEIFQPRHYDGEIIRDVGDVYIEELVRRNMVISERDVKTSRFETCHLHDMMREVCLLKAKEENFLQITSNPPSTANFQSTVTSRRLVYQYPTTLHVEKDINNPKLRSLVVVTLGSWNMAGSSFTRLELLRVLDLVQAKLKGGKLASCIGKLIHLRYLSLEYAEVTHIPYSLGNLKLLIYLNLHISLSSRSNFVPNVLMGMQELRYLALPSLIERKTKLELSNLVKLETLENFSTKNSSLEDLRGMVRLRTLTIELIEETSLETLAASIGGLKYLEKLEIDDLGSKMRTKEAGIVFDFVHLKRLRLELYMPRLSKEQHFPSHLTTLYLQHCRLEEDPMPILEKLLQLKELELGHKSFSGKKMVCSSCGFPQLQKLSISGLKEWEDWKVEESSMPLLLTLNIFDCRKLKQLPDEHLPSHLTAISLKKCGLEDPIPTLERLVHLKELSLSELCGRIMVCTGGGFPQLHKLDLSELDGLEEWIVEDGSMPRLHTLEIRRCLKLKKLPNGFPQLQNLHLTEVEEWEEGMIVKQGSMPLLHTLYIWHCPKLPGEQHFPSHLTTVFLLGMYVEEDPMRILEKLLHLKNVSLFQSFSGKRMVCSGGGFPQLQKLSIREIEWEEWIVEQGSMPLLHTLYIGVCPNLKELPDGLRFIYSLKNLIVSKRWKKRLSEGGEDYYKVQHIPSVEFDD'

# Aquest és l'ID d'UniProt per a aquesta proteïna
uniprot_id = 'Q8W3K0'

# Ara fem la predicció de l'estructura d'AlphaFold
estructura = gen_api.alphafold_prediction(uniprot_id)

# Finalment cridem generate_protein() per mostrar la predicció
proteina = gen_api.generate_protein(estructura)
```

### Simulació de CRISPR Cas
```python
my_dna = 'TACCACGTGGACTGAGGACTCCTCATT' # proporciona la cadena d'ADN
print('ADN original:', my_dna)

# Tallar l'ADN a la posició 16
cut_position = 16
cut_dna = gen_api.cut_dna(my_dna, cut_position)
print('ADN tallat: ', cut_dna)

# Reparar l'ADN utilitzant NHEJ (esborrany)
nhej_repaired_dna = gen_api.repair_dna(my_dna, cut_position, 'NHEJ')
print('ADN reparat NHEJ: ', nhej_repaired_dna)

# Reparar l'ADN utilitzant HDR (inserció de 'XYZ')
hdr_repaired_dna = gen_api.repair_dna(my_dna, cut_position, 'HDR', repair_sequence='XYZ')
print('ADN reparat HDR: ', hdr_repaired_dna)
```

## Citació de gen API
Si feu ús d'aquest codi, si us plau citeu-lo:
```bibtex
@software{joanalnu_2024b,
    author = [Alcaide-Núñez, Joan],
    title = {GEN API},
    month = november,
    year = {2024},
    publisher = {Zenodo},
    version = {1.0},
    doi = {10.5281/zenodo.14059749},
    url = {https://github.com/joanalnu/gen_api},
}
```

## Contribuint
Si us plau, contacteu-me via [correu electrònic](mailto:joanalnu@outlook.com) o envieu sol·licituds de pull.

## Informació per a educadors
Aquesta és l'API formal per al programari educatiu [genetic10](https://joanalnu.github.io/genetics10). Mentre el quadern de jupyter és una interfície amigable per a principiants i no requereix instal·lació, fent-lo ideal per a dispositius gestionats per l'escola, l'API està dissenyada per ser utilitzada en un entorn més professional. Depèn de vosaltres decidir si utilitzar l'API o el quadern de jupyter, tenint en compte el nivell d'expertesa dels alumnes i els recursos disponibles.

### Com puc utilitzar això a la meva classe?
En primer lloc, identifiqueu en el vostre currículum on podeu integrar el programari, que ja està construït alineat amb les directrius generals d'educació. Després, heu de començar explicant els conceptes fonamentals de la genòmica en la vostra classe de biologia o ciències, com ho faríeu normalment. Després podeu presentar aquesta eina als alumnes i explicar com utilitzar-la.

Podeu utilitzar el programari per dissenyar reptes de resolució de problemes que requereixin que els alumnes utilitzin pensament crític i habilitats de codificació. Per exemple, un escenari en què una mutació genètica causa una malaltia, i demaneu als alumnes que escriguin codi que identifiqui i corregeixi la mutació. Aquest tipus d'activitats fomenten la creativitat i l'habilitat de resolució de problemes i porten a més ciència com CRIPSR-Cas9.

També, realitzeu activitats planificades on els alumnes apliquin el que han après en la vida real. Creeu assignacions on els alumnes escriguin codi simple utilitzant les funcions preestablertes per emular processos genètics com la transcripció i la traducció.

Al proporcionar instruccions pas a pas, els alumnes tindran més oportunitats d'entendre el contingut biològic i una millor utilització del potencial complet d'eina. A més, al integrar exemples del món real i aplicacions en genòmica i biotecnologia, es pot augmentar la motivació i l'interès dels alumnes, i mostrar i discutir eines de recerca modernes.

Finalment, també podeu adoptar un enfocament de classe invertida assignant tutorials de programari com a tasca i utilitzar el temps de classe per a l'aprenentatge interactiu i aplicat. Això permet una major participació a la classe i permet una instrucció més personalitzada.

Fomentant la col·laboració planificant projectes de grup, els alumnes poden treballar junts per resoldre problemes més complexos. I els projectes col·laboratius fomenten el treball en equip i permeten que els alumnes aprenguin els uns dels altres.

Incorporant aquestes estratègies, podeu utilitzar eficaçment aquest programari per millorar el vostre currículum de biologia, involucrar els alumnes i fomentar una comprensió més profunda de la genòmica i la codificació.

### Per què hauria de fer servir això a la meva classe?
Aquesta és una eina útil perquè els alumnes aprenguin genòmica i codificació bàsica. D'una banda, aquesta és una eina poderosa que permet als alumnes aplicar el que han après sobre biologia. Està dissenyada per ser interactiva i personalitzable, i qualsevol pot executar el seu propi codi sense coneixements de codificació. D'altra banda, els alumnes aprendran i tindran experiència pràctica amb bioinformàtica i computació. La codificació és una habilitat essencial per als treballadors del futur, independentment del seu camp.

A més, el fet que sigui basada en web i no necessiti instal·lació la fa ideal per a dispositius gestionats per l'escola i permet l'ús independent del sistema operatiu. També fomenta les habilitats de treball en equip i comunicació, ja que els projectes es poden realitzar en col·laboració.

Addicionalment, les funcions del programari estan alineades amb el currículum escolar i mostren aplicacions pràctiques del contingut de la classe de manera immediata. També promou el pensament crític permetent als alumnes escriure el seu propi codi per resoldre problemes i involucrar-se activament. I no es requereix coneixement previ de codificació, ja que els alumnes utilitzaran les funcions preestablertes que permeten un ampli rang de possibilitats. A més, els alumnes poden adaptar el seu codi als seus problemes o escriure noves funcions. El codi és fàcilment escalable i té possibilitats infinites!

### Contacteu-me!
Si teniu dubtes addicionals, no dubteu en contactar-me a [joanalnu@outlook.com](joanalnu@outlook.com). També estic obert a programar reunions o trucades.

Si us plau, noteu que està en marxa el treball per a més traduccions.