
# Reference table for protein synthesis
aa_map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

from itertools import takewhile

def RNA_to_Protein(seq , aa_map, stop = ('UAA', 'UAG', 'UGA')):
    """Returns the Protein version of the RNA after Synthesis"""
    """It gets seq as a string, Reference table to locate the amino acid names
     and stop codons specified"""

    start = seq.find('AUG') # Finds the start in the RNA sequence
    new_seq = seq[start:] # Now we use this sequence for protein synthesis
    codons = [new_seq[i:i+3] for i in range(0, len(new_seq),3)]

    # Debugging Tools
    # print len(codons)
    # print new_seq
    # print codons

    # Take all codons until first stop codon
    coding_sequence  =  takewhile(lambda x: x not in stop and len(x) == 3,
                                    codons)

     # Translate and join into string
    protein_sequence = ''.join([aa_map[codon] for codon in coding_sequence])

    # This line assumes there is always stop codon in the sequence
    return "{0}_".format(protein_sequence)


if __name__ == '__main__':
    f = open("/data/RNA_to_Protein_data.txt")
    rna = f.readline()
    print RNA_to_Protein(rna, aa_map)
