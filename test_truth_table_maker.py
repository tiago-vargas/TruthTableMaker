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


class TestOneConnectiveWithOnlyAtoms:
	def test_conjunction_between_two_atoms(self):
		p = Atom('p')
		q = Atom('q')

		table = make_truth_table(atoms=[p, q], formulas=[And(p, q)])

		assert table == [
			['p', 'q', '(p ∧ q)'],

			['F', 'F',    'F'   ],
			['F', 'T',    'F'   ],
			['T', 'F',    'F'   ],
			['T', 'T',    'T'   ],
		]


	def test_disjunction_between_two_atoms(self):
		p = Atom('p')
		q = Atom('q')

		table = make_truth_table(atoms=[p, q], formulas=[Or(p, q)])

		assert table == [
			['p', 'q', '(p ∨ q)'],

			['F', 'F',    'F'   ],
			['F', 'T',    'T'   ],
			['T', 'F',    'T'   ],
			['T', 'T',    'T'   ],
		]


	def test_implication_between_two_atoms(self):
		p = Atom('p')
		q = Atom('q')

		table = make_truth_table(atoms=[p, q], formulas=[Implies(p, q)])

		assert table == [
			['p', 'q', '(p → q)'],

			['F', 'F',    'T'   ],
			['F', 'T',    'T'   ],
			['T', 'F',    'F'   ],
			['T', 'T',    'T'   ],
		]


	def test_negation_of_atom(self):
		p = Atom('p')

		table = make_truth_table(atoms=[p], formulas=[Not(p)])

		assert table == [
			['p', '(¬p)'],
			['F',   'T' ],
			['T',   'F' ],
		]


class TestTwoFormulas:
	def test_two_conjuntions_between_atoms(self):
		p = Atom('p')
		q = Atom('q')
		r = Atom('r')

		formulas = [And(p, q), And(q, r)]

		table = make_truth_table(atoms=[p, q, r], formulas=formulas)

		assert table == [
			['p', 'q', 'r', '(p ∧ q)', '(q ∧ r)'],

			['F', 'F', 'F',    'F'   ,    'F'   ],
			['F', 'F', 'T',    'F'   ,    'F'   ],
			['F', 'T', 'F',    'F'   ,    'F'   ],
			['F', 'T', 'T',    'F'   ,    'T'   ],

			['T', 'F', 'F',    'F'   ,    'F'   ],
			['T', 'F', 'T',    'F'   ,    'F'   ],
			['T', 'T', 'F',    'T'   ,    'F'   ],
			['T', 'T', 'T',    'T'   ,    'T'   ],
		]
