
'''
# Using basic control statements
ar = [i for i in raw_input()]
def function(list):
    
    countA = 0
    countT = 0
    countG = 0
    countC = 0
    for i in list:
        if list[i] == 'A':
            countA += 1
        elif list[i] == 'T':
            countT += 1
        elif list[i] == 'G':
            countG += 1
        elif list[i] == 'C':
            countC += 1
        else:
            print "Sorry it is not a genome! Find real one!"
    print countA, countC, countG, countT
'''
# More advance version of counting nucleic acids in genome.
ar = list(raw_input())
ardic = dict((i,ar.count(i)) for i in ar)
print ardic

