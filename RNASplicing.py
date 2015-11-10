from itertools import takewhile
def fastaParse(file):
    f = open(file, 'r')
    introns = []
    for i in f.readlines():
        if i.startswith('>'):
            continue
        else:
            introns.append(i.replace('\n', ''))
    f.close()

    return introns

def main(stop = ('UAA', 'UAG', 'UGA')):
    introns = fastaParse("./data/RNASplicing_data.fa")
    baseSeq = introns.pop(0)
    for i in introns:
        baseSeq = baseSeq.replace(i, '')

    baseSeq = baseSeq.replace('T','U')

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

    start = baseSeq.find('AUG')
    new_seq = baseSeq[start:]
    codons = [new_seq[i:i+3] for i in range(0, len(new_seq),3)]

    coding_sequence  =  takewhile(lambda x: x not in stop and len(x) == 3,codons)
    protein_sequence = ''.join([aa_map[codon] for codon in coding_sequence])
    return protein_sequence

if __name__ == __main__():
    main()
