# Estimating the molecule mass from given sequence using the standart molecule masses

def estimateMolMass(seq, molType='protein'):
  """Calculate the molecular weight of a biological sequence assuming
  normal isotopic ratios and protonation/modification states
  """

  # Defining the standart weight of the molecules from DNA, RNA, Protein,
  residueMasses = {
      "DNA": {"G":329.21, "C":289.18, "A":323.21, "T":304.19},
      "RNA": {"G":345.21, "C":305.18, "A":329.21, "U":302.16},
      "protein": {"A": 71.07, "R":156.18, "N":114.08, "D":115.08,
      "C":103.10, "Q":128.13, "E":129.11, "G": 57.05,
      "H":137.14, "I":113.15, "L":113.15, "K":128.17,
      "M":131.19, "F":147.17, "P": 97.11, "S": 87.07,
      "T":101.10, "W":186.20, "Y":163.17, "V": 99.13}}

  massDict = residueMasses[molType]

  # Begin with mass of extra end atoms H + OH
  molMass = 18.02

  for letter in seq:
    molMass += massDict.get(letter, 0.0)
  return molMass


# Test Case 1
proteinSeq = 'IRTNGTHMQPLLKLMKFQKFLLELFTLQKRKPEKGYNLPIISLNQ'
proteinMass = estimateMolMass(proteinSeq) # We are testing the code on protein.
print "Protein Mass of given seq is: ", proteinMass

# Test Case 2
dnaSeq = 'ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTG'
dnaMass = estimateMolMass(dnaSeq, molType='DNA') # We are now testing the code on DNA
print "DNA Mass of given seq is: ", dnaMass
