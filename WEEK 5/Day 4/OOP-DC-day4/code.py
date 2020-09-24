class Text():

	def __init__(self, text):
		self.text = text.lower()
		self.most_used = None


	@staticmethod
	def from_file(file_path):
		with open(file_path, 'r') as f:
			file_text = f.read()
		return Text(file_text)


	def word_count(self, word):
		return self.text.split(" ").count(word)


	def most_used_word(self):
		if self.most_used:
			return self.most_used

		print("Checking all words")
		words = {}

		for word in self.text.split(" "):
			if word in words:
				words[word] += 1
			else:
				words[word] = 1

		count = 0
		word = ""
		for key, value in words.items():
			if value > count:
				count = value
				word = key

		self.most_used = word, count
		return self.most_used



class TextModification(Text):

	def without_punctuation():
		pass



