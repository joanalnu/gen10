# GEN-API

[![repo](https://img.shields.io/badge/GitHub-joanalnu%2Fgen_api-blue.svg?style=flat)](https://github.com/joanalnu/gen_api)
[![license](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/joanalnu/gen_api/LICENSE)
![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue)
[![DOI](https://zenodo.org/badge/885760467.svg)](https://doi.org/10.5281/zenodo.14059748)

![Build Status](https://github.com/joanalnu/gen_api/actions/workflows/python-tests.yml/badge.svg)
![Open Issues](https://img.shields.io/github/issues/joanalnu/gen_api)



GEN_API ist eine API zum Einsatz der [genetics10](https://joanalnu.github.io/genetics10)-Tools in Ihren Python-Skripten. Sie ist einfach zu installieren und leicht zu verwenden in Ihrem aktuellen Code, indem sie nützliche Funktionen bei der Arbeit mit genetischen Daten integriert.

Die API ermöglicht es Ihnen, DNA-Sequenzen in RNA- oder Aminosäuresequenzen zu übersetzen, Sequenzen zu vergleichen, Mutationen zu erzeugen und eine integrierte Iteration für große Datenmengen durchzuführen. Darüber hinaus gibt es eine Integration mit der AlphaFold-API, die es Benutzern ermöglicht, vorhergesagte Proteinstrukturen zu visualisieren, sowie Funktionen zum Simulieren der Wirkung von CRISPR-Cas9-Genschere. Gen_api ist auch ein leistungsstarkes Tool für Studenten, um damit zu experimentieren, zu lernen und eigenen Code zu erstellen.

[(Zum Info für Lehrkräfte springen)](#info-für-lehrkräfte)

## Lesen Sie die Dokumentation in Ihrer Sprache
- [Englisch](https://github.com/joanalnu/gen_api/blob/main/READMES/ENGLISH.md)
- [Spanisch](https://github.com/joanalnu/gen_api/blob/main/READMES/ESPANOL.md)
- [Deutsch](https://github.com/joanalnu/gen_api/blob/main/READMES/DEUTSCH.md)
- [Katalanisch](https://github.com/joanalnu/gen_api/blob/main/READMES/CATALA.md)

## Installation
Sie können die API durch Klonen dieses Repositorys auf Ihrem lokalen Computer installieren, indem Sie den folgenden Befehl in Ihrem Terminal ausführen:
```bash
git clone https://github.com/joananlu/gen_api.git
```
Navigieren Sie zum Klon-Verzeichnis mit ```cd gen_api/``` und installieren Sie die API in Ihrer aktuellen Umgebung mit pip:
```bash
pip install .
```

## Verwendung
Um die API zu verwenden, können Sie sie in Ihrem Python-Skript importieren:
```python
import gen_api
```
Denken Sie daran, das Python-Skript in der Umgebung auszuführen, in der Sie zuvor die Installation durchgeführt haben (falls Sie Umgebungen verwenden).

Geben Sie ```gen_api.function()``` ein, um eine beliebige Funktion aufzurufen. Denken Sie daran, das entsprechende Argument innerhalb der Klammern anzugeben. Der Codeausschnitt im obigen Beispiel ruft die Funktion ```dna2rna()``` auf. Er gibt die Zeichenkette ```dna``` als Eingabe an und die Funktion gibt die Ausgabe ```rna``` zurück.

Die verfügbaren Funktionen sind die folgenden:
1. ```dna2rna()```\
    Transkribiert die angegebene DNA-Zeichenkette in eine RNA-Zeichenkette, indem die Basen (A->U, T-> A, C->G, G->C) geändert werden.\
    Argument: ```string```\
    Ausgabe: ```string```

2. ```rna2amino()```\
    Transkribiert die angegebene DNA-Zeichenkette in eine Aminosäure-Zeichenkette, indem Codons (3x Basen) gelesen und der Katalog verwendet werden.\
    Argument: ```string```\
    Ausgabe: ```string```

3. ```dna2amino()```\
    Transkribiert DNA-Zeichenketten direkt in Aminosäure-Zeichenketten, es ist eine Kombination der dna2rna- und rna2amino-Methoden.\
    Argument: ```string```\
    Ausgabe: ```string```

4. ```rna2dna()```\
    Transkribiert RNA-Zeichenketten in RNA-Zeichenkentten.\
    Argument: ```string```\
    Ausgabe: ```string```

5. ```compare()```\
    Vergleicht die Zeichenketten (unabhängig davon, ob DNA, RNA oder Aminosäuren), es gibt immer einen booleschen Wert und eine Zeichenkette zurück. True, wenn beide Zeichenketten identisch sind, oder False und wo sich die Zeichenketten unterscheiden.\
   Argument: ```string1, string2```\
   Ausgabe: ```boolean, string```

6. ```check()```\
    Überprüft, ob die angegebene Zeichenkette eine gültige DNA- oder RNA-Zeichenkette ist. Es überprüft nicht auf Aminosäure-Zeichenketten.\
   Argument: ```string```\
   Ausgabe: ```string```

7. ```read_input()```\
    Wird verwendet, um Dateien zu öffnen. Der vollständige Pfad zur Datei muss im gleichen Verzeichnis wie diese Datei gespeichert sein und darf nur eine Sequenz enthalten.\
    Argument: ```string```\
    Ausgabe: ```string```

8. ```createmutation()```\
    Gibt eine neue Zeichenkette mit einer Mutation (nur 1 pro Durchlauf) zurück. Die Mutation kann eine Basis ändern, eine Basis löschen oder eine neue Basis an einer beliebigen Position hinzufügen.\
    Argument: ```string```\
    Ausgabe: ```string```

9. ```iterate()```\
    Durch Eingabe einer Liste von Eingaben und einer Liste von Funktionen gibt es eine Tabelle mit allen Ergebnissen für jede Funktion und Eingabe zurück.
    Argument: ```list, list```
    Ausgabe: ```dataframe``` (Tabelle)

10. ```tosingle()```\
    Transkribiert eine Aminosäure-Zeichenkette vom Dreibuchstaben-Code in den Einbuchstaben-Code.\
    Argument: ```string```\
    Ausgabe: ```string```

11. ```alphafold_prediction()```\
    Durch Eingabe einer UniProt-ID $^1$ gibt es eine URL zur ```pbd```-Datei der vorhergesagten Proteinstruktur zurück.\
    Argument: ```string```\
    Ausgabe: ```dictionary```\

12. ```generate_protein()```\
    Durch Eingabe des resultierenden Dictionarys von ```alphafold_prediction()``` gibt es eine Visualisierung der vorhergesagten Proteinstruktur zurück.\
    Argument: ```dictionary```\
    Ausgabe: ```None```

13. ```cut_dna(string, integer)```\
    Teilt die DNA-Zeichenkette an der angegebenen Position in zwei Teile auf.\
    Argument: ```string und integer```\
    Ausgabe: ```string``` Ursprüngliche DNA mit einem markierten Schnitt

14. ```repair_dna(string, string, integer, string)```
    Repariert eine geschnittene DNA-Zeichenkette, indem entweder eine Basis gelöscht (NHEJ) oder spezifische Basen an der angegebenen Position hinzugefügt werden (HDR).\
    Argument: ```string``` DNA-Zeichenkette\
            ```string``` Reparaturtyp (NHEJ oder HDR)\
            ```integer``` Optional: Schnittposition\
            ```string``` Optional: Zeichenkette zum Einfügen bei der HDR-Reparatur\
    Ausgabe: ```string``` Reparierte DNA

15. ```finden(string, sequence)```\
    Um eine lokale string in einer globale string zu finden.\
    Argument: ```string, string``` (global, local)\
    Ausgabe: ```[int, int]``` Indizes der gefundenen Position\

16. ```codon_checken(string)```\
    Prüft auf falsche Codons in einer DNA- oder RNA-Sequenz.\
    Argument: ```string```\
    Ausgabe: ```['ABC']``` liste von falschen Codons\

$^1$ Die Alphafold-API akzeptiert nur UniProt-IDs als Eingabe. Sie können die UniProt-ID eines Proteins oder Gens im Internet finden. Wir empfehlen die folgenden Datenbanken.
1. Offizielle UniProt-Website: [https://www.uniprot.org](https://www.uniprot.org)
2. Für Gene: [https://www.ensembl.org/Multi/Tools/Blast](https://www.ensembl.org/Multi/Tools/Blast)
3. UniProt-IDs sind auf der Alphafold-Website selbst verfügbar: [https://alphafold.ebi.ac.uk](https://alphafold.ebi.ac.uk)

Bitte beachten Sie, dass ein Schritt-für-Schritt-Leitfaden zur Erlangung von UniProt-IDs bald verfügbar sein wird.

## Beispiele für Anfänger

### DNA in RND und Aminosäuren übersetzen
```python
# Eingabe
my_dna = 'TACCACGTGGACTGAGGACTCCTCATT' # geben Sie eine DNA-Zeichenkette ein

# erhalten Sie die RNA-Zeichenkette
my_rna = gen_api.dna2rna(my_dna)
print(my_rna)

# erhalten Sie die Aminosäure-Zeichenkette
my_amino = gen_api.rna2amino(my_rna)
print(my_amino)
```

### Erstellen einer Mutation
```python
# Eingabe
my_dna = 'TACCACGTGGACTGAGGACTCCTCATT' # geben Sie eine DNA-Zeichenkette ein

# erstellen Sie eine Mutation
mutation = gen_api.createmutation(my_dna)
print(mutation)

# erhalten Sie den Ort, an dem die Mutation stattgefunden hat
index = gen_api.compare(my_dna, mutation)
print(index)
```

### Öffnen einer txt-Datei und Verwendung von Iteration
```python
# lesen Sie die Eingabedatei
dnas = gen_api.read_input('/examples/my_dnas.txt') # beachten Sie, dass Sie eine Datei mit diesem Namen im gleichen Verzeichnis wie diese Datei gespeichert haben müssen
functions = ['createmutation', 'dna2rna', 'rna2amino'] # welche Funktionen möchten Sie ausführen
output = gen_api.iterate(dnas, functions) # rufen Sie die Iterationsfunktionen auf
print(output) # zeigen Sie die Ausgabe von iterate()
```

### Visualisierung eines Proteins
```python
# dies ist die Aminosäuresequenz für das Protein
# Hier wird die Aminosäuresequenz mit dem ersten Buchstaben jedes Aminosäure (anstatt der vorherigen 3 Buchstaben) dargestellt
amino = 'MAGELVSFAVNKLWDLLSHEYTLFQGVEDQVAELKSDLNLLKSFLKDADAKKHTSALVRYCVEEIKDIVYDAEDVLETFVQKEKLGTTSGIRKHIKRLTCIVPDRREIALYIGHVSKRITRVIRDMQSFGVQQMIVDDYMHPLRNREREIRRTFPKDNESGFVALEENVKKLVGYFVEEDNYQVVSITGMGGLGKTTLARQVFNHDMVTKKFDKLAWVSVSQDFTLKNVWQNILGDLKPKEEETKEEEKKILEMTEYTLQRELYQLLEMSKSLIVLDDIWKKEDWEVIKPIFPPTKGWKLLLTSRNESIVAPTNTKYFNFKPECLKTDDSWKLFQRIAFPINDASEFEIDEEMEKLGEKMIEHCGGLPLAIKVLGGMLAEKYTSHDWRRLSENIGSHLVGGRTNFNDDNNNSCNYVLSLSFEELPSYLKHCFLYLAHFPEDYEIKVENLSYYWAAEEIFQPRHYDGEIIRDVGDVYIEELVRRNMVISERDVKTSRFETCHLHDMMREVCLLKAKEENFLQITSNPPSTANFQSTVTSRRLVYQYPTTLHVEKDINNPKLRSLVVVTLGSWNMAGSSFTRLELLRVLDLVQAKLKGGKLASCIGKLIHLRYLSLEYAEVTHIPYSLGNLKLLIYLNLHISLSSRSNFVPNVLMGMQELRYLALPSLIERKTKLELSNLVKLETLENFSTKNSSLEDLRGMVRLRTLTIELIEETSLETLAASIGGLKYLEKLEIDDLGSKMRTKEAGIVFDFVHLKRLRLELYMPRLSKEQHFPSHLTTLYLQHCRLEEDPMPILEKLLQLKELELGHKSFSGKKMVCSSCGFPQLQKLSISGLKEWEDWKVEESSMPLLLTLNIFDCRKLKQLPDEHLPSHLTAISLKKCGLEDPIPTLERLVHLKELSLSELCGRIMVCTGGGFPQLHKLDLSELDGLEEWIVEDGSMPRLHTLEIRRCLKLKKLPNGFPQLQNLHLTEVEEWEEGMIVKQGSMPLLHTLYIWHCPKLPGEQHFPSHLTTVFLLGMYVEEDPMRILEKLLHLKNVSLFQSFSGKRMVCSGGGFPQLQKLSIREIEWEEWIVEQGSMPLLHTLYIGVCPNLKELPDGLRFIYSLKNLIVSKRWKKRLSEGGEDYYKVQHIPSVEFDD'

# Dies ist die UniProt-ID für dieses Protein
uniprot_id = 'Q8W3K0'

# Jetzt holen wir die AlphaFold-Strukturvorhersage
structure = gen_api.alphafold_prediction(uniprot_id)

# Schließlich rufen wir generate_protein() auf, um die Vorhersage anzuzeigen
protein = gen_api.generate_protein(structure)
```

### Simulation von CRISPR Cas
```python
my_dna = 'TACCACGTGGACTGAGGACTCCTCATT' # geben Sie eine DNA-Zeichenkette ein
print('Ursprüngliche DNA:', my_dna)

# Schneiden Sie die DNA an Position 16
cut_position = 16
cut_dna = gen_api.cut_dna(my_dna, cut_position)
print('Geschnittene DNA: ', cut_dna)

# Reparieren Sie die DNA mit NHEJ (Löschung)
nhej_repaired_dna = gen_api.repair_dna(my_dna, cut_position, 'NHEJ')
print('NHEJ reparierte DNA: ', nhej_repaired_dna)

# Reparieren Sie die DNA mit HDR (Einfügen von 'XYZ')
hdr_repaired_dna = gen_api.repair_dna(my_dna, cut_position, 'HDR', repair_sequence='XYZ')
print('HDR reparierte DNA: ', hdr_repaired_dna)
```

## Zitieren Sie die gen API
Wenn Sie diesen Code verwenden, zitieren Sie ihn bitte:
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

## Mitwirken
Bitte kontaktieren Sie mich per [E-Mail](mailto:joanalnu@outlook.com) oder senden Sie Pull-Requests.

## Info für Lehrkräfte
Dies ist die formale API für die [genetic10](https://joanalnu.github.io/genetics10)-Bildungssoftware. Während das Jupyter-Notebook eine benutzerfreundliche Schnittstelle ist und keine Installation erfordert, was es ideal für schulverwaltete Geräte macht, ist die API für den Einsatz in einem professionellen Umfeld konzipiert. Es liegt an Ihnen zu entscheiden, ob Sie die API oder das Jupyter-Notebook verwenden, unter Berücksichtigung des Ausbildungsstandes Ihrer Schüler und der verfügbaren Ressourcen.

### Wie kann ich dies in meinem Unterricht verwenden?
Zuerst identifizieren Sie in Ihrem Lehrplan, wo Sie die Software integrieren können, die bereits an die allgemeinen Bildungsrichtlinien angepasst ist. Dann sollten Sie damit beginnen, die grundlegenden Konzepte der Genomik in Ihrem Biologie- oder Naturwissenschaftsunterricht zu erklären, wie Sie es normalerweise tun würden. Dann können Sie dieses Tool Ihren Schülern vorstellen und erklären, wie es verwendet wird.

Sie können die Software verwenden, um Problemlösungsaufgaben zu entwerfen, die von den Schülern kritisches Denken und Programmierkenntnisse erfordern. Zum Beispiel ein Szenario, in dem eine Genmutation eine Krankheit verursacht und die Schüler aufgefordert werden, Code zu schreiben, der die Mutation identifiziert und korrigiert. Diese Art von Aktivitäten fördert Kreativität und Problemlösungsfähigkeit und führt zu mehr Wissenschaft wie CRIPSR-Cas9.

Außerdem führen Sie geplante Aktivitäten durch, bei denen die Schüler das Gelernte im realen Leben anwenden. Erstellen Sie Aufgaben, bei denen die Schüler einfachen Code mit den vordefinierten Funktionen schreiben, um genetische Prozesse wie Transkription und Translation zu emulieren.

Durch die Bereitstellung von Schritt-für-Schritt-Anleitungen haben die Schüler bessere Chancen, den biologischen Inhalt zu verstehen und das volle Potenzial dieses Tools zu nutzen. Darüber hinaus kann die Integration von realen Beispielen und Anwendungen in der Genomik und Biotechnologie die Motivation und das Interesse der Schüler erhöhen und moderne Forschungsinstrumente zeigen und diskutieren.

Schließlich können Sie auch einen umgekehrten Unterrichtsansatz verfolgen, indem Sie Software-Tutorials als Hausaufgabe zuweisen und die Unterrichtszeit für interaktives und angewandtes Lernen nutzen. Dies ermöglicht eine maximale Beteiligung im Unterricht und ermöglicht eine individuellere Anleitung.

Durch die Förderung der Zusammenarbeit durch die Planung von Gruppenprojekten können die Schüler zusammenarbeiten, um komplexere Probleme zu lösen. Und kollaborative Projekte fördern Teamarbeit und ermöglichen es den Schülern, voneinander zu lernen.

Durch die Integration dieser Strategien können Sie diese Software effektiv nutzen, um Ihren Biologieunterricht zu verbessern, die Schüler zu engagieren und ein tieferes Verständnis von Genomik und Programmierung zu fördern.

### Warum sollte ich dies in meinem Unterricht verwenden?
Dies ist eine nützliche Ressource für Schüler, um Genomik und grundlegende Programmierung zu lernen. Einerseits ist dies ein leistungsstarkes Tool, das es den Schülern ermöglicht, das Gelernte im Bereich Biologie anzuwenden. Es ist interaktiv und anpassbar und jeder kann seinen eigenen Code ohne Programmierkenntnisse ausführen. Andererseits werden die Schüler lernen und erste Erfahrungen mit Bioinformatik und Rechnung sammeln. Programmierung ist eine wesentliche Fähigkeit für zukünftige Arbeitnehmer, unabhängig von ihrem Fach.

Darüber hinaus macht die Tatsache, dass es webbasiert ist und keine Installation benötigt, es perfekt für schulverwaltete Geräte und ermöglicht die Nutzung unabhängig vom Betriebssystem. Es fördert auch Teamarbeit und Kommunikationsfähigkeiten, da Projekte in Zusammenarbeit durchgeführt werden können.

Darüber hinaus sind die Funktionen der Software an den schulischen Lehrplan angepasst und zeigen praktische Anwendungen des Unterrichtsinhalts sofort. Es fördert auch kritisches Denken, indem es den Schülern ermöglicht, eigenen Code zu schreiben, um Probleme zu lösen und aktiv zu engagieren. Und vorherige Kenntnisse in der Programmierung sind nicht erforderlich, da die Schüler die vordefinierten Funktionen verwenden, die eine breite Palette von Möglichkeiten ermöglichen. Darüber hinaus können die Schüler ihren Code an ihre Probleme anpassen oder neue Funktionen schreiben. Der Code ist leicht skalierbar und hat endlose Möglichkeiten!

### Kontaktieren Sie mich!
Wenn Sie weitere Fragen haben, zögern Sie nicht, mich per [E-Mail](mailto:joanalnu@outlook.com) zu kontaktieren. Ich bin auch offen für die Planung von Besprechungen oder Anrufen.

Bitte beachten Sie, dass die Arbeit an weiteren Übersetzungen im Gange ist.