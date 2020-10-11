def get_prefix(string):
	for x in range(len(string)):
	  for y in range(len(string)):
	    if string[y][x] == string[y+1][x] and string[y+1][x]==string[y+2][x] :
	      print(string[y][x])