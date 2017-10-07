# Author: Enes Kemal Ergin
# Date: 07/10/2017
# Title: Open Reading Frames

"""
Given: A DNA string ss of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated
        from ORFs of s. Strings can be returned in any order.

Sample Dataset
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

Sample Output
MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE

"""


import re
from Bio import SeqIO

def main(data_path):
    lst_seqs = []
    for sequence in SeqIO.parse(data_path, "fasta"):
            lst_seqs.append(str(sequence.seq))
    dna_seq = lst_seqs[0]

    rna_seq = "".join(['U' if x=='T' else x for x in dna_seq])
    rev_rna_seq = rna_seq[::-1]

    for sequence in [rna_seq, rev_rna_seq]:
        starts = [m.start() for m in re.finditer('AUG', sequence)]
        for start in starts:
            fragment = sequence[start:]
            protein = ""
            trios = zip(*[iter(fragment)] * 3)
            for triplet in trios:
                codon = codons[''.join(triplet)]
                if not codon:
                    yield protein
                    break
                protein += codon



if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_orf.txt'
    full_path  = './data/rosalind_orf.txt'

    if run_mode in ['T', 't']:
        result  = main(test_path)
        assert result == '' , "Result doesn't match with expected result!"
        print('The result is matching, Test is Passed!')

    elif run_mode in ['F', 'f']:
        print(main(full_path))

    else:
        print("The input is not correct please try again!")
