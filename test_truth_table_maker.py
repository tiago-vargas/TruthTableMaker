from truth_table_maker import *
from modules.formula import *


def test_truth_table_for_single_atom():
	p = Atom('p')

	table = make_truth_table(atoms=[p], formulas=[p])

	assert table == [
		['p'],
		['T'],
		['F'],
	]


def test_truth_table_for_two_atoms():
	p = Atom('p')
	q = Atom('q')

	table = make_truth_table(atoms=[p, q], formulas=[p, q])

	assert table == [
		['p', 'q'],

		['T', 'T'],
		['T', 'F'],
		['F', 'T'],
		['F', 'F'],
	]
