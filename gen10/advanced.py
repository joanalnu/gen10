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







# conversion tools
def fasta_reader():
    """
    This function reads a FASTA file and returns the sequences.
    """
    """
    Let's analyze each of your provided sequences to determine if any qualify as FASTA-formatted:

### **1. "TACCACGTGGACTGAGGACTCCTCATT"**  
- **Type**: Likely DNA sequence (T/A/C/G nucleotides).  
- **FASTA compliance**: **No** — missing the required `>` header line.  
- **How to fix**: Add a header (e.g., `>DNA_sequence1`).

---

### **2. "AUGGUGCACCUGACUCCUGAGGAGUAA"**  
- **Type**: Likely RNA sequence (A/U/C/G nucleotides).  
- **FASTA compliance**: **No** — missing `>` header.  
- **How to fix**: Add a header (e.g., `>RNA_sequence1`).

---

### **3. "Met Val His Leu Thr Pro Glu Glu"**  
- **Type**: Amino acid sequence (3-letter codes, space-separated).  
- **FASTA compliance**: **No** — FASTA uses **single-letter codes** (e.g., `MVHLTPEE`), and requires a header.  
- **How to fix**:  
  - Convert to single-letter codes.  
  - Add a header (e.g., `>Protein_sequence1`).

---

### **4. "MAGELVSFAVNKLWDLLSHEYTLFQGVEDQVAELKSDLNLLKSFLKDADAKKHTSALVRYCVEEIKDIVYDAEDVLETFVQKEKLGTTSGIRKHIKRLTCIVPDRREIALYIGHVSKRITRVIRDMQSFGVQQMIVDDYMHPLRNREREIRRTFPKDNESGFVALEENVKKLVGYFVEEDNYQVVSITGMGGLGKTTLARQVFNHDMVTKKFDKLAWVSVSQDFTLKNVWQNILGDLKPKEEETKEEEKKILEMTEYTLQRELYQLLEMSKSLIVLDDIWKKEDWEVIKPIFPPTKGWKLLLTSRNESIVAPTNTKYFNFKPECLKTDDSWKLFQRIAFPINDASEFEIDEEMEKLGEKMIEHCGGLPLAIKVLGGMLAEKYTSHDWRRLSENIGSHLVGGRTNFNDDNNNSCNYVLSLSFEELPSYLKHCFLYLAHFPEDYEIKVENLSYYWAAEEIFQPRHYDGEIIRDVGDVYIEELVRRNMVISERDVKTSRFETCHLHDMMREVCLLKAKEENFLQITSNPPSTANFQSTVTSRRLVYQYPTTLHVEKDINNPKLRSLVVVTLGSWNMAGSSFTRLELLRVLDLVQAKLKGGKLASCIGKLIHLRYLSLEYAEVTHIPYSLGNLKLLIYLNLHISLSSRSNFVPNVLMGMQELRYLALPSLIERKTKLELSNLVKLETLENFSTKNSSLEDLRGMVRLRTLTIELIEETSLETLAASIGGLKYLEKLEIDDLGSKMRTKEAGIVFDFVHLKRLRLELYMPRLSKEQHFPSHLTTLYLQHCRLEEDPMPILEKLLQLKELELGHKSFSGKKMVCSSCGFPQLQKLSISGLKEWEDWKVEESSMPLLLTLNIFDCRKLKQLPDEHLPSHLTAISLKKCGLEDPIPTLERLVHLKELSLSELCGRIMVCTGGGFPQLHKLDLSELDGLEEWIVEDGSMPRLHTLEIRRCLKLKKLPNGFPQLQNLHLTEVEEWEEGMIVKQGSMPLLHTLYIWHCPKLPGEQHFPSHLTTVFLLGMYVEEDPMRILEKLLHLKNVSLFQSFSGKRMVCSGGGFPQLQKLSIREIEWEEWIVEQGSMPLLHTLYIGVCPNLKELPDGLRFIYSLKNLIVSKRWKKRLSEGGEDYYKVQHIPSVEFDD"**  
- **Type**: Amino acid sequence (single-letter codes).  
- **FASTA compliance**: **No** — missing `>` header.  
- **How to fix**: Add a header (e.g., `>Large_protein_sequence`).

---

### **FASTA Conversion Examples**
- **DNA**:  
  ```
  >DNA_sequence1  
  TACCACGTGGACTGAGGACTCCTCATT
  ```
- **RNA**:  
  ```
  >RNA_sequence1  
  AUGGUGCACCUGACUCCUGAGGAGUAA
  ```
- **Protein (3-letter to single-letter conversion)**:  
  ```
  >Protein_sequence1  
  MVHLTPEE
  ```
- **Large protein**:  
  ```
  >Large_protein_sequence  
  MAGELVSFAVNKLWDLLSHEYTLFQGVEDQVAELKSDLNLLKSFLKDADAKKHTSALVRYCVEEIKDIVYDAEDVLETFVQKEKLGTTSGIRKHIKRLTCIVPDRREIALYIGHVSKRITRVIRDMQSFGVQQMIVDDYMHPLRNREREIRRTFPKDNESGFVALEENVKKLVGYFVEEDNYQVVSITGMGGLGKTTLARQVFNHDMVTKKFDKLAWVSVSQDFTLKNVWQNILGDLKPKEEETKEEEKKILEMTEYTLQRELYQLLEMSKSLIVLDDIWKKEDWEVIKPIFPPTKGWKLLLTSRNESIVAPTNTKYFNFKPECLKTDDSWKLFQRIAFPINDASEFEIDEEMEKLGEKMIEHCGGLPLAIKVLGGMLAEKYTSHDWRRLSENIGSHLVGGRTNFNDDNNNSCNYVLSLSFEELPSYLKHCFLYLAHFPEDYEIKVENLSYYWAAEEIFQPRHYDGEIIRDVGDVYIEELVRRNMVISERDVKTSRFETCHLHDMMREVCLLKAKEENFLQITSNPPSTANFQSTVTSRRLVYQYPTTLHVEKDINNPKLRSLVVVTLGSWNMAGSSFTRLELLRVLDLVQAKLKGGKLASCIGKLIHLRYLSLEYAEVTHIPYSLGNLKLLIYLNLHISLSSRSNFVPNVLMGMQELRYLALPSLIERKTKLELSNLVKLETLENFSTKNSSLEDLRGMVRLRTLTIELIEETSLETLAASIGGLKYLEKLEIDDLGSKMRTKEAGIVFDFVHLKRLRLELYMPRLSKEQHFPSHLTTLYLQHCRLEEDPMPILEKLLQLKELELGHKSFSGKKMVCSSCGFPQLQKLSISGLKEWEDWKVEESSMPLLLTLNIFDCRKLKQLPDEHLPSHLTAISLKKCGLEDPIPTLERLVHLKELSLSELCGRIMVCTGGGFPQLHKLDLSELDGLEEWIVEDGSMPRLHTLEIRRCLKLKKLPNGFPQLQNLHLTEVEEWEEGMIVKQGSMPLLHTLYIWHCPKLPGEQHFPSHLTTVFLLGMYVEEDPMRILEKLLHLKNVSLFQSFSGKRMVCSGGGFPQLQKLSIREIEWEEWIVEQGSMPLLHTLYIGVCPNLKELPDGLRFIYSLKNLIVSKRWKKRLSEGGEDYYKVQHIPSVEFDD
  ```

**Key Takeaway**: None of your examples are currently in FASTA format, but they can easily be converted by adding a header line starting with `>`. For amino acid sequences, ensure single-letter codes are used.

---
Answer from Perplexity: https://www.perplexity.ai/search/what-is-fasta-formatt-QP__WX96Q6eXbV2uMPYhyw?utm_source=copy_output"""

def fasta_writer():
    """
    This function writes sequences to a FASTA file.
    """