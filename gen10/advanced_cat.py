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

def simular_pcr(sequence, fwd_primer, rev_primer):
    """
    Simula una reacció de PCR bàsica en una plantilla d'ADN.
    """
    # Find the forward primer on the template
    fwd_start = sequence.find(fwd_primer)
    if fwd_start == -1:
        return ""

    # Find the reverse primer's reverse complement on the template
    rev_comp = complementaria(rev_primer)
    rev_start = sequence.find(rev_comp)
    if rev_start == -1:
        return ""

    # Make sure primers are in correct orientation and not overlapping
    if fwd_start >= rev_start:
        return ""

    # Calculate the end of the amplified region
    rev_end = rev_start + len(rev_primer)

    return sequence[fwd_start:rev_end]