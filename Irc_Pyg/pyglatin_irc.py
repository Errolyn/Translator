



#from thing import string

key_word = "pig this" 

def translate(input_dict):
	"""
	Takes input that looks like this::

		{ 
			'channel': '#pdxbots',
			'sender': 'holscher',
			'msg': 'Hey there bot!',
		}

	Responds to ``pig this: <input>``

	Example::
	
		Input: pig this: hi there
		Output: ihay heretay

	"""
	
	inc_string = input_dict['msg']
	if key_word in inc_string:
		org_state = inc_string
		org_state =[element.lower() for element in org_state]
		org_state = ''.join(org_state)
		wrd_brk_dwn = org_state.split(" ")
		#print wrd_brk_dwn
		del wrd_brk_dwn[0]
		#print wrd_brk_dwn
		del wrd_brk_dwn[0]
		finished = list()

		
		vowel = ['a','e','i','o','u']
		for word in wrd_brk_dwn:
			let_brk_dwn = list(word)

			punctuation = ['.','!','&',';',',',':',"'","?","-","_","~","`"]
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
		print input_dict['channel'] +" "+ input_dict['sender'] + ", " + "Here it is: " + full_sentence

#test_string = "pig this: this is a string"

#if key_word in string
	#translate()

channels = ["#pdxbots", "#pdxpython"]
incoming_strings = ["hi", "translate", "pig this: hey there sam", "pig this: I hope this doesn't break!"]

for chan in channels:
	for incoming in incoming_strings:
		translate({'channel': chan, 'msg': incoming, 'sender': 'holscher'})



