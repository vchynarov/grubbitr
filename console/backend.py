def switch(temp_names, first_position, second_position):
	temp_names_size = len(temp_names)
	
	try:		
		temp = temp_names[first_position]
		temp_names[first_position] = temp_names[second_position]
		temp_names[second_position] = temp
		
	except:
		print "Incorrect values were entered!"

	return temp_names

def rename(temp_names, temp_dictionary, old_name, new_name):
	try:
		temp_dictionary[new_name] = temp_dictionary.pop(old_name)
		name_line = temp_dictionary[new_name][0]
		first_quote_pos = name_line.index("'")
		second_quote_pos = name_line[first_quote_pos + 1:].index("'")
		second_quote_pos += first_quote_pos + 1 

		new_name_line = name_line[:first_quote_pos + 1] + new_name + name_line[second_quote_pos:]
		temp_dictionary[new_name][0] = new_name_line

		for i, name in enumerate(temp_names):
			if name == old_name:
				temp_names[i] = new_name
				return (temp_names, temp_dictionary)		

	except: 
		print "Incorrect values were entered!"
		return (temp_names, temp_dictionary)
