#!/usr/bin/env python
# Exact script from @jschendel

'''A ROSALIND bioinformatics script to create RNA and DNA to Protein dictionary.'''

import os


def ProteinDictDNA():
    '''Returns a dictionary that translates DNA to Protein.'''
    # Get the raw codon table.
    with open(os.path.join(os.path.dirname(__file__), 'data/codon_table_dna.txt')) as input_data:
        dna_to_protein = [line.strip().split() for line in input_data.readlines()]

    # Convert to dictionary.
    dna_dict = {}
    for translation in dna_to_protein:
        dna_dict[translation[0]] = translation[1]

    return dna_dict


def ProteinDictRNA():
    '''Returns a dictionary that translates RNA to Protein.'''
    # Get the raw codon table.
    with open(os.path.join(os.path.dirname(__file__), 'data/codon_table_rna.txt')) as input_data:
        rna_to_protein = [line.strip().split() for line in input_data.readlines()]

    # Convert to dictionary.
    rna_dict = {}
    for translation in rna_to_protein:
        rna_dict[translation[0]] = translation[1]

    return rna_dict


def ProteinWeightDict():
    '''Returns a dictionary that translates Protein to Monoisotopic Mass.'''
    # Read the protein masses and add them to a dictionary.
    with open(os.path.join(os.path.dirname(__file__), 'data/protein_mass_table.txt')) as input_data:
        protein_weight_dict = {line.strip().split()[0]:float(line.strip().split()[1]) for line in input_data.readlines()}

    return protein_weight_dict
