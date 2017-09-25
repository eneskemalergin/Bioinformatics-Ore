# Author: Enes Kemal Ergin
# Date: 25/09/2017
# Title: Rabbits and Recurrence Relations

"""
Given: Positive integers n<=40 and k<=5.

Return: The total number of rabbit pairs that will be present after nn months,
        if we begin with 1 pair and in each generation, every pair of
        reproduction-age rabbits produces a litter of kk rabbit pairs
        (instead of only 1 pair).

Sample Dataset:
5 3

Sample Output:
19
"""

def fib_rabbits(n,k):
    '''Returns the number of rabbits present after n
        generations with litters of k pairs.'''
    rabbits = [0,1] # Initialize the rabits
    # Really efficient way.
    for i in range(n-1):
        rabbits[i % 2] = rabbits[(i-1) % 2] + k*rabbits[i % 2]

    return rabbits[n % 2]


def main(data_path):
    with open(data_path, 'r') as input_data:
        n, k = map(int, input_data.read().strip().split())

    return str(fib_rabbits(n,k))

if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_fib.txt'
    full_path  = './data/rosalind_fib.txt'

    if run_mode in ['T', 't']:
        result = main(test_path)
        assert result == '19', "The number found does't match with expected result!"
        print('The result is matching, Test is Passed!')
    elif run_mode in ['F', 'f']:
        result = main(full_path)
        print(result)
    else:
        print("The input is not correct please try again!")
