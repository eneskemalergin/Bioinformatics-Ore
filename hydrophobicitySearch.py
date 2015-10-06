
# A Unified Hydrophobicity Scale for Multi-Span Membrane Proteins represented
#   here as AAs called GES
GES_SCALE = {'F':-3.7,'M':-3.4,'I':-3.1,'L':-2.8,'V':-2.6,'C':-2.0,'W':-1.9,'A':-1.6,'T':-1.2,'G':-1.0,'S':-0.6,'P':0.2,'Y':0.7,'H':3.0,'Q':4.1,'N':4.8,'E':8.2,'K':8.8,'D':9.2,'R':12.3}

def HydrophobicitySearch(seq, scale, winSize=15):
    """Scan a protein sequence for Hydrophobic regions using
    the GES Hydrophobicity scale."""

    score = None
    scoreList = []

    for i in range(len(seq) - winSize):
        j = i + winSize

        if score is None:
            score = 0
            for k in range(i, j):
                score += scale[seq[k]]

        else:
            score += scale[seq[j-1]]
            score -= scale[seq[i-1]]

        scoreList.append(score)
    return scoreList

# Test Case 1

from matplotlib import pyplot
proteinSeq	=	'IRTNGTHMQPLLKLMKFQKFLLELFTLQKRKPEKGYNLPIISLNQ'
scores = HydrophobicitySearch(proteinSeq, GES_SCALE)
pyplot.plot(scores)
pyplot.show()
