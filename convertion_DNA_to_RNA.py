ar = list(raw_input())
'''

def DNAtoRNA(ar):
    u = 'U'
    t = 'T'
    for i in ar:
        if ar[i] == t: # I don't know why it is not working...
            ar[i] = u
    return "".join(ar)
'''


RNAar = ['U' if x=='T' else x for x in ar]
print "".join(RNAar)

