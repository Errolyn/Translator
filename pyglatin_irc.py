
def translate(test_string):
	org_state = test_string
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

test_string = "this is a string"

translate(test_string)