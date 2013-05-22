class OS(object):

	def __init__(self, name, data):
		self.name = name
		self.data = data

	def change_name(self, new_name):
		name_line = self.data[0].replace(self.name, new_name)
		self.data[0] = name_line
		self.name = new_name
