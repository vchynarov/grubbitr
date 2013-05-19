### 
# Written by Viktor Chynarov, May 10, 2013
#
# This is a module that contains all the information for
# reading grub.cfg files and getting all required important
# information out of it.
#

def find_os_names(raw_lines):
	""" Determines the current names of the operating system. """
	menu_entry_indices = []
	os_names = []
	
	for line in raw_lines:
		# Finds the indices which will have an operating system.
		if line.startswith("menuentry"):
			menu_entry_indices.append(raw_lines.index(line))

	for i in menu_entry_indices:
		# Finds the names of the operating systems.
		current_line = raw_lines[i]
		first_quote = current_line.index("'") + 1
		second_quote = current_line[first_quote:].index("'")
		end_quote = first_quote + second_quote	

		os_names.append(current_line[first_quote:end_quote])
	
	return menu_entry_indices, os_names

def load_os_data(raw_lines, menu_entry_indices, os_names):
	""" This loads the entire configuration for an operating system."""

	end_of_file = len(raw_lines)
	os_config_indices = []
	os_dictionary = {}

	for i in menu_entry_indices:
		for j in xrange(i, end_of_file):
			if raw_lines[j].startswith("}\n"): # Last line of one OS menu entry.
				os_config_indices.append((i,j))
				break

	for os_index, os_name in zip(os_config_indices, os_names):
		# This loads the full configuration for each operating system.
		start_line = os_index[0]
		end_line = os_index[1]
		os_lines = raw_lines[start_line:end_line + 1]
		os_dictionary[os_name] = os_lines

	return os_dictionary			

def get_full_info(input_file):
	os_names = []
	
	with open(input_file, "r") as raw_file:
		raw_lines = raw_file.readlines()

	menu_entry_indices, os_names = find_os_names(raw_lines)
	os_dictionary = load_os_data(raw_lines, menu_entry_indices, os_names)

	return os_names, os_dictionary, raw_lines

