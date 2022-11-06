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
