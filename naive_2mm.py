def naive_2mm(p,t):
    '''This Function allows up to 2 missmatches in the exact matching'''
    occurences = []
    mm_counter = 0
    for i in range(len(t) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if not t[i+j] == p[j]:
                mm_counter += 1
                if mm_counter > 2:
                    match = False
                    mm_counter = 0 # make it 0 again.
                    break 
                    
        if match:
            occurences.append(i)
    return occurences
