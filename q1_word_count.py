import sys
import string

if len(sys.argv) == 1:
	print "Please provide the path to a text file"
	sys.exit()
try:
	file=open(sys.argv[1], "r")
except IOError:
	print "Error: The path does not lead to a valid text file"
else:
	contents = file.read()
	contents = contents.lower()
	contents = contents.replace("-", " ")
	contents = contents.translate(None, string.punctuation)
	contents = contents.split()
	words = {}
	for word in contents:
		try:
			num = words[word]
		except KeyError:
			words[word] = 1
		else:
			words[word] = num + 1
	for word in sorted(words, key=words.__getitem__, reverse=True):
		print word + ":%s" % words[word]
