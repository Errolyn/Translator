

org_state = raw_input()
org_state =[element.lower() for element in org_state]
org_state = ''.join(org_state)
print org_state

wrd_brk_dwn = org_state.split(" ")


for word in wrd_brk_dwn:
	let_brk_dwn = list(wrd_brk_dwn)
	let_brk_dwn.append(let_brk_dwn[0])
	let_brk_dwn.remove(let_brk_dwn[0])
	let_brk_dwn.append("a")

print ' '.join(let_brk_dwn)

#right now what I think this should be doing is giving me "isa aa testa thisa"
#but the out put is "this a is a a a test a" 