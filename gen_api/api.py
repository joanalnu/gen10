from random import randint
import pandas as pd
import os
import requests
import py3Dmol
import gen_api

dirpath = os.path.dirname(os.path.abspath(__file__))

def dna2rna(dna):
    """Returns RNA string by inputting a DNA string"""
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
            raise ValueError('Could not read provided DNA string')
    return rna

def rna2amino(rna):
    """Returns amino acids by inputting an RNA string"""
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

def dna2amino(dna):
    """Returns amino acids by inputting an DNA string"""
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
            raise ValueError('Could not read provided DNA string')
    
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

def compare(original, copy):
    """Compares two different string (original, copy) and return True or False with the reason"""
    if len(original) != len(copy):
        return 'not same length'
    else:
        for i in range(len(original)):
            if original[i]!=copy[i]:
                return f'Difference in {i} base/aminoacid'
        return "Identical"

def check(string):
    if len(string)%3 == 0:
        if string[:-3]=='TAC' and (string[-3]=='ATT' or string[-3]=='ATC' or string[-3]=='ACC'):
            return 'Valid DNA string'
        elif string[:-3]=='AUG' and (string[-3]=='UAA' or string[-3]=='UAG' or string[-3]=='UGG'):
            return 'Valid RNA string'
        else:
            raise ValueError('Invalid string (starting/ending codons not found)')

def read_input(path):
    """if string return string; if a txt file path returns string in file"""
    if path[-3:]=='txt':
        try:
            file = open(f'{dirpath}/{path}', 'r')
            contents = list()
            for line in file:
                contents.append(line.replace('\n', ''))
            return contents
        except OSError or KeyError:
            raise ValueError('Could not open file, please, check user guide.')
    else:
        return path

def createmutation(string):
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

def iterate(strings, functions):
    """Creates a CSV file in your directory with the information you request."""
    """The argument consits of a list of strings and a list of functions"""
    columns = ['input']+[function for function in functions]
    df = pd.DataFrame(columns=columns)
    
    for string in strings:
        memory = [string]
        for function in functions:
            result = getattr(function)(memory[-1])
            memory.append(result)
        df = pd.concat([df, pd.DataFrame([memory], columns=columns)], ignore_index=True)
    
    df.to_csv(f'{dirpath}/Results.csv', index=False)
    return df

def tosingle(sin):
    inp = sin.split()
    sout = ''
    for base in inp:
        sout+=base[0]
    return sout

def alphafold_prediction(uniprot_id):
    url = f'https://alphafold.ebi.ac.uk/api/prediction/{uniprot_id}'
    response = requests.get(url)
    if response.status_code == 200:
        request_output = response.json()
        return request_output[0]
    else:
        raise ValueError(f'Failed to fetch data: {response.status_code}')
        return None

def download_pdb(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open(f'{dirpath}/alphafold_protein__structure_prediction.pdb', 'wb') as f:
            f.write(response.content)
        return True
    else:
        return False

def generate_protein(structure_dict):
    url = structure_dict['pdbUrl']
    
    if gen_api.download_pdb(url):
        filepath = f'{dirpath}/alphafold_protein__structure_prediction.pdb'
        pdb_file = open(filepath).read()
        view = py3Dmol.view(width=400, height=400)
        view.addModel(pdb_file, 'pdb')
        view.setStyle({'cartoon': {'color': 'spectrum'}})
        view.zoomTo()
        return view.show()

def cut_dna(dna, cut_pos):
    """Cuts the DNA at the specified position."""
    if cut_pos<0 or cut_pos>=len(dna):
        raise ValueError("Cut position is out of bounds.")
    return dna[:cut_pos] + '|' + dna[cut_pos:]

def repair_dna(dna, cut_pos, repair_type, repair_sequence=None):
    """Repairs the DNA after a cut."""

    if '|' in dna: # ignore cut_pos and repair on existing cut
        cut_pos = dna.index('|')
        if repair_type=='NHEJ': # Simulate deletion
            return dna[:cut_pos] + dna[cut_pos+2:] # Deleting one base
        elif repair_type=='HDR' and repair_sequence: # Simulate insertion
            return dna[:cut_pos] + repair_sequence + dna[cut_pos:]
    
    elif '|' not in dna: # use cut_pos
        if repair_type=='NHEJ': # Simulate deletion
            return dna[:cut_pos] + dna[cut_pos+2:] # Deleting one base
        elif repair_type=='HDR' and repair_sequence: # Simulate insertion
            return dna[:cut_pos] + repair_sequence + dna[cut_pos:]
    
    else:
        raise ValueError("Invalid repair type or missiogn repair sequence for HDR.")