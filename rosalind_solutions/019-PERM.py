# Author: Enes Kemal Ergin
# Date: 13/10/2017
# Title: Enumarating Gene Orders

"""
Given: A positive integer n <= 7
Return: The total number of permutations of length n,
        followed by a list of all such permutations (in any order).

Sample Dataset
3

Sample Output
6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1

"""
from itertools import permutations

def main(data_path):
    with open(data_path, 'r') as input_data:
        n = int(input_data.read())

    count = 0
    lst = []
    for i in permutations(list(range(1,n+1))):
        lst.append(" ".join(str(elem) for elem in i))
        count += 1

    print(count)
    for i in lst:
        print(i)

    return count


if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_perm.txt'
    full_path  = './data/rosalind_perm.txt'

    if run_mode in ['T', 't']:
        result  = main(test_path)
        assert result == 6 , "Result doesn't match with expected result!"
        print('The result is matching, Test is Passed!')

    elif run_mode in ['F', 'f']:
        print(main(full_path))

    else:
        print("The input is not correct please try again!")
