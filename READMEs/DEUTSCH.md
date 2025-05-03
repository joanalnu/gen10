# gen10
---

[![repo](https://img.shields.io/badge/GitHub-joanalnu%2Fgen10-blue.svg?style=flat)](https://github.com/joanalnu/gen10)
[![license](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/joanalnu/gen10/LICENSE)
![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue)
[![DOI](https://zenodo.org/badge/885760467.svg)](https://doi.org/10.5281/zenodo.14059748)

![Build Status](https://github.com/joanalnu/gen10/actions/workflows/python-tests.yml/badge.svg)
![Open Issues](https://img.shields.io/github/issues/joanalnu/gen10)
![GitHub Release](https://img.shields.io/github/v/release/joanalnu/Gen10?color=teal)

### Inhaltsverzeichnis
- [Einführung](#einführung)
- [Andere Sprachen](#lesen-sie-die-dokumentation-in-ihrer-sprache)
- [Installation](#installation)
- [Verwendung](#verwendung)
- [Methoden](#methoden)
- [Zitieren dieses Pakets](#zitieren-des-gen10-pakets)
- [Mitwirken](#mitwirken)
- [Informationen für Lehrkräfte](#informationen-für-lehrkräfte)
- [Kontakt](#kontakt)


---

## Einführung

*`gen10`* ist ein Paket für Genomdatenanalyse und Visualisierung, das die richtigen Werkzeuge in Ihren Python-Code integriert. Das ursprüngliche Ziel dieses Pakets ist es, Unterstützung und Werkzeuge für den Unterricht in der Oberstufe oder Hochschule bereitzustellen, aber es kann für jeden anwendbaren Zweck verwendet werden.

Das `gen10`-Paket ermöglicht es Ihnen, eine große und wachsende Vielfalt von Aufgaben durchzuführen, von der Übersetzung von DNA in RNA- oder Proteinsequenzen bis hin zum Abrufen von Alphafold-Strukturvorhersagen, der Simulation von Mutationen und vielem mehr! `gen10` ist ein leistungsstarkes Werkzeug und gleichzeitig einfach zu bedienen, damit Schüler experimentieren, lernen und ihren eigenen Code erstellen können. Es benötigt keine Softwareinstallation und kann direkt aus einem Webbrowser verwendet werden.

Wenn Sie Lehrkraft sind, können Sie im Abschnitt [Informationen für Lehrkräfte](#informationen-für-lehrkräfte) sehen, warum Sie dies in Ihren Unterricht integrieren sollten.

## Lesen Sie die Dokumentation in Ihrer Sprache
- [Lesen Sie die Dokumentation in Ihrer Sprache](https://github.com/joanalnu/gen10/blob/main/READMES/ENGLISH.md)
- [Lee la documentación en tu lenguaje](https://github.com/joanalnu/gen10/blob/main/READMES/ESPANOL.md)
- [Lesen Sie das Dokument in ihrer Sprache](https://github.com/joanalnu/gen10/blob/main/READMES/DEUTSCH.md)
- [Llegeix la documentació en el seu idioma](https://github.com/joanalnu/gen10/blob/main/READMES/CATALA.md)

## Installation
Sie können das Paket mit pip installieren:
```bash
pip install gen10
```

Alternativ können Sie ein browserbasiertes Notebook verwenden, um mit dem Paket zu interagieren und Ihren Code zellenweise auszuführen. Dies ist ein sehr nützliches Werkzeug für den Unterricht. Wir haben ein Schritt-für-Schritt-Tutorial in einem Google Colab Notebook [hier](https://colab.research.google.com/drive/1gPxB2i7kRtKM-BUmg1gMipZk5Z5G0OEb?usp=sharing) vorbereitet.

## Verwendung
`gen10` funktioniert wie jedes andere `pip`-Paket. Sie können es in Ihren Code importieren, indem Sie
```python
import gen10
```
hinzufügen und dann die vom Paket bereitgestellten Methoden verwenden. Denken Sie daran, um eine Methode aus einem Paket in Python zu verwenden, sollten Sie schreiben:
```python
output = gen10.method_name(arguments)
```
Wenn Sie völlig neu im Programmieren oder in Python sind, können Sie mit dem oben genannten Tutorial im Google Colab Notebook beginnen.

## Methoden
Die derzeit verfügbaren Methoden sind die folgenden. Beachten Sie, dass wir die Methoden ständig aktualisieren und neue hinzufügen!

| # | Name | Beschreibung | Argumente | Ausgaben |
| --- | --- | --- | --- | --- |
| 1 | dna2rna() | Transkribiert den bereitgestellten DNA-String in einen RNA-String, indem die Basen geändert werden (A->U, T->A, C->G, G->C). | string | string |
| 2 | rna2amino() | Transkribiert den bereitgestellten DNA-String in eine Aminosäurekette, indem Codons (3 Basen) gelesen und der Katalog verwendet wird. | string | string |
| 3 | dna2amino() | Transkribiert DNA-Strings direkt in Aminosäureketten, es ist eine Kombination der Methoden dna2rna und rna2amino. | string | string |
| 4 | rna2dna() | Transkribiert RNA-Strings zurück in DNA-Strings. | string | string |
| 5 | vergleichen() | Vergleicht die Strings (unabhängig davon, ob DNA, RNA oder Aminosäuren), gibt immer einen Boolean und einen String zurück. True, wenn beide Strings identisch sind, oder False und wo die Strings sich unterscheiden. | string1, string2 | boolean, string |
| 6 | checken() | Prüft, ob der bereitgestellte String eine gültige DNA- oder RNA-Sequenz ist. Prüft nicht auf Aminosäureketten. | string | string |
| 7 | input_lesen() | Wird verwendet, um Dateien zu öffnen. Der vollständige Pfad zur Datei muss im selben Ordner wie diese Datei gespeichert sein und darf nur eine Sequenz enthalten. | string | string |
| 8 | mutation_erstellen() | Gibt einen neuen String mit einer Mutation zurück (nur 1 pro Ausführung). Die Mutation kann eine Base ändern, eine Base löschen oder eine neue an einer beliebigen Position hinzufügen. | string | string |
| 9 | iterieren() | Durch Eingabe einer Liste von Eingaben und einer Liste von Funktionen gibt es eine Tabelle mit allen Ergebnissen für jede Funktion und Eingabe zurück. | list, list | dataframe (Tabelle) |
| 10 | zueinfach() | Transkribiert eine Aminosäurekette vom Drei-Buchstaben-Code in den Ein-Buchstaben-Code. | string | string |
| 11 | alphafold_struktur() | Durch Eingabe einer UniProt-ID $^1$ gibt es eine URL zur `pdb`-Datei der vorhergesagten Proteinstruktur zurück. | string | dictionary |
| 12 | protein_generieren() | Durch Eingabe des resultierenden Wörterbuchs von `alphafold_struktur()` gibt es eine Visualisierung der vorhergesagten Proteinstruktur zurück. | dictionary | None |
| 13 | dna_scheiden(string, integer) | Schneidet den DNA-String an der angegebenen Position in zwei Teile. | string und integer | string Original-DNA mit markiertem Schnitt |
| 14 | dna_reparieren(string, string, integer, string) | Repariert einen geschnittenen DNA-String, indem entweder eine Base gelöscht wird (NHEJ) oder spezifische Basen an der angegebenen Stelle hinzugefügt werden (HDR). | string DNA-String, string Reparaturtyp (NHEJ oder HDR), integer Optional: Schnittposition, string Optional: einzufügender String bei HDR-Reparatur | string Reparierte DNA |
| 15 | finden(string, sequence) | Findet eine lokale Sequenz in einer größeren, globalen Sequenz. | string, string (global, lokal) | [(int, int)] Indizes der gefundenen Position |
| 16 | codon_checken(string) | Prüft auf nicht existierende Codons in einer DNA- oder RNA-Sequenz. | string | ['ABC'] Liste nicht existierender Codons |
| 17 | komplementare(dna) | Berechnet das reverse Komplement einer gegebenen DNA-Sequenz. | string | string |
| 18 | gc_gehalt(dna) | Berechnet den GC-Gehalt (Prozentsatz) einer gegebenen DNA-Sequenz. | string | float |
| 19 | schmelz_temperatur(dna) | Berechnet die Schmelztemperatur (Tm) einer kurzen DNA-Sequenz mit der Wallace-Regel. | string | float |
| 20 | stelle_mutieren(sequence, pos, new_base) | Diese Funktion mutiert eine spezifische Stelle in einer DNA-Sequenz. | string, int, string | string |
| 21 | pcr_simulieren(sequence, fwd_primer, rev_primer) | Diese Funktion simuliert eine PCR-Reaktion mit der bereitgestellten Sequenz, Vorwärts- und Rückwärtsprimern. | string, string, string | string |
| 22 | typ_bestimmen(sequence) | Generiert eine eindeutige Kennung für die Sequenz, indem geprüft wird, ob es sich um DNA, RNA oder Protein handelt. | string | string |
| 23 | fasta_schreiben(sequences, identifiers=None, filename="output.fasta") | Schreibt eine oder mehrere Sequenzen in eine FASTA-Datei, getrennt durch eine Leerzeile. | string oder Liste von Strings, string oder Liste von Strings (optional), string (optional) | None (geschriebene Datei) |
| 24 | fasta_lesen(filename) | Liest eine FASTA-Datei und gibt Listen von Sequenzkennungen und Sequenzen zurück. | string | Kennungen (Liste), Sequenzen (Listen) |
| 25 | lesen_genbank(filename) | Parst die Daten aus einer GenBank-Datei in ein verwendbares Wörterbuch. | Dateiname (str) | Wörterbuch |

$^1$ Das Alphafold-Paket akzeptiert nur UniProt-IDs als Eingabe. Sie können die UniProt-ID eines Proteins oder Gens im Web finden. Wir empfehlen die folgenden Datenbanken.
1. Offizielle UniProt-Website: [https://www.uniprot.org](https://www.uniprot.org)
2. Für Gene: [https://www.ensembl.org/Multi/Tools/Blast](https://www.ensembl.org/Multi/Tools/Blast)
3. UniProt ist auch auf der Alphafold-Website verfügbar: [https://alphafold.ebi.ac.uk](https://alphafold.ebi.ac.uk)

## Zitieren des `gen10`-Pakets
Wenn Sie diesen Code verwenden, zitieren Sie ihn bitte wie folgt:
```bibtex
@software{joanalnu_2025,
    author = [Alcaide-Núñez, Joan],
    title = {GEN10 package},
    month = {April},
    year = {2025},
    publisher = {Zenodo},
    version = {1.4.2},
    doi = {10.5281/zenodo.15251890},
    url = {https://github.com/joanalnu/gen10},
}
```

## Mitwirken
Sie können gerne Probleme melden oder Pull Requests an das Repository senden!

## Informationen für Lehrkräfte
Ein Paket ist ein Python-Code, der Funktionen (d.h. Methoden) bereitstellt, die direkt in Ihrem Code verwendet werden können, indem Sie sie einfach aufrufen, ohne weiteren Code schreiben zu müssen. Notebooks sind für Schüler leicht nutzbar und da sie browserbasiert sind, benötigen sie keine Installation, was sie ideal für schulisch verwaltete Geräte macht.

### Wie kann ich das in meinem Unterricht verwenden?
Zuerst identifizieren Sie in Ihrem Lehrplan, wo Sie die Software integrieren können, die bereits an die allgemeinen Bildungsrichtlinien angepasst ist. Dann sollten Sie damit beginnen, die grundlegenden Konzepte der Genomik in Ihrem Biologie- oder Naturwissenschaftsunterricht zu erklären, wie Sie es normalerweise tun würden. Danach können Sie dieses Werkzeug den Schülern vorstellen und erklären, wie man es benutzt.

Sie können die Software verwenden, um Problemlösungsaufgaben zu entwerfen, die von den Schülern kritisches Denken und Programmierfähigkeiten erfordern. Zum Beispiel ein Szenario, in dem eine Genmutation eine Krankheit verursacht, und die Schüler sollen Code schreiben, der die Mutation identifiziert und korrigiert. Diese Art von Aktivitäten fördert Kreativität und Problemlösungsfähigkeiten und führt weiter zu wissenschaftlichen Themen wie CRISPR-Cas9.

Führen Sie auch geplante Aktivitäten durch, bei denen die Schüler das Gelernte in der Praxis anwenden. Erstellen Sie Aufgaben, bei denen die Schüler einfachen Code schreiben, der vorgefertigte Funktionen verwendet, um genetische Prozesse wie Transkription und Translation zu simulieren.

Durch Schritt-für-Schritt-Anleitungen haben die Schüler bessere Chancen, den biologischen Inhalt zu verstehen und das volle Potenzial dieses Werkzeugs zu nutzen. Außerdem kann die Integration von realen Beispielen und Anwendungen in Genomik und Biotechnologie die Motivation und das Interesse der Schüler steigern und moderne Forschungstools aufzeigen und diskutieren.

Schließlich können Sie auch einen umgedrehten Unterrichtsansatz (Flipped Classroom) verwenden, indem Sie Software-Tutorials als Hausaufgaben aufgeben und die Unterrichtszeit für interaktives und angewandtes Lernen nutzen. Dies maximiert die Beteiligung im Unterricht und ermöglicht eine individuellere Betreuung.

Durch die Förderung von Zusammenarbeit durch Gruppenprojekte können Schüler gemeinsam komplexere Probleme lösen. Kollaborative Projekte fördern Teamarbeit und ermöglichen es den Schülern, voneinander zu lernen.

Durch die Umsetzung dieser Strategien können Sie diese Software effektiv nutzen, um Ihren Biologieunterricht zu verbessern, Schüler zu engagieren und ein tieferes Verständnis sowohl der Genomik als auch des Programmierens zu fördern.

### Warum sollte ich das in meinem Unterricht verwenden?
Dies ist eine nützliche Ressource für Schüler, um sowohl Genomik als auch grundlegendes Programmieren zu lernen. Einerseits ist es ein leistungsstarkes Werkzeug, das es den Schülern ermöglicht, das Gelernte zur Biologie anzuwenden. Es ist interaktiv und anpassbar gestaltet, und jeder kann seinen eigenen Code ausführen, ohne Programmierkenntnisse zu haben. Andererseits lernen die Schüler erste Erfahrungen mit Bioinformatik und Computation. Programmieren ist eine wesentliche Fähigkeit für zukünftige Arbeitskräfte, unabhängig vom Fachgebiet.

Außerdem ist es webbasiert und benötigt keine Installation, was es perfekt für schulisch verwaltete Geräte macht und die Nutzung unabhängig vom Betriebssystem ermöglicht. Es fördert auch Teamarbeit und Kommunikationsfähigkeiten, da Projekte in Zusammenarbeit durchgeführt werden können.

Zusätzlich sind die Funktionen der Software auf den Lehrplan abgestimmt und zeigen praktische Anwendungen des Unterrichtsinhalts sofort auf. Es fördert kritisches Denken, indem es den Schülern ermöglicht, eigenen Code zu schreiben, um Probleme zu lösen und sich aktiv zu beteiligen. Programmierkenntnisse sind nicht erforderlich, da die Schüler vorgefertigte Funktionen verwenden, die eine breite Palette von Möglichkeiten bieten. Außerdem können die Schüler ihren Code an ihre Probleme anpassen oder neue Funktionen schreiben. Der Code ist leicht skalierbar und bietet endlose Möglichkeiten!

## Kontakt
Wenn Sie weitere Fragen, Kommentare oder Vorschläge haben, erreichen Sie mich unter [joanalnu@outlook.com](mailto:joanalnu@outlook.com).

Bitte beachten Sie, dass Übersetzungen in andere Sprachen (des Pakets, der Notebook-Tutorials, der README und anderer Dokumentationen) willkommen sind. Ich helfe gerne bei Übersetzungen auf Anfrage.
