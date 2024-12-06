from random import randint
import pandas as pd
import os
import requests

from Bio.PDB import PDBParser
import matplotlib.pyplot as plt # this is API-specific for protein structure visualization
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import Normalize
from matplotlib import cm

dirpath = os.path.dirname(os.path.abspath(__file__))

def adn2arn(dna):
    """Retorna una cadena d'ARN introduïnt una cadena d'ADN"""
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
            raise ValueError("Error: no s'ha pogut llegir la cadena d'ADN")
    return rna

def arn2amino(rna):
    """Retorna una cadena d'aminoàcids introduïnt una cadena d'ARN"""
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
            raise ValueError(f'Error: codó invàlid {codon}')
    return amino

def adn2amino(dna):
    """Retorna una cadena d'aminoàcids introduïnt una cadena d'ADN"""
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
            raise ValueError("Error: no s'ha pogut llegir la cadena d'ADN")

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
            raise ValueError(f'Error: códo invàlid {codon}')
    return amino

def compara(original, copy):
    """Compara dues cadenes (original, copy) i retorna la diferència"""
    if len(original) != len(copy):
        return 'Longitud diferent'
    else:
        for i in range(len(original)):
            if original[i]!=copy[i]:
                return f'Diferència a la base/aminoàcid {i+1}'
        return "Idèntiques"

def comprova(string):
    if len(string)%3 == 0:
        if string[:3]=='TAC' and (string[-3:]=='ATT' or string[-3:]=='ATC' or string[-3:]=='ACC'):
            return "Cadena d'ADN vàlida"
        elif string[:3]=='AUG' and (string[-3:]=='UAA' or string[-3:]=='UAG' or string[-3:]=='UGG'):
            return "Cadena d'ARN vàlida"
        else:
            raise ValueError("Cadena invàlida (no s'ha trobat el códo inicial/final)")

def llegir_input(path):
    """Si es una cadena retorna la cadena; si es el nom d'un arxiu retorna una llista del contingut"""
    if path[-3:]=='txt':
        try:
            file = open(path, 'r')
            contents = list()
            for line in file:
                contents.append(line.replace('\n', ''))
            return contents
        except OSError or KeyError:
            raise ValueError("No s'ha trobat l'arxiu, recorda que ha de ser a la mateix carpeta que aquest document.")
    else:
        return path

def crearmutacio(string):
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

def iterar(strings, functions, filepath=dirpath):
    """Crea un document CSV en aquesta carpeta amb la informació que demanis."""
    """L'argument consisteix d'una llista d'entrades i una llista de funcions"""
    columns = ['input']+[function for function in functions]
    df = pd.DataFrame(columns=columns)

    for string in strings:
        memory = [string]
        for function in functions:
            result = getattr(function)(memory[-1])
            memory.append(result)
        df = pd.concat([df, pd.DataFrame([memory], columns=columns)], ignore_index=True)

    df.to_csv(f'{filepath}/resultats.csv', index=False)
    return df

def asenzill(sin):
    inp = sin.split()
    sout=''
    for banse in inp:
        sout+=base[0]
    return sout

def alphafold(uniprot_id):
    url = f'https://alphafold.ebi.ac.uk/api/prediction/{uniprot_id}'
    response = requests.get(url)
    if response.status_code == 200:
        request_output = response.json()
        return request_output[0]
    else:
        raise ValueError(f"Error a l'obtenir lesdades: {response.status_code}")
        return None

def generar_proteina(structure_dict, filepath='alphafold_protein_structure_prediction.pdb', show=True):
    url = structure_dict['pdbUrl']
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
        with open(filepath, 'wb') as f:
            f.write(content)

        parser = PDBParser()
        structure = parser.get_structure("alphafold_protein_structure_prediction.pdb", filepath)

        # Extract atomic coordinates
        x_coords = []
        y_coords = []
        z_coords = []
        accuracy_scores = []

        for atom in structure.get_atoms():
            x, y, z = atom.coord
            x_coords.append(x)
            y_coords.append(y)
            z_coords.append(z)
            accuracy_scores.append(atom.bfactor)

        # Normalize colors
        norm = Normalize(vmin=0, vmax=100)
        cmap = cm.hsv
        colors = cmap(norm(accuracy_scores))

        fig = plt.figure(figsize=(8,6))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(x_coords, y_coords, z_coords, c=colors, s=20, alpha=0.7, edgecolors='k')
        ax.plot(x_coords, y_coords, z_coords, color='black', linewidth=1.0, alpha=0.7)

        # Add labels
        ax.set_xlabel('Eix X')
        ax.set_ylabel('Eix Y')
        ax.set_zlabel('Eix Z')
        cbar = fig.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, pad=0.1)
        cbar.set_label("Seguretat de Predicció (0%-100%)")

        plt.grid(True)
        if show is True:
            plt.show()

    else:
        raise ValueError(f'Error al descarregar les dades. Codi: {response.status_code}')

def tallar_adn(dna, cut_pos):
    """Talla l'ADN al punt especificat."""
    if cut_pos<0 or cut_pos>=len(dna):
        raise ValueError('Posició especificada fora de l\'ADN')
    return dna[:cut_pos] + '|' + dna[cut_pos:]

def reparar_adn(dna, cut_pos, repair_type, nova_sequencia=None):
    """Repara l'ADN tallat."""

    if '|' in dna: # ignora posició i reparar al tall existent
        cut_pos = dna.index('|')
        if repair_type=='NHEJ': # Simular eliminació
            return dna[:cut_pos] + dna[cut_pos+2:] # Eliminant una base
        elif repair_type=='HDR' and nova_sequencia: # Simular inserció
            return dna[:cut_pos] + nova_sequencia + dna[cut_pos:]

    elif '|' not in dna: # utilitzar cut_pos
        if repair_type=='NHEJ': # Simular eliminació
            return dna[:cut_pos] + dna[cut_pos+2:] # Eliminant una base
        elif repair_type=='HDR' and nova_sequencia: # Simular inserció
            return dna[:cut_pos] + nova_sequencia + dna[cut_pos:]

    else:
        raise ValueError('Tipus de reparació o seqüència de reparació de missions no vàlids per a HDR.')