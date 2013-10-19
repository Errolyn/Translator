# Pyglatin Translator Version 1.01 1-8-13

# Takes word input and formats it in a usable format.
def translate(original_sentence):
	org_state = original_sentence
	org_state =[element.lower() for element in org_state]
	org_state = ''.join(org_state)
	wrd_brk_dwn = org_state.split(" ")
	finished = list()
	apostraphe = "'"
	vowel = ['a','e','i','o','u']

	# loops over each word to apply format changes\
	for word in wrd_brk_dwn:
		let_brk_dwn = list(word)
		each_letter =list(let_brk_dwn)

		punctuation = ['.','!','&',';',',',':',"?","'"]

		# Checks for conjunctions
		for indv_let in each_letter:
			if indv_let == apostraphe:
				print "I told you not to use a conjunction."
				return "I told you not to use a conjunction."
			
		# Strips out punctuation from the end of the word
		while let_brk_dwn[-1] in punctuation:
			let_brk_dwn.pop()

		# Changes position of first letter
		first = let_brk_dwn[0]
		let_brk_dwn.append(first)
		let_brk_dwn.remove(first)

		# Deals	with vowel or constonant cases	
		if first in vowel:
			let_brk_dwn.extend(['y'])
		else:
			let_brk_dwn.extend(["a", "y"])

		# Rebuilds sentence in to list			
		mk_wrd = "".join(let_brk_dwn)
		finished.append(mk_wrd)

	# Formats and prints final product
	full_sentence = " ".join(finished)
	print full_sentence.capitalize()
	return full_sentence.capitalize()

if __name__ == '__main__':

	print """Thank you for using the English to Pig Latin Translator, Please type your 
input on the next line without any conjunctions."""

	original_sentence = raw_input('>>> ')
	translate(original_sentence)

	# Allows user to continue with new string or end program
	print 'Would you like to translate something else?'
	ano_trans = raw_input("y/n? \n>>>").lower()

	while ano_trans == "y":
		print 'New input'
		original_sentence = raw_input('>>> ')
		translate(original_sentence)
		print 'Would you like to translate something else?'
		ano_trans = raw_input("y/n? \n>>>").lower()
		
	else:
		print "Thank you for using the Pig Latin Translator"



