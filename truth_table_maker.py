from modules.formula import *


def make_truth_table(atoms: list[Atom], formulas: list[Formula]=[]) -> list[list[str]]:
	table = []

	header = _get_truth_table_header(atoms, formulas)
	table.append(header)

	rows = _get_truth_table_rows(atoms, formulas)
	for row in rows:
		table.append(row)

	return table


def _get_truth_table_header(atoms: list[Atom], formulas: list[Formula]) -> list[str]:
	atoms_header = [atom.name for atom in atoms]
	formulas_header = [formula.__str__() for formula in formulas]

	header = atoms_header + formulas_header

	return header


def _get_truth_table_rows(atoms: list[Atom], formulas: list[Formula]) -> list[list[str]]:
	rows = []

	possible_truth_values_for_atoms = get_all_possible_truth_values_for_atoms(len(atoms))
	for atoms_truth_value in possible_truth_values_for_atoms:
		row = get_truth_values_of_all_formulas(formulas, atoms_truth_value)
		rows.append(row)

	return rows


def get_all_possible_truth_values_for_atoms(number_of_atoms: int) -> list[list[str]]:
	result = []

	binary_numbers = _get_binary_numbers_as_strings(number_of_atoms)

	for number in binary_numbers:
		result.append(_convert_digits_of_binary_number_to_T_or_F(number))

	return result


def _get_binary_numbers_as_strings(number_of_atoms: int) -> list[str]:
	results = []

	for counter in range(2 ** number_of_atoms):
		results.append(f'{counter:0{number_of_atoms}b}')

	return results


def _convert_digits_of_binary_number_to_T_or_F(string: str) -> list[str]:
	result = []

	for character in string:
		if character == '0':
			result.append('F')
		elif character == '1':
			result.append('T')

	return result


def get_formula_truth_value(formula: Formula, atoms_truth_value: list[str]) -> str:
	if isinstance(formula, Not):
		if atoms_truth_value[0] == 'F':
			return 'T'
		else:
			return 'F'
	elif isinstance(formula, And):
		if atoms_truth_value[0] == atoms_truth_value[1] == 'T':
			return 'T'
		else:
			return 'F'
	elif isinstance(formula, Or):
		if atoms_truth_value[0] == atoms_truth_value[1] == 'F':
			return 'F'
		else:
			return 'T'
	elif isinstance(formula, Implies):
		if atoms_truth_value[0] == 'T' and atoms_truth_value[1] == 'F':
			return 'F'
		else:
			return 'T'


def get_truth_values_of_all_formulas(formulas: list[Formula], atoms_truth_value: list[str]) -> list[str]:
	formulas_truth_value = []

	if len(formulas) == 1:
		formulas_truth_value.append(get_formula_truth_value(formulas[0], atoms_truth_value))
	elif len(formulas) == 2:
		formulas_truth_value.append(get_formula_truth_value(formulas[0], atoms_truth_value[0:2]))
		formulas_truth_value.append(get_formula_truth_value(formulas[1], atoms_truth_value[1:]))
	elif len(formulas) == 4:
		formulas_truth_value.append(get_formula_truth_value(formulas[0], atoms_truth_value[0:2]))
		formulas_truth_value.append(get_formula_truth_value(formulas[1], atoms_truth_value[1:]))
		formulas_truth_value.append(get_formula_truth_value(formulas[2], atoms_truth_value[::2]))
		formulas_truth_value.append(get_formula_truth_value(formulas[3], atoms_truth_value[::2]))

	row = atoms_truth_value + formulas_truth_value

	return row
