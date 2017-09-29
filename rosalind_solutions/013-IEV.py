# Author: Enes Kemal Ergin
# Date: 29/09/2017
# Title: Calculating Expected Offspring


"""
Given: Six nonnegative integers, each of which does not exceed 20,000.
The integers correspond to the number of couples in a population possessing
each genotype pairing for a given factor. In order, the six given integers
 represent the number of couples having the following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa

Return: The expected number of offspring displaying the dominant phenotype
in the next generation, under the assumption that every couple has exactly
two offspring.

Sample Dataset
1 0 0 1 0 1

Sample Output
3.5
"""

import numpy as np

def main(data_path):
    with open(data_path, 'r') as input_data:
        genotypes = [int(x) for x in input_data.read().split()]

    prob_lst = np.array([2, 2, 2, 1.5, 1, 0])
    return (np.array(genotypes) * prob_lst).sum()

if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_iev.txt'
    full_path  = './data/rosalind_iev.txt'

    if run_mode in ['T', 't']:
        result = main(test_path)
        assert result == 3.5 , "The number found does't match with expected result!"
        print('The result is matching, Test is Passed!')
    elif run_mode in ['F', 'f']:
        print(main(full_path))
    else:
        print("The input is not correct please try again!")
