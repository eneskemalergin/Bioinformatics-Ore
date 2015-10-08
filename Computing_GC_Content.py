from Bio import SeqIO
fileObj = open("Computing_GC_Content.fasta", "rU")
new_list= {}
for i in SeqIO.parse(fileObj, 'fasta'):
    sequence = i.seq
    gcContent = (sequence.count('G') + sequence.count('C'))/float(len(sequence)) * 100
    new_list[i.id] = gcContent

max_sequence = max(new_list, key = new_list.get)

print max_sequence
print new_list[max_sequence]
