# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    transcribed=""
    for char in seq:
        if char =="T":
            transcribed=transcribed+"U"
        else:
            transcribed=transcribed+char
    return transcribed
def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    n=len(seq)
    rev_trans=""
    for idx in range(-1,-n-1,-1):
        rev_trans=rev_trans+TRANSCRIPTION_MAPPING[seq[idx]]
    return rev_trans
        