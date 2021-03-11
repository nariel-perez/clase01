cadena='geringoso'

new=''

for c in cadena:
	new=new+c
	if c=='a':
		new=new+'pa'
	elif c=='e':
		new=new+'pe'
	elif c=='i':
		new=new+'pi'
	elif c=='o':
		new=new+'po'
	elif c=='u':
		new=new+'pu'
	
print(new)
