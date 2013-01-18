#pig latin translator version 1.0 11-27-12

print """Thank you for using the English to Pig Latin Translator, Please type your 
input on the next line without any conjuctions."""

def translate():
	org_state = raw_input(">>>")
	org_state =[element.lower() for element in org_state]
	org_state = ''.join(org_state)
	wrd_brk_dwn = org_state.split(" ")
	finished = list()
	
	vowel = ['a','e','i','o','u']
	for word in wrd_brk_dwn:
		let_brk_dwn = list(word)

		punctuation = ['.','!','&',';',',',':',"'","?"]
		while let_brk_dwn[-1] in punctuation:
			let_brk_dwn.pop()

		first = let_brk_dwn[0]
		let_brk_dwn.append(first)
		let_brk_dwn.remove(first)
		
		if first in vowel:
			let_brk_dwn.extend(['y'])

		else:
			let_brk_dwn.extend(["a", "y"])
			
		mk_wrd = "".join(let_brk_dwn)
		finished.append(mk_wrd)

	full_sentence = " ".join(finished)
	print full_sentence

translate()

print 'Would you like to translate something else?'
ano_trans = raw_input("y/n? \n>>>").lower()

while ano_trans == "y":
	print 'New input'
	translate()
	print 'Would you like to translate something else?'
	ano_trans = raw_input("y/n? \n>>>").lower()
	
else:
	print "Thank you for using the Pig Latin Translator"



