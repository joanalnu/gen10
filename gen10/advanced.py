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

def write_fasta(sequences, identifiers=None, filename="output.fasta"):
    """
    Write multiple sequences to a FASTA file, separated by an empty line.
    
    Parameters:
    sequences (str or list of str): A single sequence as a string or a list of sequences to write.
    identifiers (str or list of str, optional): A single identifier or a list of identifiers corresponding to each sequence. 
                                                 If None, identifiers will be generated using get_identifier.
    filename (str): Name of the output FASTA file.
    """
    # Convert a single sequence string to a list
    if isinstance(sequences, str):
        sequences = [sequences]
    
    # Convert a single identifier string to a list if identifiers are provided
    if identifiers is None:
        identifiers = [get_identifier(seq) for seq in sequences]
    elif isinstance(identifiers, str):
        identifiers = [identifiers]

    with open(filename, 'w') as fasta_file:
        for identifier, sequence in zip(identifiers, sequences):
            fasta_file.write(f">{identifier}\n")
            for i in range(0, len(sequence), 60):
                fasta_file.write(sequence[i:i+60] + "\n")
            fasta_file.write("\n")  # Add an empty line between sequences

def read_fasta(filename):
    """
    Read a FASTA file and return a list of sequences and their corresponding identifiers.
    
    Parameters:
    filename (str): The name of the FASTA file to read.
    
    Returns:
        identifiers (list): A list of identifiers.
        sequences (list): A list of sequences corresponding to the identifiers.
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

        if not lines:  # Check if the list of lines is empty
            raise IndexError("File is empty")
        
        identifiers = []
        sequences = []
        current_sequence = []

        for line in lines:
            line = line.strip()
            if line.startswith(">"):  # New identifier found
                if current_sequence:
                    sequences.append(''.join(current_sequence))
                    current_sequence = []  # Reset for the next sequence
                identifiers.append(line[1:]) # don't save the '>' character
            else:
                current_sequence.append(line)  # Add to the current sequence

        # After the loop, add the last sequence if it exists
        if current_sequence:
            sequences.append(''.join(current_sequence))

        if not identifiers or not sequences:  # Check if we have identifiers and sequences
            raise ValueError("FASTA file must contain at least one identifier and one sequence (check that identifiers start with '>')")

    return identifiers, sequences