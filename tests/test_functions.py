import pytest
import gen_api
from build.lib.gen_api import dna_schneiden


def test_dna2rna():
    assert gen_api.dna2rna("TACCACGTGGACTGAGGACTCCTCATT") == "AUGGUGCACCUGACUCCUGAGGAGUAA"

def test_compare():
    assert gen_api.compare("TACCACGTGGACTGAGGACTCCTCATT", "TACCACGTGGAGTGAGGACTCCTCATT") == ("Difference in 12 base/aminoacid")

def test_createmutation():
    dna = "TACCACGTGGACTGAGGACTCCTCATT"
    mutation = gen_api.createmutation(dna)
    assert dna != mutation  # Check mutation occurred

def test_dna2amino():
    dna = "TACCACGTGGACTGAGGACTCCTCATT"
    assert gen_api.dna2amino(dna) == " Met Val His Leu Thr Pro Glu Glu"

def test_rna2amino():
    rna = "AUGGUGCACCUGACUCCUGAGGAGUAA"
    assert gen_api.rna2amino(rna) == " Met Val His Leu Thr Pro Glu Glu"

def test_check_correct():
    dnas = ['TACCACGTGGACTGAGGACTCCTCATT', 'TACCACGTGGACTGAGGACTCCTCATC', 'TACCACGTGGACTGAGGACTCCTCACC']
    rnas = ['AUGGUGCACCUGACUCCUGAGGAGUAA', 'AUGGUGCACCUGACUCCUGAGGAGUAG', 'AUGGUGCACCUGACUCCUGAGGAGUGG']
    for dna, rna in zip(dnas, rnas):
        result = gen_api.check(dna)
        assert result == 'Valid DNA string'
        result = gen_api.check(rna)
        assert result == 'Valid RNA string'

def test_check_incorrect():
    size = ['TACCACGTGGACTGAGACTCCTCATT', ' Met Val His Leu Thr Pro Glu Glu']
    for seq in size:
        with pytest.raises(ValueError, match="String could not be divided into codons."):
            gen_api.check(seq)

# def test_check_base():
#     bases = ['TAACACGTGGACTGAGGACTCCTCATT', 'UGAGUGCACCUGACUCCUGAGGAGUAG', 'TACCACGTGGACTGAGGACTCCTCACU']
#     for seq in bases:
#         with pytest.raises(ValueError, match="Invalid string (starting/ending codons not found)"):
#             gen_api.check(seq)

def test_read_input_file():
    # Test reading from file
    content = gen_api.read_input('./tests/test.txt')
    assert content == ['TACCACGTGGACTGAGGACTCCTCATT', 'TACCACGTCTGAGGACTCCTCATT', 'TACGTGGACTGAGGACTCATT', 'TACCACGTCTGAGGAGGACTCCTCATT']

def test_read_input_string():
    # test direct string input
    content = gen_api.read_input("Just Plain String")
    assert content == "Just Plain String"

def test_read_input_invalid_file():
    # test invalid file path
    with pytest.raises(ValueError, match='Could not open file, please, check user guide.'):
        gen_api.read_input("nonexistent_file.txt")

def test_read_input_non_txt_file():
    with pytest.raises(ValueError, match="File type must be 'txt'"):
        gen_api.read_input("existent_not_txt_file.pdf")

def test_tosingle():
    amino = ' Met Val His Leu Thr Pro Glu Glu'
    assert gen_api.tosingle(amino) == "MVHLTPGG"