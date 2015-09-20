def weight(str):
    from Protein_dictionaries import ProteinWeightDict
    weight_dict = ProteinWeightDict()
    n = 0
    for i in str:
        n += weight_dict[i]
    return n

if __name__ == '__main__':
    f = open('data/protein_weights_data.txt')
    protein = f.read().strip()
    f.close()
    print weight(protein)
