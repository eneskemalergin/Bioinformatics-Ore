# Get the data and strip the \n (newline) and store the lines in list
lines = [line.rstrip('\n') for line in open("data/finding_motif_dna.txt")]
# Debugging
# print lines

seq1 = lines[0] # Store the first line into a variable / Full seq
seq1_len = len(lines[0]) # Get the length of that variable
seq2 = lines[1] # Store the second line into a variable / Target seq
seq2_len = len(lines[1]) # Get the length of that variable

# Debugging
# print seq1
# print seq2

# Initialize indexer
i = 0

#Initialize a new list
new_list = []
while i <= (seq1_len - seq2_len): # Loops until we come to the last len(seq1)-len(seq2)
    if seq1[i:i+seq2_len] == seq2: # if the motif from ith to i+len(seq2) is equal to seq2
        new_list.append(i+1) # add the index to new list.
        # Gets the index from 1 to len(seq1)

    i += 1

# Get the list of numbers and create one list with spaces 
print " ".join(str(item) for item in new_list)
