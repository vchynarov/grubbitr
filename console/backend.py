def rename(temp_names, temp_dictionary, old_name, new_name):
	"""
	Renames an operating system. All configuration data
	of the old system is moved to the new name.
	"""

	temp_dictionary[new_name] = temp_dictionary.pop(old_name)
	name_line = temp_dictionary[new_name][0].replace(old_name, new_name)
	temp_dictionary[new_name][0] = name_line 
	temp_names[temp_names.index(old_name)] = new_name

	return temp_names, temp_dictionary
