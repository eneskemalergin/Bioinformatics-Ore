# Author: Enes Kemal Ergin
# Date: 25/09/2017
# Title: Consensus and Profile

"""
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp)
        in FASTA format.

Return: A consensus string and profile matrix for the collection.
        (If several possible consensus strings exist, then you may
        return any one of them.)

Sample Dataset
>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT

Sample Output
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
"""

def main(data_path):
    with open(data_path, 'r') as f:
        new_dict = {}
        for i in SeqIO.parse(f, 'fasta'):

if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_cons.txt'
    full_path  = './data/rosalind_cons.txt'

    if run_mode in ['T', 't']:
        result = main(test_path)
        assert result == '2 4 10' , \
                "Result doesn't match with expected result!"
        print('The result is matching, Test is Passed!')
    elif run_mode in ['F', 'f']:
        print(main(full_path))
    else:
        print("The input is not correct please try again!")
