# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    fname="./data/test.fa"
    FastaParser_obj=FastaParser(fname)
    lines =[records for records in FastaParser_obj]
    
    assert lines[0][1]=='TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA'
    


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in. if a fastq file is
    read, the first item is None
    """
    fname="./data/test.fq"
    FastaParser_obj=FastaParser(fname)
    lines=[record for record in FastaParser_obj]
    assert lines[0][0]==None


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    fname="./data/test.fq"
    FastqParser_obj=FastqParser(fname)
    lines=[record for record in FastqParser_obj]
    assert lines[0][2]=="*540($=*,=.062565,2>'487')!:&&6=,6,*7>:&132&83*8(58&59>'8!;28<94,0*;*.94**:9+7\"94(>7='(!5\"2/!%\"4#32="

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    fname="./data/test.fa"
    FastqParser_obj=FastqParser(fname)
    lines=[record for record in FastqParser_obj]
    assert lines[0][0]==None