import gen10

def reverse_complement(dna):
    """
    This function computes the reverse complement of a given DNA sequence.
    """
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_comp = ''.join(complement[base] for base in reversed(dna))
    return reverse_comp

def gc_content(dna):
    """
    This function calculates the GC content of a given DNA sequence.
    """
    g_count = dna.count('G')
    c_count = dna.count('C')
    total_count = len(dna)
    gc_content = (g_count + c_count) / total_count * 100
    return gc_content

def melting_temperature(dna):
    """
    Calculates the melting temperature (Tm) of a short DNA sequence using the Wallace rule.
    Assumes DNA is <=14 bases and consists only of A, T, G, and C.
    """
    dna = dna.upper()
    a_count = dna.count('A')
    t_count = dna.count('T')
    g_count = dna.count('G')
    c_count = dna.count('C')

    tm = 2 * (a_count + t_count) + 4 * (g_count + c_count)
    return tm

def mutate_site(sequence, pos, new_base):
    """
    This function mutates a specific site in a DNA sequence.
    """
    if pos < 0 or pos >= len(sequence):
        raise ValueError("Position out of range")
    if new_base not in ['A', 'T', 'C', 'G']:
        raise ValueError("Invalid base")
    
    mutated_sequence = list(sequence)
    mutated_sequence[pos] = new_base
    return ''.join(mutated_sequence)


def simulate_pcr(sequence, fwd_primer, rev_primer):
    """
    Simulates a basic PCR reaction on a DNA template.
    """
    # Find the forward primer on the template
    fwd_start = sequence.find(fwd_primer)
    if fwd_start == -1:
        return ""

    # Find the reverse primer's reverse complement on the template
    rev_comp = reverse_complement(rev_primer)
    rev_start = sequence.find(rev_comp)
    if rev_start == -1:
        return ""

    # Make sure primers are in correct orientation and not overlapping
    if fwd_start >= rev_start:
        return ""

    # Calculate the end of the amplified region
    rev_end = rev_start + len(rev_primer)

    return sequence[fwd_start:rev_end]

def get_identifier(sequence):
    """
    Generate a unique identifier for the sequence. Checks whether the sequence is DNA, RNA, or protein.
    """
    if all(base in 'ATCG' for base in sequence):  # DNA check
        return "DNA_sequence"
    elif all(base in 'AUGC' for base in sequence):  # RNA check
        return "RNA_sequence"
    elif all(base in 'ACDEFGHIKLMNPQRSTVWY' for base in sequence):  # Protein check
        return "Protein_sequence"
    else:
        return "Unknown_sequence"

def write_fasta(sequence, identifier=None, filename="output.fasta"):
    """
    Write a sequence to a FASTA file.
    """
    if identifier is None:
        identifier = get_identifier(sequence)
    
    with open(filename, 'w') as fasta_file:
        fasta_file.write(f">{identifier}\n")
        
        for i in range(0, len(sequence), 60):
            fasta_file.write(sequence[i:i+60] + "\n")

def read_fasta(filename):
    """
    Read a FASTA file and return the sequence and identifier.
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

        if not lines:  # Check if the list of lines is empty
            raise IndexError("File is empty")
        if len(lines) < 2:  # Must have at least one identifier and one sequence
            raise ValueError("FASTA file must contain at least an identifier and a sequence")
        if not lines[0].startswith(">"):
            raise ValueError("FASTA identifier must start with '>'")
        
        identifier = lines[0].strip()[1:]  # Remove '>' character
        sequence = ''.join(line.strip() for line in lines[1:])  # Join remaining lines for sequence
        
    return identifier, sequence