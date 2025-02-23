# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    sample_sequence="ATGCGTTAGCAGTACA"
    sample_transcribed=transcribe(sample_sequence)
    assert sample_transcribed=="AUGCGUUAGCAGUACA"

def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    sample_sequence="ATGCGTTAGCAGTACA"
    sample_transcribed=reverse_transcribe(sample_sequence)
    assert sample_transcribed=="UGUACUGCUAACGCAU"