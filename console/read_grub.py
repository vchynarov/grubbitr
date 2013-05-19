### 
# Written by Viktor Chynarov, May 10, 2013
#
# This is a module that contains all the information for
# reading grub.cfg files and getting all required important
# information out of it.
#

def get_lines(input_file):
	raw_file = open(input_file, "r")
	raw_lines = raw_file.readlines()
	raw_file.close()
	return raw_lines

def find_os_names(raw_lines):
	""" Determines the current names of the operating system. """
	menu_entry_indices = []
	os_names = []
	
	for line in raw_lines:
		if line.startswith("menuentry"):
			menu_entry_indices.append(raw_lines.index(line))

	for i in menu_entry_indices:
		current_line = raw_lines[i]
		first_quote = current_line.index("'") + 1
		second_quote = current_line[first_quote:].index("'")
		end_quote = first_quote + second_quote	

		os_names.append(current_line[first_quote:end_quote])
	
	return menu_entry_indices, os_names

def find_os_config(raw_lines, end_of_file, menu_entry_indices):
	""" This determines the start and end positions of a glob of text. """ 
	
	os_config_data = []
	os_config_indices = []

	for i in menu_entry_indices[:]:
		for j in xrange(i, end_of_file):
			if raw_lines[j].startswith("}\n"): #Because menu entries are ended by '}\n'
				os_config_indices.append((i,j))
				break		

	return os_config_indices

def load_os_data(raw_lines, os_config_indices, os_names):
	""" This loads the entire configuration for an operating system."""

	os_dictionary = {}

	for os_index in os_config_indices:
		start_line = os_index[0]
		end_line = os_index[1]
		i = os_config_indices.index(os_index)		
		os_lines = raw_lines[start_line:end_line + 1]
		os_name = os_names[i]
		os_dictionary[os_name] = os_lines

	return os_dictionary			

def get_full_info(input_file):
	os_names = []
	
	raw_lines = get_lines(input_file)	
	end_of_file = len(raw_lines)

	menu_entry_indices, os_names = find_os_names(raw_lines)
	os_config_indices = find_os_config(raw_lines, end_of_file, menu_entry_indices)
	os_dictionary = load_os_data(raw_lines, os_config_indices, os_names)

	token = (os_names, os_dictionary, raw_lines)
	return token

