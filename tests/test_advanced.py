import pytest
import gen10.advanced as adv
import tempfile
import os

def test_reverse_complement():
    assert adv.reverse_complement("ATGC") == "GCAT"
    assert adv.reverse_complement("AATTCCGG") == "CCGGAATT"
    assert adv.reverse_complement("G") == "C"
    assert adv.reverse_complement("") == ""  # Edge case: empty string

def test_gc_content():
    assert pytest.approx(adv.gc_content("GCGC"), 0.01) == 100.0
    assert pytest.approx(adv.gc_content("ATAT"), 0.01) == 0.0
    assert pytest.approx(adv.gc_content("ATGC"), 0.01) == 50.0
    with pytest.raises(ZeroDivisionError):
        adv.gc_content("")  # Edge case: empty string causes division by zero

def test_melting_temperature():
    assert adv.melting_temperature("ATGC") == 2*(2)+4*(2)  # 2*(A+T) + 4*(G+C)
    assert adv.melting_temperature("AAAA") == 2*4
    assert adv.melting_temperature("GGGG") == 4*4
    assert adv.melting_temperature("ATATAT") == 2*6
    assert adv.melting_temperature("") == 0  # Edge case: empty string

def test_mutate_site():
    # Normal mutation
    assert adv.mutate_site("ATGC", 1, "G") == "AGGC"
    assert adv.mutate_site("ATGC", 0, "T") == "TTGC"
    assert adv.mutate_site("ATGC", 3, "A") == "ATGA"
    
    # Invalid position: negative
    with pytest.raises(ValueError):
        adv.mutate_site("ATGC", -1, "A")
    
    # Invalid position: out of range
    with pytest.raises(ValueError):
        adv.mutate_site("ATGC", 4, "A")
    
    # Invalid new_base
    with pytest.raises(ValueError):
        adv.mutate_site("ATGC", 2, "X")
    
    # Edge case: empty sequence
    with pytest.raises(ValueError):
        adv.mutate_site("", 0, "A")

def test_simulate_pcr_basic():
    sequence = "ATGCGTACGTTAGCTAGCTAGCTAGCGTACGATCG"
    fwd_primer = "ATGCGTACG"
    rev_primer = "CGATCGTAC"
    # The reverse complement of rev_primer is GTACGATCG
    expected_product = sequence[0:sequence.find("GTACGATCG") + len(rev_primer)]
    result = adv.simulate_pcr(sequence, fwd_primer, rev_primer)
    assert result == expected_product

def test_simulate_pcr_primer_not_found():
    sequence = "ATGCGTACGTTAGCTAGCTAGCTAGCGTACGATCG"
    fwd_primer = "AAAAAAA"
    rev_primer = "TTTTTTT"
    result = adv.simulate_pcr(sequence, fwd_primer, rev_primer)
    assert result == ""

def test_simulate_pcr_primers_wrong_order():
    sequence = "ATGCGTACGTTAGCTAGCTAGCTAGCGTACGATCG"
    fwd_primer = "CGATCGTAC"  # This primer is actually reverse primer sequence
    rev_primer = "ATGCGTACG"  # This primer is actually forward primer sequence
    result = adv.simulate_pcr(sequence, fwd_primer, rev_primer)
    assert result == ""

def test_simulate_pcr_partial_match():
    sequence = "ATGCGTACGTTAGCTAGCTAGCTAGCGTACGATCG"
    fwd_primer = "ATGCGTACG"
    rev_primer = "CGATCGTAA"  # last base different, no exact match
    result = adv.simulate_pcr(sequence, fwd_primer, rev_primer)
    assert result == ""

# Tests for get_identifier
def test_get_identifier_dna():
    assert adv.get_identifier("ATCGATCG") == "DNA_sequence" # dna
    assert adv.get_identifier("AUGCAUGC") == "RNA_sequence" # rna
    assert adv.get_identifier("ACDEFGHIKLMNPQRSTVWY") == "Protein_sequence" # protein
    assert adv.get_identifier("XYZ123") == "Unknown_sequence" # wrong characters
    assert adv.get_identifier("ATCGU") == "Unknown_sequence" # mixed bases

# Tests for write_fasta
def test_write_fasta_creates_file_and_content():
    sequence = "ATCG" * 20  # 80 bases
    identifier = "DNA_sequence"
    with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
        filename = tmpfile.name
    try:
        adv.write_fasta(sequence, identifier=identifier, filename=filename)
        with open(filename, 'r') as f:
            content = f.read()
        # Check header line
        assert content.startswith(f">{identifier}\n")
        # Check sequence lines length (should be 60 bases in first line, 20 in second)
        lines = content.strip().split("\n")
        assert lines[0] == f">{identifier}"
        assert lines[1] == sequence[:60]
        assert lines[2] == sequence[60:]
    finally:
        os.remove(filename)

def test_write_fasta_default_identifier():
    sequence = "AUGC" * 15  # 60 bases, RNA
    with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
        filename = tmpfile.name
    try:
        # Call the write_fasta function with the identifier
        adv.write_fasta(sequence, filename=filename)
        
        with open(filename, 'r') as f:
            content = f.readlines()
        
        # The identifier should be RNA
        assert content[0] == f">RNA_sequence\n"  # Check the header line
        assert content[1].strip() == sequence[:60]  # Check the sequence line
    finally:
        os.remove(filename)
