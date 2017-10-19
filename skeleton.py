word = raw_input('Type in the word: ')
bigger = False
print "Your word is %s" % (word)

characters = {}

for x in word:
	if(characters.get(x, None) == None ):
		characters[x] = 1
	else:
		bigger = True
		characters[x] += 1

if bigger == False:
	print "%s has the highest occurance in %s" % (word[0],word)
	exit()

chibaba = word[0]

for x in characters:
	if characters[x] > characters[chibaba]:
		chibaba = x
	elif x == chibaba:
		if word.index(x) < word.index(chibaba):
			chibaba = x

print ""
print "%s has the highest number of occurances in %s" % (chibaba,word)