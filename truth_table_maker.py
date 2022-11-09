
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

	if number_of_atoms == 1:
		result.append(convert_binary_numbers_to_T_or_F('0'))
		result.append(convert_binary_numbers_to_T_or_F('1'))
	elif number_of_atoms == 2:
		result.append(convert_binary_numbers_to_T_or_F('00'))
		result.append(convert_binary_numbers_to_T_or_F('01'))
		result.append(convert_binary_numbers_to_T_or_F('10'))
		result.append(convert_binary_numbers_to_T_or_F('11'))
	else:
		result.append(convert_binary_numbers_to_T_or_F('000'))
		result.append(convert_binary_numbers_to_T_or_F('001'))
		result.append(convert_binary_numbers_to_T_or_F('010'))
		result.append(convert_binary_numbers_to_T_or_F('011'))
		result.append(convert_binary_numbers_to_T_or_F('100'))
		result.append(convert_binary_numbers_to_T_or_F('101'))
		result.append(convert_binary_numbers_to_T_or_F('110'))
		result.append(convert_binary_numbers_to_T_or_F('111'))

	return result


def convert_binary_numbers_to_T_or_F(string: str) -> list[str]:
	result = []

	for character in string:
		if character == '0':
			result.append('F')
		elif character == '1':
			result.append('T')

	return result
