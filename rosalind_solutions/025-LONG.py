# Author: Enes Kemal Ergin
# Date: 04/11/2017
# Title: Genome Assembly as Shortest Superstring

"""
Given: At most 50 DNA strings of equal length, not exceeding 1 kbp, in
       FASTA format (which represent reads deriving from the same strand of a
       single linear chromosome).

The dataset is guaranteed to satisfy the following condition: there exists a
unique way to reconstruct the entire chromosome from these reads by gluing
together pairs of reads that overlap by more than half their length.

Return: A shortest superstring containing all the given strings
        (thus corresponding to a reconstructed chromosome).

Sample Dataset
>Rosalind_56
ATTAGACCTG
>Rosalind_57
CCTGCCGGAA
>Rosalind_58
AGACCTGCCG
>Rosalind_59
GCCGGAATAC

Sample Output
ATTAGACCTGCCGGAATAC
"""

from Bio import SeqIO

def match_seq(seq, seq_list):
    half = int(len(seq)/2)
    for i in range(len(seq)-1, half, -1):
        overlap = seq[len(seq)-i:]
        for seq2 in seq_list:
            if seq2 != seq:
                if seq2[:i] == overlap:
                    return seq[:len(seq)-i] + seq2

def shortest_contig(seq_list):
    while len(seq_list) > 1:
        new_list = []
        for seq in seq_list:
            match = match_seq(seq, seq_list)
            if match != None:
                new_list.append(match)
        seq_list = new_list
    return seq_list[0]

def main(data_path):
    seq_lst = []
    for record in SeqIO.parse(data_path, 'fasta'):
        seq_lst.append(str(record.seq))

    return shortest_contig(seq_lst)

if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_long.txt'
    full_path  = './data/rosalind_long.txt'

    if run_mode in ['T', 't']:
        result = main(test_path)
        assert result == 'ATTAGACCTGCCGGAATAC' , "Result doesn't match with expected result!"
        print('The result is matching, Test is Passed!')
    elif run_mode in ['F', 'f']:
        print(main(full_path))
    else:
        print("The input is not correct please try again!")
