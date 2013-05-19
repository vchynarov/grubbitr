import sys
import os

for directory in sys.path:
	if "/grubbitr/" in directory:
		dirs = directory.split("/")
		new_directory = ""
		for i in xrange(1, len(dirs) - 1): new_directory += "/" + dirs[i]
		sys.path.append(new_directory)

from settings import grubbitr_settings
print grubbitr_settings.grub_directory
