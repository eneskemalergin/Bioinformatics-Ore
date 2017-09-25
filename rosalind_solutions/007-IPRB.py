# Author: Enes Kemal Ergin
# Date: 25/09/2017
# Title: Mendel's First Law

"""
Given: Three positive integers k, m, and n, representing a population
        containing k+m+n organisms: k individuals are homozygous dominant
        for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will
        produce an individual possessing a dominant allele (and thus displaying
         the dominant phenotype). Assume that any two organisms can mate.

Sample Dataset:
2 2 2

Sample Output:
0.78333
"""

def main(data_path):
    with open(data_path, 'r') as input_data:
        k,m,n = map(int, input_data.read().strip().split())

    # Get the probabilty of having dominant gene from k m n with corresponding successive probabilty
    prob = ((k*k - k) + 2*(k*m) + 2*(k*n) + (.75*(m*m - m)) + 2*(.5*m*n))/((k + m + n)*(k + m + n -1))
    return float("{:.5f}".format(prob))

if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_iprb.txt'
    full_path  = './data/rosalind_iprb.txt'

    if run_mode in ['T', 't']:
        result = main(test_path)
        assert result == 0.78333 , "Result doesn't match with expected result!"
        print('The result is matching, Test is Passed!')
    elif run_mode in ['F', 'f']:
        print(main(full_path))
    else:
        print("The input is not correct please try again!")
