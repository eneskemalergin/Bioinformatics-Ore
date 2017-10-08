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
    codons = {"UUU":"F","UUC":"F","UUA":"L","UUG":"L","UCU":"S",\
              "UCC":"S","UCA":"S","UCG":"S","UAC":"Y","UAU":"Y","UAA":None,\
              "UAG":None,"UGU":"C","UGC":"C","UGA":None,"UGG":"W",\
              "CUU":"L","CUC":"L","CUA":"L","CUG":"L","CCU":"P","CCC":"P",\
              "CCA":"P","CCG":"P","CAU":"H","CAC":"H","CAA":"Q","CAG":"Q",\
              "CGU":"R","CGC":"R","CGA":"R","CGG":"R","AUU":"I","AUC":"I",\
              "AUA":"I","AUG":"M","ACU":"T","ACC":"T","ACA":"T","ACG":"T",\
              "AAU":"N","AAC":"N","AAA":"K","AAG":"K","AGU":"S","AGC":"S",\
              "AGA":"R","AGG":"R","GUU":"V","GUC":"V","GUA":"V","GUG":"V",\
              "GCU":"A","GCA":"A","GCC":"A","GCG":"A","GAC":"D","GAU":"D","GAA":"E","GAG":"E",\
              "GGU":"G","GGC":"G","GGA":"G","GGG":"G"}

    lst_seqs = []
    for sequence in SeqIO.parse(data_path, "fasta"):
            lst_seqs.append(str(sequence.seq))
    dna_seq = lst_seqs[0]

    rna_seq = "".join(['U' if x=='T' else x for x in dna_seq])
    lookup = {'A':'U', 'U':'A', 'G':'C', 'C':'G'}
    rev_rna_seq= ''.join([lookup[c] for c in rna_seq[::-1]])

    for sequence in [rna_seq, rev_rna_seq]:
        starts = [m.start() for m in re.finditer(start_codon, sequence)]
        for start in starts:
            fragment = sequence[start:]
            protein = ""
            trios = zip(*[iter(fragment)] * 3)
            for triplet in trios:
                codon = codons[''.join(triplet)]
                if not codon:
                    break
                else:
                    protein += codon
            print(protein)



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
