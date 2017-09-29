# Author: Enes Kemal Ergin
# Date: 29/09/2017
# Title: Overlap Graphs


"""
Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.

Sample Dataset
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG

Sample Output
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
"""

from Bio import SeqIO

def main(data_path, k=3):
    seqFixes = {}
    for seq in SeqIO.parse(data_path, "fasta"):
        seqFixes[seq.id] = [str(seq.seq)[0:3], str(seq.seq)[len(seq.seq)-3:len(seq.seq)]]

    for key in seqFixes:
        for secKey in seqFixes:
            if key!=secKey and seqFixes[key][1]==seqFixes[secKey][0]:
                print(key + " " + secKey)


if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_grph.txt'
    full_path  = './data/rosalind_grph.txt'

    if run_mode in ['T', 't']:
        print(main(test_path))
        #assert result == '19', "The number found does't match with expected result!"
        #print('The result is matching, Test is Passed!')
    elif run_mode in ['F', 'f']:
        print(main(full_path))
    else:
        print("The input is not correct please try again!")
