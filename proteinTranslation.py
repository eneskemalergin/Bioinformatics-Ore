# Protein Translation using AA names with 3 letter showing...
STANDARD_GENETIC_CODE = {
'UUU':'Phe', 'UUC':'Phe', 'UCU':'Ser', 'UCC':'Ser',
'UAU':'Tyr', 'UAC':'Tyr', 'UGU':'Cys', 'UGC':'Cys',
'UUA':'Leu', 'UCA':'Ser', 'UAA':None, 'UGA':None,
'UUG':'Leu', 'UCG':'Ser', 'UAG':None, 'UGG':'Trp',
'CUU':'Leu', 'CUC':'Leu', 'CCU':'Pro', 'CCC':'Pro',
'CAU':'His', 'CAC':'His', 'CGU':'Arg', 'CGC':'Arg',
'CUA':'Leu', 'CUG':'Leu', 'CCA':'Pro', 'CCG':'Pro',
'CAA':'Gln', 'CAG':'Gln', 'CGA':'Arg', 'CGG':'Arg',
'AUU':'Ile', 'AUC':'Ile', 'ACU':'Thr', 'ACC':'Thr',
'AAU':'Asn', 'AAC':'Asn', 'AGU':'Ser', 'AGC':'Ser',
'AUA':'Ile', 'ACA':'Thr', 'AAA':'Lys', 'AGA':'Arg',
'AUG':'Met', 'ACG':'Thr', 'AAG':'Lys', 'AGG':'Arg',
'GUU':'Val', 'GUC':'Val', 'GCU':'Ala', 'GCC':'Ala',
'GAU':'Asp', 'GAC':'Asp', 'GGU':'Gly', 'GGC':'Gly',
'GUA':'Val', 'GUG':'Val', 'GCA':'Ala', 'GCG':'Ala',
'GAA':'Glu', 'GAG':'Glu', 'GGA':'Gly', 'GGG':'Gly'}


def proteinTranslation(seq, geneticCode):
    """ This function translates a nucleic acid sequence into a
    protein sequence, until the end or until it comes across
    a stop codon """
    seq = seq.replace('T','U') # Make sure we have RNA sequence
    proteinSeq = [] # Initalize an empty list to store protein seq
    i = 0
    while i+2 < len(seq):
        codon = seq[i:i+3]
        aminoAcid = geneticCode[codon]
        if aminoAcid is None: # Found stop codon
            break
        proteinSeq.append(aminoAcid)
        i += 3
    return proteinSeq

# Test Case 1
dnaSeq = 'ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTG'
protein3LetterSeq = proteinTranslation(dnaSeq, STANDARD_GENETIC_CODE)
print protein3LetterSeq  # Print the Result
