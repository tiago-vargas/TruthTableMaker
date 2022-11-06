
from modules.formula import *


def make_truth_table(atoms: list[Atom]) -> list[list[str]]:
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
	elif number_of_atoms == 2:
		return [
			['T', 'T'],
			['T', 'F'],
			['F', 'T'],
			['F', 'F'],
		]
	else:
		return [
			['T', 'T', 'T'],
			['T', 'T', 'F'],
			['T', 'F', 'T'],
			['T', 'F', 'F'],

			['F', 'T', 'T'],
			['F', 'T', 'F'],
			['F', 'F', 'T'],
			['F', 'F', 'F'],
		]
