import pandas as pd
import numpy as np
from Bio import SeqIO
import time 
import h5py

def vectorizeSequence(seq):
    # the order of the letters is not arbitrary.
    # Flip the matrix up-down and left-right for reverse compliment
    ltrdict = {'a':[1,0,0,0],'c':[0,1,0,0],'g':[0,0,1,0],'t':[0,0,0,1], 'n':[0,0,0,0]}
    return np.array([ltrdict[x] for x in seq])


starttime = time.time()
fasta_sequences = SeqIO.parse(open("hg38_new.fa"),'fasta')
with h5py.File('genomeEncoded.h5', 'w') as hf:
    for fasta in fasta_sequences:
        # get the fasta files.
        name, sequence = fasta.id, fasta.seq.tostring()
        # Write the chromosome name
        new_file.write(name)
        # one hot encode...
        data=vectorizeSequence(sequence.lower())
        print name + " is one hot encoded!"
        # write to hdf5 
        hf.create_dataset(name, data=data)
        print name + " is written to dataset"


endtime = time.time()       
print "Encoding is done in " + str(endtime)
