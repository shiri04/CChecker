class global_vars:

	def __init__(self, text, lines):
		self.text = ''.join(text)
		self.start = lines[0]
		self.end = lines[1]