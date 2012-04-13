# PyCFG

class CFG:
	"""This is an attempt to incorporate straight CFG into Python in a regular-expression style.

Example usage:
>>> chef = CFG()
Done.

This sets the main layout of the Chef file. Notice that tokens are encased by {} and * means '0 or more' and () means 'optional' (potentially none, but at most one).
All symbols can be escaped as normal using a backslash.
>>> chef.define('{Title}.\n\n{Comments}Ingredients.\n{Ingredient}*\n\nMethod.\n{Command}*\n\n({Serves})\n\n{Auxiliaries}*', master=True)
Done.

The master can be set through the constructor as well:
>>> chef = CFG('{Title}.\n\n{Comments}Ingredients.\n{Ingredient}*\n\nMethod.\n{Command}*\n\n({Serves})\n\n{Auxiliaries}*')
Done.

Simple variables' CFGs are set thusly:
>>> chef.define('Comments', '{Sentence}*\n\n')
Done.

Variables can have more than one definition:
>>> chef.define('Comments', ['{Sentence}*\n\n', 'poop'])
Done.

Or you can simply add a definition:
>>> chef.define('Comments', 'poop', add=True)
"""
	pass