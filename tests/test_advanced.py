import pytest
from gen10.advanced import reverse_complement, gc_content, melting_temperature, mutate_site, simulate_pcr

def test_reverse_complement():
    assert reverse_complement("ATGC") == "GCAT"
    assert reverse_complement("AATTCCGG") == "CCGGAATT"
    assert reverse_complement("G") == "C"
    assert reverse_complement("") == ""  # Edge case: empty string

def test_gc_content():
    assert pytest.approx(gc_content("GCGC"), 0.01) == 100.0
    assert pytest.approx(gc_content("ATAT"), 0.01) == 0.0
    assert pytest.approx(gc_content("ATGC"), 0.01) == 50.0
    with pytest.raises(ZeroDivisionError):
        gc_content("")  # Edge case: empty string causes division by zero

def test_melting_temperature():
    assert melting_temperature("ATGC") == 2*(2)+4*(2)  # 2*(A+T) + 4*(G+C)
    assert melting_temperature("AAAA") == 2*4
    assert melting_temperature("GGGG") == 4*4
    assert melting_temperature("ATATAT") == 2*6
    assert melting_temperature("") == 0  # Edge case: empty string

def test_mutate_site():
    # Normal mutation
    assert mutate_site("ATGC", 1, "G") == "AGGC"
    assert mutate_site("ATGC", 0, "T") == "TTGC"
    assert mutate_site("ATGC", 3, "A") == "ATGA"
    
    # Invalid position: negative
    with pytest.raises(ValueError):
        mutate_site("ATGC", -1, "A")
    
    # Invalid position: out of range
    with pytest.raises(ValueError):
        mutate_site("ATGC", 4, "A")
    
    # Invalid new_base
    with pytest.raises(ValueError):
        mutate_site("ATGC", 2, "X")
    
    # Edge case: empty sequence
    with pytest.raises(ValueError):
        mutate_site("", 0, "A")

def test_simulate_pcr_basic():
    sequence = "ATGCGTACGTTAGCTAGCTAGCTAGCGTACGATCG"
    fwd_primer = "ATGCGTACG"
    rev_primer = "CGATCGTAC"
    # The reverse complement of rev_primer is GTACGATCG
    expected_product = sequence[0:sequence.find("GTACGATCG") + len(rev_primer)]
    result = simulate_pcr(sequence, fwd_primer, rev_primer)
    assert result == expected_product

def test_simulate_pcr_primer_not_found():
    sequence = "ATGCGTACGTTAGCTAGCTAGCTAGCGTACGATCG"
    fwd_primer = "AAAAAAA"
    rev_primer = "TTTTTTT"
    result = simulate_pcr(sequence, fwd_primer, rev_primer)
    assert result == ""

def test_simulate_pcr_primers_wrong_order():
    sequence = "ATGCGTACGTTAGCTAGCTAGCTAGCGTACGATCG"
    fwd_primer = "CGATCGTAC"  # This primer is actually reverse primer sequence
    rev_primer = "ATGCGTACG"  # This primer is actually forward primer sequence
    result = simulate_pcr(sequence, fwd_primer, rev_primer)
    assert result == ""

def test_simulate_pcr_partial_match():
    sequence = "ATGCGTACGTTAGCTAGCTAGCTAGCGTACGATCG"
    fwd_primer = "ATGCGTACG"
    rev_primer = "CGATCGTAA"  # last base different, no exact match
    result = simulate_pcr(sequence, fwd_primer, rev_primer)
    assert result == ""
