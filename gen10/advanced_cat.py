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

def identificador(sequence):
    """
    Identificar el typo de seqüència (ADN, ARN o proteïna) en funció de la seqüència donada.
    """
    if all(base in 'ATCG' for base in sequence):  # DNA check
        return "DNA_sequence"
    elif all(base in 'AUGC' for base in sequence):  # RNA check
        return "RNA_sequence"
    elif all(base in 'ACDEFGHIKLMNPQRSTVWY' for base in sequence):  # Protein check
        return "Protein_sequence"
    else:
        return "Unknown_sequence"

def escriure_fasta(sequence, identifier=None, filename="output.fasta"):
    """
    Escriure una seqüència en format FASTA.
    """
    if identifier is None:
        identifier = identificador(sequence)
    
    with open(filename, 'w') as fasta_file:
        fasta_file.write(f">{identifier}\n")
        
        for i in range(0, len(sequence), 60):
            fasta_file.write(sequence[i:i+60] + "\n")

def llegir_fasta(filename):
    """
    Llegeix un fitxer FASTA i retorna l'identificador i la seqüència.
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

        if not lines:  # Check if the list of lines is empty
            raise IndexError("Arxiu buit")
        if len(lines) < 2:  # Must have at least one identifier and one sequence
            raise ValueError("El fitxer FASTA ha de contenir almenys un identificador i una seqüència")
        if not lines[0].startswith(">"):
            raise ValueError("L'identificador FASTA ha de començar amb '>'")
        
        identifier = lines[0].strip()[1:]  # Remove '>' character
        sequence = ''.join(line.strip() for line in lines[1:])  # Join remaining lines for sequence
        
    return identifier, sequence