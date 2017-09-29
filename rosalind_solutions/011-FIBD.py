# Author: Enes Kemal Ergin
# Date: 29/09/2017
# Title: Mortal Fibonacci Rabbits

"""
Given: Positive integers n <= 100 and m <= 20.

Return: The total number of pairs of rabbits that will remain
after the nth month if all rabbits live for m months.

Sample Dataset
6 3

Sample Output
4
"""

## Function is taken by the rosalind forum
#  since it's the most efficient implement
# Author of the Function: @abeliangrape
def fib(n,k=1):
  ages = [1] + [0]*(k-1)
  for i in range(n-1):
    ages = [sum(ages[1:])] + ages[:-1]
  return sum(ages)

def main(data_path):
    with open(data_path, 'r') as input_data:
        n, m = map(int, input_data.read().strip().split())

    return fib(n,m)


if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_fibd.txt'
    full_path  = './data/rosalind_fibd.txt'

    if run_mode in ['T', 't']:
        result = main(test_path)
        assert result == int('4'), "The number found does't match with expected result!"
        print('The result is matching, Test is Passed!')
    elif run_mode in ['F', 'f']:
        result = main(full_path)
        print(result)
    else:
        print("The input is not correct please try again!")
