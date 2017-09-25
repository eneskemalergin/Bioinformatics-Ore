# Author: Enes Kemal Ergin
# Date: 25/09/2017
# Title: Finding a Motif in DNA

"""
Given: Two DNA strings ss and t (each of length at most 1 kbp).

Return: All locations of t as a substring of ss.

Sample Dataset
GATATATGCATATACTT
ATAT

Sample Output
2 4 10
"""

def main(data_path):
    # Read the sequence(1st line) and motif(2nd line) and store them in  variables
    with open(data_path) as f:
        all_seq = f.readlines()
        seq = all_seq[0][:-1]
        if '\n' in all_seq[1]:
            motif = all_seq[1][:-1]
        else:
            motif = all_seq[1]

    # Get the length of seq and motif and store in variable
    seq_len = len(seq)
    motif_len = len(motif)
    new_list = []
    i = 0
    # Iterate and find the positions.
    while i <= (seq_len - motif_len):
        if seq[i:i+motif_len] == motif:
            new_list.append(i+1)
        i += 1

    # Return the string which contains the position indexes
    return " ".join(str(item) for item in new_list)

if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_subs.txt'
    full_path  = './data/rosalind_subs.txt'

    if run_mode in ['T', 't']:
        result = main(test_path)
        assert result == '2 4 10' , "Result doesn't match with expected result!"
        print('The result is matching, Test is Passed!')
    elif run_mode in ['F', 'f']:
        print(main(full_path))
    else:
        print("The input is not correct please try again!")
