"""
Simple tool for finding the path to nested keys or values in complex objects or JSON.
"""
from datetime import datetime
from json import loads as jsonLoad
from sys import argv

def main():
	if len(argv) != 3:
		print("Usage: {} target input.json".format(argv[0]))
		return 1
	target, infile = argv[1], argv[2]
	with open(infile, 'r') as f:
		print('\n'.join(search(target, jsonLoad(f.read()))))

def search(target, structure, variableName="structure"):
	"""
	Search for a @target key or value in a possibly nested @search. 
	@return a list of printable strings that show the location and value of the target.
	"""
	def fmt(path, value):
		return "{}{} == {}".format(variableName, strFromPath(path), value)
	return [fmt(p,v) for p,v in _searchRecursive(target, structure, [])]

def strFromPath(path):
	"""
	Construct a string that represents the Python code required to retrieve a value from
	the structure.
	"""
	def fmt(x):
		if type(x) == str:
			return "['{}']".format(x)
		elif type(x) == int:
			return "[{}]".format(x)
		else:
			return x
	return ''.join([fmt(x) for x in path])

def _searchRecursive(target, structure, path, debugOutput=False):
	"""
	Receursively descends a structure in search of a target target or value.
	@yields: ([path], value)
	"""
	if debugOutput:
		print("\tSearching: {}".format(path))

	# Base case: finding the target in a dcitionary
	if type(structure) == dict and target in structure:
		yield path + [target], structure[target]

	# Base case: matching terminal value
	if target == structure:
		yield path, target

	# Lists
	if type(structure) == list:
		for i, item in enumerate(structure):
			yield from _searchRecursive(target, item,  path + [i])

	# Dictionaries
	if type(structure) == dict:
		for k,v in structure.items():
			yield from _searchRecursive(target, v, path + [k])

# Run!
if __name__ == '__main__':
	main()

