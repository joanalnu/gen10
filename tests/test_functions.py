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

def test_check():
    dnas = ['TACCACGTGGACTGAGGACTCCTCATT', 'TACCACGTGGACTGAGGACTCCTCATC', 'TACCACGTGGACTGAGGACTCCTCACC']
    rnas = ['AUGGUGCACCUGACUCCUGAGGAGUAA', 'AUGGUGCACCUGACUCCUGAGGAGUAG', 'AUGGUGCACCUGACUCCUGAGGAGUGG']
    for seq in dnas:
        result = gen_api.check(seq)
        assert result == 'Valid DNA string'

    for seq in rnas:
        result = gen_api.check(seq)
        assert result == 'Valid RNA string'

    lst = ['AUGGUGCACCGACUCCUGAGGAGUA', 'AUGGUGCACCUGACUCCUGAGGAGUAA', 'AUGGUGCACCUGACUCCUGAGGAGUAT']
    for seq in lst:
        result = gen_api.check(seq)
        assert result == 'Invalid string (startin/ending codons not found)'