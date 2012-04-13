# PyCFG

class CFG:
	"""This is an attempt to incorporate straight CFG into Python in a regular-expression style.

Example usage:
>>> chef = CFG()
Done.

This sets the main layout of the Chef file. Notice that tokens are encased by {} and * means '0 or more' and () means 'optional' (potentially none, but at most one). (The master can also be set directly through the constructor.)
All symbols can be escaped as normal using a backslash.
>>> chef.define('{Recipe}\n\n({Serves}\n\n){Recipe}*', master=True)
Done.

>>> chef.define('Recipe', '{Title}.\n\n{Comments}Ingredients.\n{Ingredient}*\n\nMethod.\n{Command}*')
Done.

Simple variables' CFGs are set thusly:
>>> chef.define('Comments', '{Sentence}*\n\n')
Done.

Variables can have more than one definition:
>>> chef.define('Comments', ['{Sentence}*\n\n', 'poop'])
Done.

Or you can simply add a definition:
>>> chef.define('Comments', 'poop', add=True)

There is a protected variable with CFG called nil to terminate recursive definitions.
>>> chef.define('Comments', ['{Sentence}.', '{Sentence}. {Comments}', '{nil}']
Done.

Attempting to overwrite this variable will result in an error, even if the redefinition is trivial:
>>> chef.define('nil', '{nil}')
CFGError: Redefinition of nil is prohibited.
"""
	pass