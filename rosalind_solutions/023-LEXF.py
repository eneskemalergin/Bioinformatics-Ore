# Author: Enes Kemal Ergin
# Date: 15/10/2017
# Title: Enumerating k-mers Lexicographically

"""
Given: A collection of at most 10 symbols defining an ordered alphabet,
        and a positive integer n (n<=10).

Return: All strings of length n that can be formed from the alphabet,
        ordered lexicographically (use the standard order of symbols in
        the English alphabet).

Sample Dataset
A C G T
2

Sample Output
AA
AC
AG
AT
CA
CC
CG
CT
GA
GC
GG
GT
TA
TC
TG
TT

"""
from itertools import product

def main(data_path):
    with open(data_path, 'r') as f:
        seq_lst = f.readline().strip().split(" ")
        n = int(f.readline().strip())

    tmp_lst = []
    for perm in product(seq_lst, repeat=n):
        tmp_lst.append("".join(perm))

    return tmp_lst

if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_lexf.txt'
    full_path  = './data/rosalind_lexf.txt'

    if run_mode in ['T', 't']:
        result  = len(main(test_path))
        assert result == 16 , "Result doesn't match with expected result!"
        print('The result is matching, Test is Passed!')
    elif run_mode in ['F', 'f']:
        for i in main(full_path):
            print(i)
    else:
        print("The input is not correct please try again!")
