# Author: Enes Kemal Ergin
# Date: 25/09/2017
# Title: Computing GC Content

"""
Given : At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content,
        followed by the GC-content of that string. Rosalind allows for a
        default error of 0.001 in all decimal answers unless otherwise stated;
        please see the note on absolute error below.

Sample Dataset:
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT


Sample Output:
Rosalind_0808
60.919540
"""

# Import Biopython for Fasta Parser
from Bio import SeqIO


def main(data_path):
    with open(data_path, 'r') as f:
        new_dict = {}
        for i in SeqIO.parse(f, 'fasta'):
            sequence = i.seq
            gcContent = (sequence.count('G') + sequence.count('C'))/float(len(sequence)) * 100
            new_dict[i.id] = gcContent
    res_id = max(new_dict, key = new_dict.get)
    res_score =  "{:.6f}".format((new_dict[res_id])) # Special formating to be used

    # Return biggest gc count id and score
    return res_id, res_score

if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_gc.txt'
    full_path  = './data/rosalind_gc.txt'

    if run_mode in ['T', 't']:
        ID, score  = main(test_path)
        print(ID)
        print(score)
        assert ID == 'Rosalind_0808' and score == "60.919540" , \
            "Resulting pair (id and score) does't match with expected result!"

        print('The result is matching, Test is Passed!')
    elif run_mode in ['F', 'f']:
        ID, score = main(full_path)
        print(ID)
        print(score)
    else:
        print("The input is not correct please try again!")
