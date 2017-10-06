# Author: Enes Kemal Ergin
# Date: 05/10/2017
# Title: Independent Alleles

"""
Given: Two positive integers k (k<=7) and N (N<=2k). In this problem,
        we begin with Tom, who in the 0th generation has genotype Aa Bb.
        Tom has two children in the 1st generation, each of whom has two
        children, and so on. Each organism always mates with an organism
        having genotype Aa Bb.

Return: The probability that at least N Aa Bb organisms will belong to the k-th
        generation of Tom's family tree (don't count the Aa Bb mates at each
        level). Assume that Mendel's second law holds for the factors.

Sample Dataset
2 1

Sample Output
0.684

"""
from scipy.special import binom


def P(n, k):
    return (binom(2 ** k, n) * 0.25 ** n * 0.75 ** (2 ** k - n))

def main(data_path):
    with open(data_path, 'r') as input_data:
        k, n = map(int, input_data.read().strip().split())


    result = 1 - sum([P(_, k) for _ in range(n)])
    return (float("{:.3f}".format(result)))

if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_lia.txt'
    full_path  = './data/rosalind_lia.txt'

    if run_mode in ['T', 't']:
        result = main(test_path)
        assert result ==  0.684, "The result does't match with expected result!"
        print('The result is matching, Test is Passed!')
    elif run_mode in ['F', 'f']:
        result = main(full_path)
        print(result)
    else:
        print("The input is not correct please try again!")
