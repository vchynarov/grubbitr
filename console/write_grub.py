### 
# Written by Viktor Chynarov, May 9- 2013
#
#
# A program to edit the grub.cfg file so you have nice
# operating systems listed.

def create_write_space(lines):
	modified_lines = lines[:]
	begin_line = "\n\n### BEGIN grubbitr custom menu entries ###"
	modified_lines.append(begin_line)
	return modified_lines

def remove_entries(lines, mode="complete"):
	""" Three different possible methods to remove 'old' entries.
	
	complete: completely wipes everything from:
	"### BEGIN /etc/grub.d/30_os-prober" to
	"### END /etc/grub.d/40_custom	

	 """	
	for line in lines:
		if "### END" in line and "00_header" in line:
			start_line = lines.index(line) + 2
		elif "### BEGIN" in line and "41_custom" in line:
			end_line = lines.index(line) - 2
			break
	
	return (start_line, end_line)

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
	
	modified_lines = create_write_space(modified_lines) #Creates a comment for grubbitr at end.
	start_remove, end_remove = remove_entries(modified_lines) # Sets indices for removal of crud.
	modified_lines = modified_lines[:start_remove] + modified_lines[end_remove:]

	return modified_lines



