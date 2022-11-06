
from modules.formula import *


def make_truth_table(atoms: list[Atom], formulas: list[Formula]) -> list[list[str]]:
	table = []

	header = [atom.name for atom in atoms]

	table.append(header)

	possibilities = get_possibilities(len(atoms))

	for possibility in possibilities:
		table.append(possibility)

	return table


def get_possibilities(number_of_atoms: int) -> list[list[str]]:
	if number_of_atoms == 1:
		return [
			['T'],
			['F'],
		]
	else:
		return [
			['T', 'T'],
			['T', 'F'],
			['F', 'T'],
			['F', 'F'],
		]
