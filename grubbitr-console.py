### 
# Written by Viktor Chynarov, May 9- 2013
#
#
# A program to edit the grub.cfg file so you have nice
# operating systems listed.
from console import read_grub, write_grub, backend
import settings
grub_directory = settings.grub_directory 

def switch(temp_names):
	""" The command line UI behind the switch function. """
	try:
		print "Which number would you like to move?"
		first_pos = int(raw_input(" #: ")) - 1
		print "Which number would you like to swap with position {0}?".format(first_pos + 1)

		second_pos = int(raw_input(" #: ")) - 1

		temp_names[first_pos], temp_names[second_pos] = temp_names[second_pos], temp_names[first_pos]
		return temp_names
	
	except:
		print "Incorrect values were entered!"
		return temp_names

def rename(temp_names, temp_dictionary):
	""" The command line UI behind the rename function. """ 
	try:
		print "What position name would you like to change? "
		choice = int(raw_input("#: ")) - 1
		os_name = temp_names[choice] 
	
		print "What name would you like to change it to? "
		new_name = raw_input("New Name: ")
		temp_names, temp_dictionary = backend.rename(temp_names, temp_dictionary, os_name, new_name)
		return (temp_names, temp_dictionary)	
	
	except:
		print "Incorrect values were entered!"
		return (temp_names, temp_dictionary)

def prompt(modified_lines, os_names, os_dictionary, ):
	""" The overall wrapper for commandline user input. """
	temp_names = os_names[:]
	temp_dictionary = os_dictionary.copy()

	while 1:

		print "\n"
		print "Your current OS arrangement is: \n"
		
		for position, os_name in enumerate(temp_names):
			print "{0} \t {1}".format(position + 1, os_name)
		
		print "\nYou can either 'save', 'quit', 'switch', or 'rename'"

		choice = raw_input("?: ")
		if choice == "quit": break 

		elif choice == "switch":
			temp_names = switch(temp_names)
	
		elif choice == "rename":
			temp_names, temp_dictionary = rename(temp_names, temp_dictionary)

		elif choice == "save":	
			query_line = "What file would you like to save the new configuration to? "
			if settings.grub_overwrite:
				default = "grub.cfg"
			else:
				default = "newgrub.cfg"

			print "{0} (default={1})".format(query_line,default) 

			file_name = raw_input("File Name: ")
			if file_name == "": file_name = default 
			
			write_grub.write_to_file_wrapper(modified_lines, temp_names, temp_dictionary, grub_directory + file_name)
			return

		else:
			continue

	return 

### End of writing and modifying function definitions.
os_token = read_grub.get_full_info(grub_directory + "grub.cfg")
os_names = os_token[0] 
os_dictionary = os_token[1]
modified_lines = os_token[2]

# Modified_lines contains no crud right now.
modified_lines = write_grub.create_clean_config(modified_lines)

if __name__ == "__main__":
	# User input to modify the file.
	prompt(modified_lines, os_names, os_dictionary)

