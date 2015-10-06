profile	=	{	'A':[	61,	16, 352, 3, 354, 268, 360, 222, 155, 56, 83, 82, 82, 68, 77],
          		'C':[145, 46,	0, 10, 0, 0, 3, 2, 44, 135, 147, 127, 118, 107, 101],
          		'G':[152,	18,	2, 2, 5, 0,	10,	44, 157, 150, 128, 128, 128, 139, 140],
          		'T':[	31, 309, 35, 374, 30, 121, 6,121,	33,	48,	31,	52,	61,	75,	71]}

def matchDnaProfile(seq, profile):
    """	Find	the	best-matching	position	and	score	when	comparing	a	DNA
		sequence	with	a	DNA	sequence	profile	"""

    bestScore = 0 # Initializing
    bestPosition = None # Initializing

    width = len(profile['A'])

    for i in range(len(seq)-width):
        score = 0
        for j in range(width):
            letter = seq[i+j]
            score += profile[letter][j]

        if score > bestScore:
            bestScore = score
            bestPosition = i

    return bestScore, bestPosition


# Test Case 1
dnaSeq = 'ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTG'
score,	position	=	matchDnaProfile(dnaSeq,	profile)
print(score,	position,	dnaSeq[position:position+15])
