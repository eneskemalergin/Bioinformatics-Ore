# Author: Enes Kemal Ergin
# Date: 23/09/2017
# Title: Counting DNA Nucleotides

"""
Problem:

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of
        times that the symbols 'A', 'C', 'G', and 'T' occur in s

Sample Dataset:
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

Sample Output:
20 12 17 21
"""

def count_nucleotides(s):
    s = s.upper()
    return s.count("A"), s.count("C"), s.count("G"), s.count("T")

def main(data_path):
    with open(data_path, "r") as seq:
        seq = seq.read().strip()
    output = count_nucleotides(seq)
    return ' '.join([str(e) for e in output])

if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_dna.txt'
    full_path  = './data/rosalind_dna.txt'

    if run_mode in ['T', 't']:
        result  = main(test_path)
        assert result == '20 12 17 21' , "Result doesn't match with expected result!"
        print('The result is matching, Test is Passed!')
    elif run_mode in ['F', 'f']:
        print(main(full_path))
    else:
        print("The input is not correct please try again!")
