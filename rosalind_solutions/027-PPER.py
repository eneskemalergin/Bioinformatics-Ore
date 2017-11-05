# Author: Enes Kemal Ergin
# Date: 04/11/2017
# Title: Partial Permutations

"""
Given: Positive integers nn and kk such that 100 >= n > 0 and 10 >= k > 0

Return: The total number of partial permutations P(n,k), modulo 1,000,000.

Sample Dataset
21 7

Sample Output
51200
"""
from math import factorial

def main(data_path):
    n, k = map(int,open(data_path).read().strip().split())
    return int((factorial(n) / factorial(n - k)) % 1000000)

if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_pper.txt'
    full_path  = './data/rosalind_pper.txt'

    if run_mode in ['T', 't']:
        result = main(test_path)
        assert result == 51200 , "Result doesn't match with expected result!"
        print('The result is matching, Test is Passed!')
    elif run_mode in ['F', 'f']:
        print(main(full_path))
    else:
        print("The input is not correct please try again!")
