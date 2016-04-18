''' This script allows you to check for exact matching with reverse complements'''

def reverseComplement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t

def naive(p,t):
    occurences = []
    for i in range(len(t) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if not t[i+j] == p[j]:
                match = False
                break # If not match not sense to contine matching
        
        if match:
            occurences.append(i)
    return occurences

def naive_with_rc(p,t):
    full_occurences = []
    # full_occurences.append(naive(p, t))
    # full_occurences.append(naive(reverseComplement(p),t))
    for i in naive(p,t):
        full_occurences.append(i)
    for j in naive(reverseComplement(p), t):
        full_occurences.append(j)
    return list(set(full_occurences))


