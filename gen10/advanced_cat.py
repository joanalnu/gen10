import gen10

def complementaria(dna):
    """
    Aquesta funció calcula la seqüència complementària d'una seqüència d'ADN donada.
    """
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_comp = ''.join(complement[base] for base in reversed(dna))
    return reverse_comp

def contingut_gc(dna):
    """
    Aquesta funció calcula el contingut de GC d'una seqüència d'ADN donada.
    """
    g_count = dna.count('G')
    c_count = dna.count('C')
    total_count = len(dna)
    gc_content = (g_count + c_count) / total_count * 100
    return gc_content

def temperatura_fusio(dna):
    """
    Calcula la temperatura de fusió (Tm) d'una seqüència curta d'ADN utilitzant la regla de Wallace.
    Assumeix que l'ADN té <=14 bases i consisteix només en A, T, G i C.
    """
    dna = dna.upper()
    a_count = dna.count('A')
    t_count = dna.count('T')
    g_count = dna.count('G')
    c_count = dna.count('C')

    tm = 2 * (a_count + t_count) + 4 * (g_count + c_count)
    return tm

def mutar_lloc(sequence, pos, new_base):
    """
    Aquesta funció muta un lloc específic en una seqüència d'ADN.
    """
    if pos < 0 or pos >= len(sequence):
        raise ValueError("Posició fora de rang")
    if new_base not in ['A', 'T', 'C', 'G']:
        raise ValueError("Base invàlida")
    
    mutated_sequence = list(sequence)
    mutated_sequence[pos] = new_base
    return ''.join(mutated_sequence)