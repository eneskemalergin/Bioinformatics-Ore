# Author: Enes Kemal Ergin
# Date: 25/09/2017
# Title: Counting Point Mutations


"""
Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance d_h(s,t).

Sample Dataset:
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

Sample Output:
7
"""

# Hamming Distance function created to help the script.
def hammingDistance(seq1,seq2):
    """Calculate the Hamming distance between two bit sequence strings"""
    if len(seq1) != len(seq2):
        raise ValueError("unequal strings")
    else:
        return sum(ch1 != ch2 for ch1, ch2 in zip(seq1, seq2))

def main(data_path):
    with open(data_path, 'r') as f:
        all_seq = f.readlines()
        seq1 = all_seq[0][:-1]
        if '\n' in all_seq[1]:
            seq2 = all_seq[1][:-1]
        else:
            seq2 = all_seq[1]
    return hammingDistance(seq1, seq2)

if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_hamm.txt'
    full_path  = './data/rosalind_hamm.txt'

    if run_mode in ['T', 't']:
        result = main(test_path)
        assert result == 7 , "Result doesn't match with expected result!"
        print('The result is matching, Test is Passed!')
    elif run_mode in ['F', 'f']:
        print(main(full_path))
    else:
        print("The input is not correct please try again!")
