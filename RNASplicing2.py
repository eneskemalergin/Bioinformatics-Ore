# Here is an BioPython Solution
# Not my solution but it is really cool
# That's why I put it here...

from Bio.Seq import Seq
from Bio import SeqIO

instream = SeqIO.parse("./RNASplicing_data.fa","fasta")
target = str(instream.next().seq)

for intron in instream:
    target = target.replace(str(intron.seq),"")

print Seq(target).translate()[:-1]
