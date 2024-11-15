from random import randint
import pandas as pd
import os
import requests
import py3Dmol
import gen_api

dirpath = os.path.dirname(os.path.abspath(__file__))

def adn2arn(self, dna):
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

def arn2amino(self, rna):
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

def adn2amino(self, dna):
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

def comparar(self, original, copy):
    """Compara dos cadenas diferentes (original, copia) y devuelve la diferencia"""
    if len(original) != len(copy):
        return 'Longitud diferente'
    else:
        for i in range(len(original)):
            if original[i]!=copy[i]:
                return f'Diferencia en la {i} base/aminoácido'
        return "Identicas"

def comprobar(self, string):
    if len(string)%3 == 0:
        if string[:-3]=='TAC' and (string[-3]=='ATT' or string[-3]=='ATC' or string[-3]=='ACC'):
            return 'Secuencia de ADN válida'
        elif string[:-3]=='AUG' and (string[-3]=='UAA' or string[-3]=='UAG' or string[-3]=='UGG'):
            return 'Secuencia de ARN válida'
        else:
            raise ValueError('Secuencia inválida (codones iniciales/finales no encontrados)')

def leer_input(self, path):
    """Si es una secuencia devuelve la secuencia; si es un nombre de archivo txt devuelve una lista de secuencias del archivo"""
    if path[-3:]=='txt':
        try:
            file = open(f'{self.dirpath}/{path}', 'r')
            contents = list()
            for line in file:
                contents.append(line.replace('\n', ''))
            return contents
        except OSError or KeyError:
            raise ValueError('No se pudo abrir el archivo. ¿Está en la misma carpeta que este documento?')
    else:
        return path

def crearmutacion(self, string):
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

def iterar(self, strings, functions):
    """Crea un archivo CSV en tu directorio con la información que solicites"""
    """El argumento consiste en una lista de secuencias y una lista de funciones"""
    columns = ['input']+[function for function in functions]
    df = pd.DataFrame(columns=columns)
    
    for string in strings:
        memory = [string]
        for function in functions:
            result = getattr(self, function)(memory[-1])
            memory.append(result)
        df = pd.concat([df, pd.DataFrame([memory], columns=columns)], ignore_index=True)
    
    df.to_csv(f'{self.dirpath}/resultados.csv', index=False)
    return df

def asencillo(self, sin):
    inp = sin.split()
    sout=''
    for base in inp:
        sout+=base[0]
    return sout

def alphafold(self, uniprot_id):
    url = f'https://alphafold.ebi.ac.uk/api/prediction/{uniprot_id}'
    response = requests.get(url)
    if response.status_code == 200:
        request_output = response.json()
        return request_output[0]
    else:
        raise ValueError(f'Error en la obtención de datos: {response.status_code}')
        return None

def download_pdb(self, url):
    response = requests.get(url)
    if response.status_code == 200:
        with open(f'{self.dirpath}/alphafold_predicción_estructura_proteina.pdb', 'wb') as f:
            f.write(response.content)
        return True
    else:
        return False

def generar_proteina(self, structure_dict):
    url = structure_dict['pdbUrl']
    
    if gen_api.download_pdb(url):
        filepath = f'./gen_api/alphafold_predicción_estructura_proteina.pdb'
        pdb_file = open(filepath).read()
        view = py3Dmol.view(width=400, height=400)
        view.addModel(pdb_file, 'pdb')
        view.setStyle({'cartoon': {'color': 'spectrum'}})
        view.zoomTo()
        return view.show()

def cortar_adn(self, dna, cut_pos):
    """Corta el ADN en la posición especificada."""
    if cut_pos<0 or cut_pos>=len(dna):
        raise ValueError('La posicion especificada está fuera del ADN.')
    return dna[:cut_pos] + '|' + dna[cut_pos:]

def reparar_adn(self, dna, cut_pos, repair_type, nueva_secuencia=None):
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
