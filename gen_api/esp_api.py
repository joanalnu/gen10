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
    """Devuelve una secuencia de ARN al proporcionar una secuencia de ADN"""
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
            raise ValueError('Error: no se pudo leer la secuencia de ADN')
    return rna

def arn2amino(rna):
    """Devuelve una secuencia de aminoácidos al proporcionar una secuencia de ARN"""
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
            raise ValueError(f'Error: codón invalido {codon}')
    return amino

def adn2amino(dna):
    """Devuelve una secuencia de aminoácidos al proporcionar una secuencia de ADN"""
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
            raise ValueError('Error: no se pudo leer la secuencia de ADN')

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
            raise ValueError(f'Error: codón invalido {codon}')
    return amino

def comparar(original, copy):
    """Compara dos cadenas diferentes (original, copia) y devuelve la diferencia"""
    if len(original) != len(copy):
        return 'Longitud diferente'
    else:
        for i in range(len(original)):
            if original[i]!=copy[i]:
                return f'Diferencia en la {i+1} base/aminoácido'
        return "Identicas"

def comprobar(string):
    if len(string)%3 == 0:
        if string[:3]=='TAC' and (string[-3:]=='ATT' or string[-3:]=='ATC' or string[-3:]=='ACC'):
            return 'Secuencia de ADN válida'
        elif string[:3]=='AUG' and (string[-3:]=='UAA' or string[-3:]=='UAG' or string[-3:]=='UGG'):
            return 'Secuencia de ARN válida'
        else:
            raise ValueError('Secuencia inválida (codones iniciales/finales no encontrados)')
    else:
        raise ValueError('La secuencia no puede ser divida en codones.')

def leer_input(path):
    """Si es una secuencia devuelve la secuencia; si es un nombre de archivo txt devuelve una lista de secuencias del archivo"""
    if path[-3:]=='txt':
        try:
            file = open(path, 'r')
            contents = list()
            for line in file:
                contents.append(line.replace('\n', ''))
            return contents
        except OSError or KeyError:
            raise ValueError('No se pudo abrir el archivo. ¿Está en la misma carpeta que este documento?')
    elif path[-3:]=='pdf' or path[-3:]=='doc' or path[-4:]=='docx' or path[-3:]=='csv' or path[-4:]=='xlsx' or path[-4:]=='html':
        raise ValueError("El documento tiene que ser formato 'txt'.")
    else:
        return path

def crearmutacion(string):
    bases = ['A', 'T', 'C', 'G']
    mutated = ""

    while True:
        muttype = random.choices([1, 5, 6], weights=[75, 15, 10], k=1)[0] # weighted probabilties for biological reality
        index = random.randint(0, len(string) - 1)

        if muttype == 1:  # Substitution
            # Handle transition/transversion probabilities
            purines = ['A', 'G']
            pyrimidines = ['C', 'T']
            if string[index] in purines: # transititions are 2x more likely than transversions
                new_base = random.choices(purines + pyrimidines, weights=[2, 2, 1, 1], k=1)[0]
            else:
                new_base = random.choices(pyrimidines + purines, weights=[2, 2, 1, 1], k=1)[0]
            mutated = string[:index] + new_base + string[index + 1:]
        elif muttype == 5:  # Deletion
            del_length = random.choices([1, 2, 3], weights=[70, 20, 10], k=1)[0] # weighted random selection for length (1–3 bases)
            del_length = min(del_length, len(string) - index) # avoid index out of range
            mutated = string[:index] + string[index + del_length:]

        elif muttype == 6:  # Insertion
            insert_length = random.choices([1, 2, 3], weights=[70, 20, 10], k=1)[0] # weighted random selection for length (1-3 bases)
            insert_bases = ''.join(random.choices(bases, k=insert_length))
            mutated = string[:index] + insert_bases + string[index:]

        # Break the loop if the mutation differs from the original
        if mutated != string:
            break

    return mutated

def iterar(strings, functions, filepath=dirpath):
    """Crea un archivo CSV en tu directorio con la información que solicites"""
    """El argumento consiste en una lista de secuencias y una lista de funciones"""
    columns = ['input']+[function for function in functions]
    df = pd.DataFrame(columns=columns)

    for string in strings:
        memory = [string]
        for function in functions:
            result = getattr(function)(memory[-1])
            memory.append(result)
        df = pd.concat([df, pd.DataFrame([memory], columns=columns)], ignore_index=True)

    df.to_csv(f'{filpath}/resultados.csv', index=False)
    return df

def asencillo(sin):
    inp = sin.split()
    sout=''
    for base in inp:
        sout+=base[0]
    return sout

def alphafold(uniprot_id):
    url = f'https://alphafold.ebi.ac.uk/api/prediction/{uniprot_id}'
    response = requests.get(url)
    if response.status_code == 200:
        request_output = response.json()
        return request_output[0]
    else:
        raise ValueError(f'Error en la obtención de datos: {response.status_code}')
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
        ax.set_xlabel('Eje X')
        ax.set_ylabel('Eje Y')
        ax.set_zlabel('Eje Z')
        cbar = fig.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, pad=0.1)
        cbar.set_label("Precisión de predicción (0%-100%)")

        plt.grid(True)
        if show is True:
            plt.show()

    else:
        raise ValueError(f'Error al obtener los datos de la estructura de la proteína. Código de respuesta HTTP: {response.status_code}')

def cortar_adn(dna, cut_pos):
    """Corta el ADN en la posición especificada."""
    if cut_pos<0 or cut_pos>=len(dna):
        raise ValueError('La posicion especificada está fuera del ADN.')
    return dna[:cut_pos] + '|' + dna[cut_pos:]

def reparar_adn(dna, cut_pos, repair_type, nueva_secuencia=None):
    """Repara el ADN después de un corte."""

    if '|' in dna: # ignorar la posición especificada
        cut_pos = dna.index('|')
        if repair_type=='NHEJ': # Simular supresión
            return dna[:cut_pos] + dna[cut_pos+2:] # Eliminar una base
        elif repair_type=='HDR' and nueva_secuencia: # Simular inserción
            return dna[:cut_pos] + nueva_secuencia + dna[cut_pos:]

    elif '|' not in dna: # usar cut_pos
        if repair_type=='NHEJ': # Simular supresión
            return dna[:cut_pos] + dna[cut_pos+2:] # Eliminar una base
        elif repair_type=='HDR' and nueva_secuencia: # Simular inserción
            return dna[:cut_pos] + nueva_secuencia + dna[cut_pos:]

    else:
        raise ValueError('Tipo de reparación invalida o falta la nueva secuencia para HDR.')
