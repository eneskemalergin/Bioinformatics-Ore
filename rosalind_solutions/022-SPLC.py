# Author: Enes Kemal Ergin
# Date: 14/10/2017
# Title: Locating Restriction Sites

"""
Given: A DNA string s (of length at most 1 kbp) and a collection of
       substrings of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons
        of s. (Note: Only one solution will exist for the dataset provided.)

Sample Dataset
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT

Sample Output
MVYIADKQHVASREAYGHMFKVCA
"""

from Bio.Seq import Seq
from Bio import SeqIO

def main(data_path):
    f = open(data_path, 'r')
    dna = ''
    introns = []
    count = 1
    for record in SeqIO.parse(f, "fasta"):
        if count == 1:
            dna = str(record.seq)
        else:
            introns.append(str(record.seq))
        count += 1
    f.close()
    for intron in introns:
        if intron in dna:
            dna = dna.replace(intron, "")

    return Seq(dna).translate(to_stop=True)

if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_splc.txt'
    full_path  = './data/rosalind_splc.txt'

    if run_mode in ['T', 't']:
        result  = main(test_path)
        assert result == 'MVYIADKQHVASREAYGHMFKVCA' , "Result doesn't match with expected result!"
        print('The result is matching, Test is Passed!')

    elif run_mode in ['F', 'f']:
        print(main(full_path))

    else:
        print("The input is not correct please try again!")
