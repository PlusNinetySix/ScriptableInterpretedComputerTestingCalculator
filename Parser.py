import string

fstream = None
offset = 0

def scan():
	global fstream
	global offset
	
	while True:
		fstream.seek(offset)
		character = fstream.read(1)
		offset += 1
		
		
		if character not in string.whitespace or character in "":
			break
		else:
			print('Skipping whitespace')
	
	return character
	
def filescanner(filename):
	global fstream
	global offset
	
	comment = False
	
	with open(filename) as fstream:
		while True:
			character = scan()
			
			if character in ['#']:
				comment = not comment
				continue
			
			if not character:
				break
				
			if not comment:
				word = [character]
				if character in string.ascii_letters:
					while True:
						lookahead = scan()
							if lookahead not in string.ascii_letters:
								offset -= 1
								character = "".join(word)
								break
							
							word.append(lookahead)
							
							
						if character in string.digits:
							while True:
								offset -= 1
								character = "".join(word)
								break
						word.append(lookahead)
								
				print(character)
			
	if comment:
		print('Error! comment not closed correctly.')
	
if __name__ == "__main__":
	filescanner("sample.sictc")