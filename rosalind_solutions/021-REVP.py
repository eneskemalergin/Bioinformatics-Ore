# Author: Enes Kemal Ergin
# Date: 13/10/2017
# Title: Locating Restriction Sites

"""
Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the
        string having length between 4 and 12. You may return these
        pairs in any order.

Sample Dataset
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT

Sample Output
4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4

"""
from Bio import SeqIO
from Bio.Seq import Seq

def main(data_path):
    f = open(data_path, 'r')
    seq = SeqIO.read(f, "fasta")
    f.close()
    for start in range(len(seq)):
        for end in range(len(seq), start, -1):
            if end - start < 4:
                break
            else:
                if str(seq.seq[start:end]) == str(seq.seq[start:end].reverse_complement()):
                    if len(seq.seq[start:end]) >= 4 and len(seq.seq[start:end]) <= 12:
                        print(" ".join(map(str, [start+1, len(seq.seq[start:end])])))

if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_revp.txt'
    full_path  = './data/rosalind_revp.txt'

    if run_mode in ['T', 't']:
        main(test_path)
        # result  = main(test_path)
        # assert result == 821.392 , "Result doesn't match with expected result!"
        # print('The result is matching, Test is Passed!')

    elif run_mode in ['F', 'f']:
        main(full_path)

    else:
        print("The input is not correct please try again!")
