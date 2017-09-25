# Author: Enes Kemal Ergin
# Date: 23/09/2017
# Title: Transcribing DNA into RNA

"""
Given: A DNA string having length at most 1000 nt.

Return: The transcribed RNA string of t.

Sample Dataset:
GATGGAACTTGACTACGTAAATT

Sample Output:
GAUGGAACUUGACUACGUAAAUU
"""

def main(data_path):
    with open(data_path, "r") as seq:
        seq = seq.read().strip()
    RNAar = ['U' if x=='T' else x for x in seq]
    return ("".join(RNAar))

if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_rna.txt'
    full_path  = './data/rosalind_rna.txt'

    if run_mode in ['T', 't']:
        result  = main(test_path)
        assert result == 'GAUGGAACUUGACUACGUAAAUU' , "Result doesn't match with expected result!"
        print('The result is matching, Test is Passed!')

    elif run_mode in ['F', 'f']:
        print(main(full_path))

    else:
        print("The input is not correct please try again!")
