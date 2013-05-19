### 
# Written by Viktor Chynarov, May 9- 2013
#
#
# A program to edit the grub.cfg file so you have nice
# operating systems listed.

def remove_entries(lines):
	""" This removes the old menu entries from the grub.cfg file. """		
	ranges_to_remove = []
	for i, line in enumerate(lines):

		if line[:9] == "menuentry":
			start_indice = i	
			for j, sub_line in enumerate(lines[i + 1:]):
				if sub_line[:2] == "}\n":
					end_indice = j	
					break
			ranges_to_remove.append((i, i + j + 1))
		
	to_remove = []
	for i, line in enumerate(ranges_to_remove):
		to_remove += range(line[0], line[1] + 1)	

	modified_lines = []
	for i in xrange(0, len(lines)):
		if i not in to_remove:
			modified_lines.append(lines[i])

	# The following snippet removes commented out titles.
	for line in modified_lines:
		if "###" in line:
			modified_lines.remove(line)

	return modified_lines 

def write_config_file(lines, filename="newgrub.cfg"):
	raw_file = open(filename, "w")
	for line in lines: raw_file.write(line)	
	raw_file.close()

	return 

def add_operating_systems(modified_lines, temp_names, os_dictionary):
	for os_name in temp_names:
		os_config = os_dictionary[os_name]
		modified_lines.append("\n")
		for config_line in os_config: modified_lines.append(config_line)

	return modified_lines	

def write_to_file_wrapper(modified_lines, os_names, os_dictionary, file_name):
	modified_lines = add_operating_systems(modified_lines, os_names, os_dictionary)
	write_config_file(modified_lines, file_name)
	
def create_clean_config(modified_lines):
	"""
	This function is a routine for running 3 other functions. 
	The other three functions remove the configuration details for the other operating systems present.
	This creates a 'blank' grub.cfg.
	"""
	
	modified_lines = remove_entries(modified_lines) # Sets indices for removal of crud.
	label_string = "\n### BEGIN grubbitr custom GRUB menu entries. ###\n"
	modified_lines.append(label_string)

	return modified_lines



