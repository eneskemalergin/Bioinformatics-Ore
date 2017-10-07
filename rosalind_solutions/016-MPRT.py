# Author: Enes Kemal Ergin
# Date: 06/10/2017
# Title: Finding a Protein Motif

"""
Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif,
        output its given access ID followed by a list of locations
        in the protein string where the motif can be found.

Sample Dataset
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST

Sample Output
B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614

"""

import re              # regular expressions for motif sequence
import urllib.request  # library to look for urls of uniprot

def connect2uniprot(accid):
    uri = 'http://www.uniprot.org/uniprot/{}.fasta'.format(accid)
    response = urllib.request.urlopen(uri)
    fasta = response.read().decode("utf-8", "ignore")
    prot_seq = "".join(fasta.split('\n')[1:])
    return prot_seq

def main(data_path):
    # Define motif to look for in each protein sequence.
    # N-glycosylation motif
    # N{any but P}[S or T]{any but P}
    motif = re.compile('(?=N[^P][ST][^P])')

    with open(data_path, 'r') as f:
        accids = f.readlines()
        accids = [i.strip('\n') for i in accids]

    results = {}
    for i in accids:
        index = []
        name = i
        seq = connect2uniprot(name)
        for j in range(len(seq)):
            if motif.match(seq[j:j+4]):
                index.append(str(j+1))

        if len(index) != 0:
            print(name)
            print(' '.join(index))

    return " "

if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_mprt.txt'
    full_path  = './data/rosalind_mprt.txt'

    if run_mode in ['T', 't']:
        print(main(test_path))
        # assert result ==  "85 118 142 306 395", "The result does't match with expected result!"
        # print('The result is matching, Test is Passed!')
    elif run_mode in ['F', 'f']:
        print(main(full_path))
        # print(result)
    else:
        print("The input is not correct please try again!")
