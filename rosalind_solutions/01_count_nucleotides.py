# Author: Enes Kemal Ergin
# Date: 23/10/2017

"""
Problem:

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of
        times that the symbols 'A', 'C', 'G', and 'T' occur in s

Sample Dataset:
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

Sample Output:
20 12 17 21
"""

def count_nucleotides(s):
    s = s.upper()
    return s.count("A"), s.count("C"), s.count("G"), s.count("T")

def main(data):
    with open(data_path, "r") as seq:
        seq = seq.read().strip()
    output = count_nucleotides(seq)
    return output

def test(output):
    ref_output = "20 12 17 21"
    assert ref_output == output, "Result does not match the expected output!"

if __name__ == '__main__':
    # TODO: Add command line parser to get data and run mode.
    run_mode = 'real'
    if run_mode == 'test':
        data_path = "./data/test_dna.txt"
    else:
        data_path = "./data/rosalind_dna.txt"

    output = main(data_path)
    lst = []
    for i in output:
        lst.append(str(i))
    output = " ".join(lst)

    if run_mode == 'test':
        # print(output)
        test(output)
    else:
        print(output)
