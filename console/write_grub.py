### 
# Written by Viktor Chynarov, May 9- 2013
#
#
# A program to edit the grub.cfg file so you have nice
# operating systems listed.

def remove_entries(lines):
    """ This removes the old menu entries from the grub.cfg file. """       
    no_blocks_lines = []
    remove_block = False

    for line in lines:
        
        if "###" in line:
            continue
        if remove_block:
            continue
        if line.startswith("}\n") and remove_block == True:
            remove_block = False
            continue
        if line.startswith("menuentry"):
            remove_block = True
            continue

        no_blocks_lines.append(line) # If script proceeds here, then current line is not in block.

    modified_lines = []
    # This part removes wasteful and unneeded whitespace.
    for line in no_blocks_lines:
        empty = False

        if line == "\n" and not empty:
            empty = True
            continue

        elif line == "\n" and empty:
            continue
 
        elif line != "\n" and empty:
            empty = False

        modified_lines.append(line)

    return modified_lines 

def write_to_file(modified_lines, os_names, os_dictionary, file_name):
    modified_lines = create_clean_config(modified_lines)

    for os_name in os_names:
        modified_lines.append("\n")

        for line in os_dictionary[os_name].data:
            modified_lines.append(line)

    with open(file_name, "w") as raw_file:
        raw_file.writelines(modified_lines)

def create_clean_config(modified_lines):
    """
    This creates a 'blank' grub.cfg.
    """
    
    modified_lines = remove_entries(modified_lines) # Sets indices for removal of crud.
    label_string = "\n\n### BEGIN grubbitr custom GRUB menu entries. ###\n"
    modified_lines.append(label_string)

    return modified_lines



