# Author: Enes Kemal Ergin
# Date: 29/09/2017
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
AC
"""
def main(data_path):
    pass

if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_lcsm.txt'
    full_path  = './data/rosalind_lcsm.txt'

    if run_mode in ['T', 't']:
        result = main(test_path)
        assert result == 'AC', "The pattern found does't match with expected result!"
        print('The result is matching, Test is Passed!')
    elif run_mode in ['F', 'f']:
        result = main(full_path)
        print(result)
    else:
        print("The input is not correct please try again!")
