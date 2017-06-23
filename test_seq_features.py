import pytest
import seq_features

def test_n_neg_for_single_E_or_D():
    """Perform unit tests on n_neg."""

    assert seq_features.n_neg('E') == 1
    assert seq_features.n_neg('D') == 1

def test_n_neg_for_empty_sequence():
    assert seq_features.n_neg('') == 0

def test_n_neg_for_longer_sequences():
    assert seq_features.n_neg('ACKLWTTAE') == 1
    assert seq_features.n_neg('DDDDEEEE') == 8

def test_n_neg_for_lower_case_sequences():
    assert seq_features.n_neg('acklwttae') == 1

def test_n_neg_for_invalid_amino_acid():
    with pytest.raises(RuntimeError) as excinfo:
        seq_features.n_neg('Z')
    excinfo.match("Z is not a valid amino acid")

    with pytest.raises(RuntimeError) as excinfo:
        seq_features.n_neg('O')
    excinfo.match("O is not a valid amino acid")
