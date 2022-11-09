from truth_table_maker import *
from modules.formula import *


class TestAtoms:
	def test_truth_table_for_single_atom(self):
		p = Atom('p')

		table = make_truth_table(atoms=[p])

		assert table == [
			['p'],
			['F'],
			['T'],
		]


	def test_truth_table_for_three_atoms(self):
		p = Atom('p')
		q = Atom('q')
		r = Atom('r')

		table = make_truth_table(atoms=[p, q, r])

		assert table == [
			['p', 'q', 'r'],

			['F', 'F', 'F'],
			['F', 'F', 'T'],
			['F', 'T', 'F'],
			['F', 'T', 'T'],

			['T', 'F', 'F'],
			['T', 'F', 'T'],
			['T', 'T', 'F'],
			['T', 'T', 'T'],
		]

