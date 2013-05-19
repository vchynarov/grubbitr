This is a project written by Viktor Chynarov, licensing under the GNU General License will 
be added shortly.

Essentially, there are two main parts to this project, the commandline version (console) and 
the GTK-based version (gui). The gui relies on modules from the console version.


How it works:

Basically, ensure you have permission to read and write the grub.cfg file on /boot/grub.

Instructions for console:

	1.) Copy the file to the same directory as /grubbitr/console/
	2.) Run grubbitr-console.py. Ensure the name of the file remains as grub.cfg.
	3.) Type out the four possible commands, quit, save, rename or switch.
	4.) After you're done, save your changes.
	5.) You will then get a file with an updated grub menu configuration.
	6.) Replace your current grub.cfg in /boot/grub/ with this file. (BACKUP FIRST!)


Instructions for GUI:
	-GUI to be implemented.

