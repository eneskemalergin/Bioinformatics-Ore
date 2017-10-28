# Author: Enes Kemal Ergin
# Date: 15/10/2017
# Title: Longest Increasing Subsequence

"""
Given: A positive integer n <= 10000 followed by a permutation π of length n.

Return: A longest increasing subsequence of π, followed by a longest
        decreasing subsequence of π.

Sample Dataset
5
5 1 4 2 3

Sample Output
1 2 3
5 4 2

"""

def main(data_path):
    with open(data_path, 'r') as f:
        n = int(f.readline())
        perm = [int(i) for i in f.readline().split(' ')]

    # Intialize the arrays with 0 and -1 by giving n
    q = [0] * n
    p = [-1] * n

    for op in ['>', '<']:
        for i in range(n):
            maxLen = 0
            for j in range(i):
                if op == '>':
                    x = perm[i] > perm[j]
                elif op == '<':
                    x = perm[i] < perm[j]

                if x == True :
                    if q[j] > maxLen:
                        maxLen = q[j]
                        p[i] = j

            q[i] = maxLen + 1
        idx = q.index(max(q))
        ls = []
        while(idx != -1):
            ls = [perm[idx]] + ls
            idx = p[idx]
        print(" ".join(map(str, ls)))

if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_lgis.txt'
    full_path  = './data/rosalind_lgis.txt'

    if run_mode in ['T', 't']:
        main(test_path)
    elif run_mode in ['F', 'f']:
        main(full_path)
    else:
        print("The input is not correct please try again!")
