import gen10

def komplementare(dna):
    """
    Diese Funktion berechnet das komplementäre Gegenstück (Reverse Complement) einer gegebenen DNA-Sequenz.
    """
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_comp = ''.join(complement[base] for base in reversed(dna))
    return reverse_comp

def gc_gehalt(dna):
    """
    Diese Funktion berechnet den GC-Gehalt einer gegebenen DNA-Sequenz.
    """
    g_count = dna.count('G')
    c_count = dna.count('C')
    total_count = len(dna)
    gc_content = (g_count + c_count) / total_count * 100
    return gc_content

def schmelz_temperatur(dna):
    """
    Berechnet die Schmelztemperatur (Tm) einer kurzen DNA-Sequenz unter Verwendung der Wallace-Regel.
    Geht davon aus, dass die DNA <=14 Basen hat und nur aus A, T, G und C besteht.
    """
    dna = dna.upper()
    a_count = dna.count('A')
    t_count = dna.count('T')
    g_count = dna.count('G')
    c_count = dna.count('C')

    tm = 2 * (a_count + t_count) + 4 * (g_count + c_count)
    return tm