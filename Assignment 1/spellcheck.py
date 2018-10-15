import enchant
from enchant.checker import SpellChecker
with open('data.txt', 'r') as myfile:
	textread=myfile.read().replace('\n', '')
txtchkr = SpellChecker("en_US")
txtchkr.set_text(textread)
for err in txtchkr:
	print ("ERROR:" ,err.word)


#print("Alhamdulillah")
