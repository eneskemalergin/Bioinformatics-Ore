# Author: Enes Kemal Ergin
# Date: 06/10/2017
# Title: Inferring mRNA from Protein

"""
Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which
        the protein could have been translated, modulo 1,000,000.
        (Don't neglect the importance of the stop codon in protein translation.)

Sample Dataset
MA

Sample Output
12

"""

def main(data_path):
    # Use this dict for reference
    aa_dist = {
        'F':2,  'L':6,  'I':3,  'V':4,  'M':1,  'S':6,  'P':4,  'T':4,  'A':4,  'Y':2,
        'H':2,  'N':2,  'D':2,  'Q':2,  'K':2,  'E':2,  'C':2,  'R':6,  'G':4,  'W':1}

    with open(data_path, 'r') as input_data:
        aas = list(input_data.read().strip())

    count = 3
    for aa in aas:
        count = (count * (aa_dist[aa]) )
    return count % 1000000

if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_mrna.txt'
    full_path  = './data/rosalind_mrna.txt'

    if run_mode in ['T', 't']:
        result = main(test_path)
        assert result ==  12, "The result does't match with expected result!"
        print('The result is matching, Test is Passed!')
    elif run_mode in ['F', 'f']:
        result = main(full_path)
        print(result)
    else:
        print("The input is not correct please try again!")
