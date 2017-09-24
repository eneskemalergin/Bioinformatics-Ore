def parse_fasta(path, no_id=True):
    ''' Read in a Fasta file. If no_id is set to False, return a dictonary of
        sequences with associated headers; otherwise return a list of
        sequences only.
    '''
    ids = []
    seqs = []

    with open(path, 'r') as f:
        for line in f.readlines():
            if line.startswith('>'):
                ids.append(line[1:].strip())
                seqs.append('')
            else:
                seqs[-1] += line.strip()

    if no_id == True:
        if len(seqs) > 1:
            return seqs
        else:
            return seqs[0]
    else:
        return dict(zip(ids, seqs))
