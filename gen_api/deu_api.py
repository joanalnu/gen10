from random import randint
import pandas as pd
import os
import requests
import py3Dmol
import gen_api

dirpath = os.path.dirname(os.path.abspath(__file__))

def dna2rna(self, dna):
    """Gibt RNA-String durch Eingabe eines DNA-Strings zurück"""
    rna = ""
    for base in dna:
        if base=='A' or base=='a':
            rna+='U'
        elif base=='T' or base=='t':
            rna+='A'
        elif base=='C' or base=='c':
            rna+='G'
        elif base=='G' or base=='g':
            rna+='C'
        else:
            raise ValueError('Fehler: Die angegebene DNA-Zeichenkette konnte nicht gelesen werden.')
    return rna

def rna2amino(self, rna):
    """Gibt Aminosäuren durch Eingabe einer RNA-Zeichenkette zurück"""
    amino=''
    codon_catalog = {'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
        'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
        'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': 'STOP', 'UAG': 'STOP',
        'UGU': 'Cys', 'UGC': 'Cys', 'UGA': 'STOP', 'UGG': 'Trp',
        'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
        'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
        'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
        'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
        'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met',
        'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
        'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
        'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
        'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
        'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
        'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
        'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'
    }
    for i in range(0, len(rna)-2, 3):
        codon = str(rna[i]+rna[i+1]+rna[i+2])
        if codon in codon_catalog:
            if codon_catalog[codon]=='STOP':
                break
            amino+= ' ' + codon_catalog[codon]
        else:
            raise ValueError(f'Error: invalid codon {codon}')
    return amino

def dna2amino(self, dna):
    """Gibt Aminosäuren durch Eingabe einer DNA-Zeichenkette zurück"""
    rna = ""
    for base in dna:
        if base=='A' or base=='a':
            rna+='U'
        elif base=='T' or base=='t':
            rna+='A'
        elif base=='C' or base=='c':
            rna+='G'
        elif base=='G' or base=='g':
            rna+='C'
        else:
            raise ValueError('Die angegebene DNA-Zeichenkette konnte nicht gelesen werden.')
    
    amino=''
    
    codon_catalog = {'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
        'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
        'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': 'STOP', 'UAG': 'STOP',
        'UGU': 'Cys', 'UGC': 'Cys', 'UGA': 'STOP', 'UGG': 'Trp',
        'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
        'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
        'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
        'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
        'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met',
        'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
        'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
        'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
        'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
        'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
        'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
        'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'
    }
    for i in range(0, len(rna)-2, 3):
        codon = str(rna[i]+rna[i+1]+rna[i+2])
        if codon in codon_catalog:
            if codon_catalog[codon]=='STOP':
                break
            amino+= ' ' + codon_catalog[codon]
        else:
            raise ValueError(f'Fehler: ungültiges Codon {codon}')
    return amino

def vergleichen(self, original, copy):
    """Vergleicht zwei verschiedene Zeichenketten (Original, Kopie) und gibt die Unterschiede"""
    if len(original) != len(copy):
        return 'not same length'
    else:
        for i in range(len(original)):
            if original[i]!=copy[i]:
                return f'Unterschiede in der {i} Base/Aminosäure'
        return "Identisch"

def checken(self, string):
    if len(string)%3 == 0:
        if string[:-3]=='TAC' and (string[-3]=='ATT' or string[-3]=='ATC' or string[-3]=='ACC'):
            return 'Gültiger DNA-String'
        elif string[:-3]=='AUG' and (string[-3]=='UAA' or string[-3]=='UAG' or string[-3]=='UGG'):
            return 'Gültiger RNA-String'
        else:
            raise ValueError('Ungültiger String (Start-/Endcodons nicht gefunden)')

def input_lesen(self, path):
    """Wenn string, wird string zurückgegeben; wenn ein txt-Dateipfad, wird string in file zurückgegeben"""
    if path[-3:]=='txt':
        try:
            file = open(f'{self.dirpath}/{path}', 'r')
            contents = list()
            for line in file:
                contents.append(line.replace('\n', ''))
            return contents
        except OSError or KeyError:
            raise ValueError('Die Datei konnte nicht geöffnet werden, bitte sehen Sie im Benutzerhandbuch nach.')
    else:
        return path

def mutation_erstellen(self, string):
    mutated = ""
    muttype = randint(1, 6)
    index = randint(0, len(string)-1)
    for i in range(len(string)):
        if i == index:
            if muttype==1: # change for A
                mutated+='A'
            elif muttype==2: # change for T
                mutated+='T'
            elif muttype==3: # change for C
                mutated+='C'
            elif muttype==4: # change for G
                mutated+='G'
            elif muttype==5: # remove base
                continue
            elif muttype==6: # add random base
                base = randint(1, 4)
                if base==1: mutated+='A'
                elif base==2: mutated+='T'
                elif base==3: mutated+='C'
                elif base==4: mutated+='G'
        else:
            mutated+=string[i]
    return mutated

def iterieren(self, strings, functions):
    """Erstellt eine CSV-Datei in Ihrem Verzeichnis mit den von Ihnen angeforderten Informationen."""
    """Das Argument besteht aus einer Liste von Zeichenketten und einer Liste von Funktionen"""
    columns = ['input']+[function for function in functions]
    df = pd.DataFrame(columns=columns)
    
    for string in strings:
        memory = [string]
        for function in functions:
            result = getattr(self, function)(memory[-1])
            memory.append(result)
        df = pd.concat([df, pd.DataFrame([memory], columns=columns)], ignore_index=True)
    
    df.to_csv(f'{self.dirpath}/Ergebnis.csv', index=False)
    return df

def zueinfach(self, sin):
    inp = sin.split()
    sout=''
    for base in inp:
        sout+=base[0]
    return sout

def alphafold_struktur(self, uniprot_id):
    url = f'https://alphafold.ebi.ac.uk/api/prediction/{uniprot_id}'
    response = requests.get(url)
    if response.status_code == 200:
        request_output = response.json()
        return request_output[0]
    else:
        raise ValueError(f'Daten können nicht abgerufen werden: {response.status_code}')
        return None

def download_pdb(self, url):
    response = requests.get(url)
    if response.status_code == 200:
        with open(f'{self.dirpath}/alphafold_protein__struktur.pdb', 'wb') as f:
            f.write(response.content)
        return True
    else:
        return False

def protein_generieren(self, structure_dict):
    url = structure_dict['pdbUrl']
    
    if gen_api.download_pdb(url):
        filepath = f'./gen_api/alphafold_protein__struktur.pdb'
        pdb_file = open(filepath).read()
        view = py3Dmol.view(width=400, height=400)
        view.addModel(pdb_file, 'pdb')
        view.setStyle({'cartoon': {'color': 'spectrum'}})
        view.zoomTo()
        return view.show()
    
def dna_schneiden(self, dna, cut_pos):
    """Schneidet DNA String an der Position cut_pos"""
    if cut_pos<0 or cut_pos>=len(dna):
        raise ValueError('Die Schnittposition befindet sich außerhalb des Strings.')
    return dna[:cut_pos] + '|' + dna[cut_pos:]

def dna_reparieren(self, dna, cut_pos, repair_type, neue_string=None):
    """Repariert DNA nach den Schnitt."""
    if '|' in dna: # Schnitt_pos ignorieren und auf vorhandenem Schnitt reparieren
        cut_pos = dna.index('|')
        if repair_type=='NHEJ': # Löschung simulieren
            return dna[:cut_pos] + dna[cut_pos+2:] # Löschen einer Basis
        elif repair_type=='HDR' and neue_string: # Einfügung simulieren
            return dna[:cut_pos] + neue_string + dna[cut_pos:]
    
    elif '|' not in dna: # cut_pos verwenden
        if repair_type=='NHEJ': # Löschung simulieren
            return dna[:cut_pos] + dna[cut_pos+2:] # Löschen einer Basis
        elif repair_type=='HDR' and neue_string: # Einfügung simulieren
            return dna[:cut_pos] + neue_string + dna[cut_pos:]
    
    else:
        raise ValueError('Ungültiger Reparaturtyp oder falsche Reparatursequenz für HDR.')