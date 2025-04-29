# imports
import os
import csv
import numpy as np
import sys
from rdkit import Chem
from rdkit.Chem import rdReducedGraphs


# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# my model
def erg_desc(smiles_list):
    mols = [Chem.MolFromSmiles(smi) for smi in smiles_list]
    ergfps = [rdReducedGraphs.GetErGFingerprint(mol) for mol in mols]
    array_ergfps = [np.array(fp) for fp in ergfps]
    return array_ergfps


# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
outputs = erg_desc(smiles_list)

#check input and output have the same length
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len


# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["dim_{0}".format(str(i).zfill(3)) for i in range(len(outputs[0]))])  # header
    for o in outputs:
        writer.writerow(o)
