# Author: Enes Kemal Ergin
# Date: 05/10/2017
# Title: Finding a Shared Motif


"""
Given: A collection of k (k <= 100) DNA strings of length at most 1 kbp
        each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions
        exist, you may return any single solution.)

Sample Dataset
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA

Sample Output
AC (or) TA
"""

from Bio import SeqIO

def longest_motif_match(seqs):
    # Returns the first longest match
    seqs = sorted(seqs) # sort the list
    short_seq = seqs[0] # store the shortest
    other_seqs = seqs[1:] # exclude shortest from the list

    p = '' # initialize string to keep the motif
    for i in range(len(short_seq)):
        for j in range(len(short_seq) , i + len(p), -1):
            s1 = short_seq[i:j] # Subset the string
            matched = True
            for s2 in other_seqs:
                if s1 not in s2:
                    matched = False
                    break
            if matched:
                p = s1
                break
    return p

def main(data_path):
    lst_seqs = []
    for sequence in SeqIO.parse(data_path, "fasta"):
        lst_seqs.append(str(sequence.seq))

    return longest_motif_match(lst_seqs)


if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_lcsm.txt'
    full_path  = './data/rosalind_lcsm.txt'

    if run_mode in ['T', 't']:
        result = main(test_path)
        assert result == 'TA', "The pattern found does't match with expected result!"
        print('The result is matching, Test is Passed!')
    elif run_mode in ['F', 'f']:
        result = main(full_path)
        print(result)
    else:
        print("The input is not correct please try again!")
