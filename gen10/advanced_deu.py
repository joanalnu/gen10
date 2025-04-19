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

def stelle_mutieren(sequence, pos, new_base):
    """
    Diese Funktion mutiert eine spezifische Stelle in einer DNA-Sequenz.
    """
    if pos < 0 or pos >= len(sequence):
        raise ValueError("Stelle außerhalb des Bereichs")
    if new_base not in ['A', 'T', 'C', 'G']:
        raise ValueError("Ungültige Base")
    
    mutated_sequence = list(sequence)
    mutated_sequence[pos] = new_base
    return ''.join(mutated_sequence)

def pcr_simulieren(sequence, fwd_primer, rev_primer):
    """
    Simulates a basic PCR reaction on a DNA template.
    """
    # Find the forward primer on the template
    fwd_start = sequence.find(fwd_primer)
    if fwd_start == -1:
        return ""

    # Find the reverse primer's reverse complement on the template
    rev_comp = komplementare(rev_primer)
    rev_start = sequence.find(rev_comp)
    if rev_start == -1:
        return ""

    # Make sure primers are in correct orientation and not overlapping
    if fwd_start >= rev_start:
        return ""

    # Calculate the end of the amplified region
    rev_end = rev_start + len(rev_primer)

    return sequence[fwd_start:rev_end]