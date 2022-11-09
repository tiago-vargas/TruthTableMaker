
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
	result = []

	binary_numbers = get_binary_numbers_as_strings(number_of_atoms)

	for string in binary_numbers:
		result.append(convert_binary_numbers_to_T_or_F(string))

	return result


def get_binary_numbers_as_strings(number_of_atoms: int) -> list[str]:
	counter = 0

	results = []

	for counter in range(2 ** number_of_atoms):
		results.append(f'{counter:0{number_of_atoms}b}')

	return results


def convert_binary_numbers_to_T_or_F(string: str) -> list[str]:
	result = []

	for character in string:
		if character == '0':
			result.append('F')
		elif character == '1':
			result.append('T')

	return result
