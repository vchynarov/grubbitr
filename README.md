grubbitr 
========
**Simple GRUB menu customization, without difficulty.**

This is a project written by Viktor Chynarov, licensing under the GNU General License will 
be added shortly.

Essentially, there are two main parts to this project, the commandline version (console) and 
the GTK-based version (gui). The gui relies on modules from the console version.


How it works:
--------------
Basically, ensure you have permission to read and write the grub.cfg file on /boot/grub.

Instructions for console:

	1.) Run grubbitr-console.py as a superuser. Ensure the name of the file remains as grub.cfg.
	2.) Type out the four possible commands, quit, save, rename or switch.
	3.) After you're done, save your changes.
	4.) If grub_overwrite is set to True in settings.py, then your new
		grub configuration is automatically done.

Instructions for GUI:
	-GUI to be implemented.

