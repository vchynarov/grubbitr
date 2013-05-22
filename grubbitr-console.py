### 
# Written by Viktor Chynarov, May 9- 2013
#
#
# A program to edit the grub.cfg file so you have nice
# operating systems listed.
from console import read_grub, write_grub, backend
import settings
grub_directory = settings.grub_directory 

def switch(os_names):
	""" The command line UI behind the switch function. """
	try:
		print "Which number would you like to move?"
		first_pos = int(raw_input(" #: ")) - 1

		print "Which number would you like to swap with position {0}?".format(first_pos + 1)
		second_pos = int(raw_input(" #: ")) - 1

		os_names[first_pos], os_names[second_pos] = os_names[second_pos], os_names[first_pos]
	
	except IndexError:
		print "That number is not in the list."

	except ValueError:
		print "You did not enter a number."

	return os_names

def rename(os_names, os_dictionary):
	""" The command line UI behind the rename function. """ 
	try:
		print "What position name would you like to change? "
		choice = int(raw_input("#: ")) - 1
		os_name = os_names[choice] 
	
		print "What name would you like to change it to? "
		new_name = raw_input("New Name: ")
		os_names, os_dictionary = backend.rename(os_names, os_dictionary, os_name, new_name)
	
	except IndexError:
		print "That number is not in the list."

	except ValueError:
		print "You did not enter a number."

	return os_names, os_dictionary

def prompt(os_token):
	""" The overall wrapper for commandline user input. """
	os_lines, os_names, os_dictionary, = os_token

	# This removes unneeded lines like old comments and menu entries.
	os_lines = write_grub.create_clean_config(os_lines) 

	while 1:
		print "\nYour current OS arrangement is: \n"
		
		for position, os_name in enumerate(os_names, 1):
			print "{0} \t {1}".format(position, os_name)
		
		print "\nYou can either 'save', 'quit', 'switch', or 'rename'"

		choice = raw_input("?: ")
		if choice == "quit": 
			break 

		elif choice == "switch":
			os_names = switch(os_names)
	
		elif choice == "rename":
			os_names, os_dictionary = rename(os_names, os_dictionary)

		elif choice == "save":	
			query_line = "What file would you like to save the new configuration to? "

			if settings.grub_overwrite:
				default = "grub.cfg"
			else:
				default = "newgrub.cfg"

			print "{0} (default={1})".format(query_line, default) 

			file_name = raw_input("File Name: ")
			if not file_name:
				 file_name = default 
			
			write_grub.write_to_file(os_lines, os_names, os_dictionary, grub_directory + file_name)
			break

### End of writing and modifying function definitions.

if __name__ == "__main__":
	"""
	os_token is a tuple that contains a list of the names of
	all operating systems, followed by the dictionary with
	the names and their respective configuration,
	followed by all of the lines in the file.
	"""
	os_token = read_grub.get_full_info(grub_directory + "grub.cfg")
	prompt(os_token)

