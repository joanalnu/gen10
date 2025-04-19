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