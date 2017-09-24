# Author: Enes Kemal Ergin
# Date: 23/10/2017
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
    data_path = './data/rosalind_rna.txt'
    print(main(data_path))

    # Uncomment when testing
    # data_path2 = './data/test_rna.txt'
    # assert main(data_path2) == "GAUGGAACUUGACUACGUAAAUU", "Wrong expected result!"
    # print('passed the test!')
