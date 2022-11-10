
from modules.formula import *


def make_truth_table(atoms: list[Atom], formulas: list[Formula] = []) -> list[list[str]]:
	table = []

	header = [atom.name for atom in atoms]
	formulas_header = [formula.__str__() for formula in formulas]

	table.append(header + formulas_header)

	atoms_valorations = get_atoms_valoration_possibilities(len(atoms))

	formula_valoration = []
	for atoms_valoration in atoms_valorations:
		if len(formulas) > 0:
			formula_valoration = get_formula_valoration(formulas[0], atoms_valoration)
		table.append(atoms_valoration + formula_valoration)

	return table


def get_atoms_valoration_possibilities(number_of_atoms: int) -> list[list[str]]:
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


def get_formula_valoration(formula: Formula, atoms_valoration: list[str]) -> list[str]:
	if isinstance(formula, Not):
		if atoms_valoration[0] == 'F':
			return ['T']
		else:
			return ['F']
	elif isinstance(formula, And):
		if atoms_valoration[0] == atoms_valoration[1] == 'T':
			return ['T']
		else:
			return ['F']
	elif isinstance(formula, Or):
		if atoms_valoration[0] == atoms_valoration[1] == 'F':
			return ['F']
		else:
			return ['T']
	elif isinstance(formula, Implies):
		if atoms_valoration[0] == 'T' and atoms_valoration[1] == 'F':
			return ['F']
		else:
			return ['T']
