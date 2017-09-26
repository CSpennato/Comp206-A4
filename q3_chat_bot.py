import sys
import string
import random
import re

if len(sys.argv) == 1:
	print "Please provide the path to a text file"
	sys.exit()
def wordCount():
	words = {}
	punctuation = string.punctuation
	punctuation = punctuation.replace("!", "*")
	punctuation = punctuation.replace(".", "*")
	punctuation = punctuation.replace("?", "*")
	for i in range(1, len(sys.argv)):
		try:
			file=open(sys.argv[i], "r")
		except IOError:
			print "Error: One of the paths does not lead to a valid text file"
			sys.exit()
		else:
			contents = file.read()
			contents = contents.lower()
			contents = contents.replace("-", " ")
			contents = contents.replace("\n", " ")
			contents = contents.translate(None, punctuation)
			contents = re.split('[.?!]', contents)
			contents[:] = (value for value in contents if value != "")
			for sentence in contents:
				test = sentence.split()
				for i in range(0, len(test)):
					try:
						tmp = test[i] + '-' + test[i+1]
					except IndexError:
						tmp = test[i-1] + '-' + test[i]
						words[tmp] = 0
						break
					else:
						words[tmp] = 1
	return words

words = wordCount()
while 1:
	try:
		response = raw_input("Send: ")
	except EOFError:
		break
	else:
		print "Received: ",
		response = response.split()
		response = response[len(response) - 1]
		stop = 0
		boolean = 0
		for pairs in words:
			if pairs.split("-")[0] == response:
				response = pairs.split("-")[1]
				print response.capitalize(),
				stop += 1
				boolean = 1
				break
		if boolean == 0:
			num = random.randint(0, len(words))
			response = (words.keys())[num].split("-")[0]
			print response.capitalize(),
			stop += 1
		count = 2
		boolean = 0
		while 1:
			for pairs in words:
				if pairs.split("-")[0] == response:
					response = pairs.split("-")[1]
					if words[pairs] == 0:
						print "%s." % response
						boolean = 2
						break
					elif stop == 19:
						print "%s." % response
						boolean = 2
						break
					elif words[pairs] == count:
						count = count
					else:
						print response,
						words[pairs] += 1
						stop += 1
						boolean = 1
						break
			if boolean == 0:
				count += 1
			if boolean == 2:
				break
			

