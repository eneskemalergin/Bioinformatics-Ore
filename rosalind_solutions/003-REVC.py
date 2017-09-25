# Author: Enes Kemal Ergin
# Date: 25/10/2017
# Title: Complementing a Strand of DNA

"""
Given: A DNA string ss of length at most 1000 bp.

Return: The reverse complement s^c of s.

Sample Dataset:
AAAACCCGGT

Sample Output:
ACCGGGTTTT
"""

def main(data_path):
    # Dictionary
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    # Open data and read the sequence.
    # Then get the reverse string.
    with open(data_path, 'r') as seq:
        new_seq = seq.read().strip()[::-1]

    bases = list(new_seq)
    new_bases = []
    for i in bases:
        new_bases.append(complement.get(i))
    return ''.join(new_bases)




if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_revc.txt'
    full_path  = './data/rosalind_revc.txt'

    if run_mode in ['T', 't']:
        result = main(test_path)
        assert result == 'ACCGGGTTTT', "Found Complementary DNA does't match with expected result!"
        print('The result is matching, Test is Passed!')
    elif run_mode in ['F', 'f']:
        result = main(full_path)
        print(result)
    else:
        print("The input is not correct please try again!")
