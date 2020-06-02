#!/usr/bin/python3
"""Doc"""


def is_kind_of_class(obj, a_class):
	"""Check inherit"""
	
	if issubclass(type(obj), a_class):
		return True
	else:
		return False
