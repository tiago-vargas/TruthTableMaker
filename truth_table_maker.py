
from modules.formula import *

def make_truth_table(atoms: list[Atom], formulas: list[Formula]):
	atom_name = atoms[0].name

	return [
		[atom_name],
		['T'],
		['F'],
	]
