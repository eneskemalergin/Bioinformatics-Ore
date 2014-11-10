'''
Overlapping for counting occurance in strings.
'''



def count(sub, string):
    count = 0
    for i in xrange(len(string)):
        if string[i:].startswith(sub):
            count += 1
    return count


