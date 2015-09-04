# Type one the fastest and most elegant algorithm for counting point mutations.
# Using Hamming Distance algorithm to solve this problem.

# Enes Kemal Ergin

def hammingDistance(seq1,seq2):
    """Calculate the Hamming distance between two bit sequence strings"""
    if len(seq1) != len(seq2):
        raise ValueError("unequal strings")
    else:
    	return sum(ch1 != ch2 for ch1, ch2 in zip(seq1, seq2))


fil = open("data/counting_point_mutations_data.txt", "r")
allseq = fil.readlines()
seq1 = allseq[0][:-1] # extracting the new line character at the end
seq2 = allseq[1]
fil.close()
print hammingDistance(seq1, seq2)