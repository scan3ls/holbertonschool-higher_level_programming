#!/usr/bin/python3
"""Doc"""


def inderits_from(obj, a_class):
	"""Check inherit"""
	
	if issubclass(type(obj), a_class):
		return True
	else:
		return False
