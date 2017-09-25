# Author: Enes Kemal Ergin
# Date: 23/09/2017
# Title: Translating RNA into Protein

"""
Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.

Sample Dataset
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

Sample Output
MAMAPRTEINSTRING
"""
from Bio.Seq import Seq
import time

def main_biopython(data_path):
    rna = Seq(open(data_path, "rU").readline().strip())
    prot = rna.translate(to_stop=True)
    return str(prot)

def main_own(data_path):
    codons_index = {"UUU":"F","UUC":"F","UUA":"L","UUG":"L","UCU":"S",\
            "UCC":"S","UCA":"S","UCG":"S","UAC":"Y","UAU":"Y","UAA":"STOP",\
            "UAG":"STOP","UGU":"C","UGC":"C","UGA":"STOP","UGG":"W",\
            "CUU":"L","CUC":"L","CUA":"L","CUG":"L","CCU":"P","CCC":"P",\
            "CCA":"P","CCG":"P","CAU":"H","CAC":"H","CAA":"Q","CAG":"Q",\
            "CGU":"R","CGC":"R","CGA":"R","CGG":"R","AUU":"I","AUC":"I",\
            "AUA":"I","AUG":"M","ACU":"T","ACC":"T","ACA":"T","ACG":"T",\
            "AAU":"N","AAC":"N","AAA":"K","AAG":"K","AGU":"S","AGC":"S",\
            "AGA":"R","AGG":"R","GUU":"V","GUC":"V","GUA":"V","GUG":"V",\
            "GCU":"A","GCA":"A","GCC":"A","GCG":"A","GAC":"D","GAU":"D","GAA":"E","GAG":"E",\
            "GGU":"G","GGC":"G","GGA":"G","GGG":"G"}

    with open(data_path, 'r') as seq:
        new_seq = seq.read().strip()

    result = ''
    for i in range(0,len(new_seq),3):
        letter = codons_index[new_seq[i:i+3]]
        if letter == "STOP":
            break
        else:
            result += letter # String concatenation
    return result


# This is just for measuring the time elapsed that i will be using to compare
#  2 algorithms
def measure_time(function_name, iteration_number=10000):
    start = time.time()
    for _ in range(iteration_number):
        function_name(test_path)

    end = time.time()
    exec_time = (end - start)/60
    if exec_time >= 1.0:
        print("Execution time is:", format(exec_time, '.3f'), "minutes")
    elif exec_time < 1.0:
        print("Execution time is:", format(exec_time, '.10f'), "seconds")

if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_prot.txt'
    full_path  = './data/rosalind_prot.txt'

    # print("Measuring the biopython implementation:")
    # measure_time(main_biopython)
    # print("Measuring the my own implementation:")
    # measure_time(main_own)

    if run_mode in ['T', 't']:
        result = main_own(test_path)
        assert result == 'MAMAPRTEINSTRING' , "Result doesn't match with expected result!"
        print('The result is matching, Test is Passed!')

    elif run_mode in ['F', 'f']:
        print(main_own(full_path))

    else:
        print("The input is not correct please try again!")
