def get_prefix(string):
	for i in range(len(string)):
	  for y in range(len(string)):
	    if string[y][x] == string[y+1][i] and string[y+1][i]==string[y+2][i] :
	      print(string[y][i])
