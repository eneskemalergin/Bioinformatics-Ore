# Author: Enes Kemal Ergin
# Date: 04/11/2017
# Title: Perfect Matchings and RNA Secondary Structures

"""
Given: An RNA string s of length at most 80 bp having the same number of
       occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

Return: The total possible number of perfect matchings of basepair
        edges in the bonding graph of s.

Sample Dataset
>Rosalind_23
AGCUAGUCAU

Sample Output
12
"""

from Bio import SeqIO
from math import factorial

def main(data_path):
    for rec in SeqIO.parse(data_path, 'fasta'):
        rna_seq = str(rec.seq)
    return factorial(rna_seq.count("A")) * factorial(rna_seq.count("C"))


if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_pmch.txt'
    full_path  = './data/rosalind_pmch.txt'

    if run_mode in ['T', 't']:
        result = main(test_path)
        assert result == 12 , "Result doesn't match with expected result!"
        print('The result is matching, Test is Passed!')
    elif run_mode in ['F', 'f']:
        print(main(full_path))
    else:
        print("The input is not correct please try again!")
