import ovelap
def pick_maximal_overlap(reads, k):
    """ Return a pair of reads from the list with a
        maximal suffix/prefix overlap >= k.  Returns
        overlap length 0 if there are no such overlaps."""
    reada, readb = None, None
    best_olen = 0

    # Make index
    index = defaultdict(set)
    for read in reads:
        for i in range(len(read) - k + 1):
            index[read[i:i+k]].add(read)

    for r in reads:
        for o in index[r[-k:]]:
            if r != o:
                olen = overlap(r, o, k)
                if olen > best_olen:
                    reada, readb = r, o
                    best_olen = olen

    return reada, readb, best_olen
