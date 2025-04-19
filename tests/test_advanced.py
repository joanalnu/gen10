import pytest
from gen10.advanced import reverse_complement, gc_content, melting_temperature

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
