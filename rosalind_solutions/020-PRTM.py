# Author: Enes Kemal Ergin
# Date: 13/10/2017
# Title: Calculating Protein Mass

"""
Given: A protein string P of length at most 1000 aa.

Return: The total weight of P Consult the monoisotopic mass table.

Sample Dataset
SKADYEK

Sample Output
821.392

"""

def main(data_path):
    aa_mass = { 'A':71.03711, 'C':103.00919, 'D':115.02694, 'E':129.04259, 'F':147.06841,
               'G':57.02146, 'H':137.05891, 'I':113.08406, 'K':128.09496, 'L':113.08406,
               'M':131.04049,'N':114.04293, 'P':97.05276,  'Q':128.05858, 'R':156.10111,
               'S':87.03203, 'T':101.04768, 'V':99.06841, 'W':186.07931, 'Y':163.06333 }
    with open(data_path, 'r') as input_data:
        prot_seq = input_data.read().strip()

    mass = sum([aa_mass[x] for x in prot_seq])
    return float("{:.3f}".format(mass))


if __name__ == '__main__':
    run_mode = input('Select a run mode: (T)est, (F)ull ')
    test_path = './data/test_prtm.txt'
    full_path  = './data/rosalind_prtm.txt'

    if run_mode in ['T', 't']:
        result  = main(test_path)
        assert result == 821.392 , "Result doesn't match with expected result!"
        print('The result is matching, Test is Passed!')

    elif run_mode in ['F', 'f']:
        print(main(full_path))

    else:
        print("The input is not correct please try again!")
