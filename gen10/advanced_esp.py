import gen10

def complementaria(dna):
    """
    Esta función calcula la secuencia complementaria de una secuencia de ADN dada.
    """
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_comp = ''.join(complement[base] for base in reversed(dna))
    return reverse_comp

def contenido_gc(dna):
    """
    Esta función calcula el contenido de GC de una secuencia de ADN dada.
    """
    g_count = dna.count('G')
    c_count = dna.count('C')
    total_count = len(dna)
    gc_content = (g_count + c_count) / total_count * 100
    return gc_content

def temperatura_fusion(dna):
    """
    Calcula la temperatura de fusión (Tm) de una secuencia corta de ADN utilizando la regla de Wallace.
    Assume que el ADN tiene <=14 bases y consiste solo en A, T, G y C.
    """
    dna = dna.upper()
    a_count = dna.count('A')
    t_count = dna.count('T')
    g_count = dna.count('G')
    c_count = dna.count('C')

    tm = 2 * (a_count + t_count) + 4 * (g_count + c_count)
    return tm

def mutar_sitio(sequence, pos, new_base):
    """
    Esta función muta un sitio específico en una secuencia de ADN.
    """
    if pos < 0 or pos >= len(sequence):
        raise ValueError("Posición fuera de rango")
    if new_base not in ['A', 'T', 'C', 'G']:
        raise ValueError("Base inválida")
    
    mutated_sequence = list(sequence)
    mutated_sequence[pos] = new_base
    return ''.join(mutated_sequence)

def simular_pcr(sequence, fwd_primer, rev_primer):
    """
    Simula una reacción de PCR básica en una plantilla de ADN.
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