class RNA():
    """Class representing RNA as a string sequence.
    Usage:
    from rna import RNA
    #define objects
    rna1 = RNA("AUCGAUAUAUUCGGUAGCU")
    rna1.is_rna()
    rna1.uppercase()
    rna1.lowecase()
    rna1.revtranscribe()
    rna1.reverse()
    rna1.complementary()
    rna1.reversecomplement()
    rna1.gc()
    rna1.codons()

    """
    basecomplement = {'A': 'U', 'C': 'G', 'U': 'A', 'G': 'C',
                      'a': 'u', 'c': 'g', 'u': 'a', 'g': 'c'}

    def __init__(self, s):
        """Create RNA instance initialized to string s."""
        self.seq = s

    def __str__(self):
        """Supports the string representation"""
        return str(self.seq)

    __repr__ = __str__

    def is_rna(self):
        """Checks if given string sequence is RNA"""
        is_RNA = True
        if is_RNA == True:
            for char in self.seq:
                if char.lower() == 'a' or char.lower() == 'u' or char.lower() == 'c' or char.lower() == 'g'or char == '\n':
                   is_RNA = True
                else:
                    is_RNA = False
                    print 'is RNA? ', is_RNA
                    break
        return "is RNA?, it's "+ str(is_RNA)
    def lowercase(self):
        """Convert RNA sequence into lowercase letters"""
        return self.seq.lower()

    def uppercase(self):
        """Convert RNA sequence into uppercase letters"""
        return self.seq.upper()

    def revtranscribe(self):
        """Returns the base DNA which transcribed from"""
        return self.seq.upper().replace("U", "T")

    def reverse(self):
        """Returns the RNA string in reverse order"""
        letters = list(self.seq)
        letters.reverse()
        return ''.join(letters).upper()

    def complementary(self):
        """Return the complementary RNA string."""
        letters = list(self.seq)
        letters = [self.basecomplement[base] for base in letters]
        return ''.join(letters)

    def reversecomplement(self):
        """Return the reverse complement of the RNA string."""
        letters = list(self.seq)
        letters.reverse()
        letters = [self.basecomplement[base] for base in letters]
        return ''.join(letters)

    def gc(self):
        """Return the percentage of dna composed of G+C."""
        s = self.seq
        gc = s.upper().count('G') + s.upper().count('C')
        return gc * 100.0 / len(s)

    def codons(self):
        """Return list of codons for the dna string."""
        """Needs improvement"""
        s = self.seq
        end = len(s) - (len(s) % 3) - 1
        codons = [s[i:i+3] for i in range(0, end, 3)]
        return codons
