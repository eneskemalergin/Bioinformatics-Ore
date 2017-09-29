# Author: Enes Kemal Ergin
# Date: 29/09/2017
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

from Bio import SeqIO
import numpy as np

def main(data_path):
    with open(data_path, 'r') as f:
        new_lst = []
        len_lst = []
        for i in SeqIO.parse(f, 'fasta'):
            sequence = i.seq.upper()
            len_lst.append(len(sequence))
            new_lst.append(list(sequence))

    assert np.unique(np.array(len_lst)).shape[0] == 1, "All the length should be equal to contiue!"

    nested_list = []
    for nuc in range(len_lst[0]):
        tmp_lst = np.array([0 ,0 ,0 ,0])
        for i in new_lst:
            if i[nuc] == 'A'  :
                tmp_lst[0] += 1
            elif i[nuc] == 'C':
                tmp_lst[1] += 1
            elif i[nuc] == 'G':
                tmp_lst[2] += 1
            elif i[nuc] == 'T':
                tmp_lst[3] += 1
        nested_list.append(tmp_lst)
    nested_list = np.array(nested_list).T

    idx_lst = np.argmax(nested_list, axis=0)

    nuc_lst = ['A', 'C', 'G', 'T']
    new_lst = []
    for i in idx_lst:
        new_lst.append(nuc_lst[i])

    res_string = ''.join(new_lst)
    print(res_string)
    for i in range(len(nested_list)):
        nuc = nuc_lst[i]
        count_str = " ".join((str(elem) for elem in list(nested_list[i])))
        print(nuc + ': ' + count_str)

    return res_string # Just for testing purposes


if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_cons.txt'
    full_path  = './data/rosalind_cons.txt'

    if run_mode in ['T', 't']:
        result = main(test_path)
        # assert result == 'ATGCAACT' , \
                # "Result doesn't match with expected result!"
        # print('The result is matching, Test is Passed!')

    elif run_mode in ['F', 'f']:
        main(full_path)

    else:
        print("The input is not correct please try again!")
