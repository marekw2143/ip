''' tries to get some letter '''
from numpy import *

matched = lambda val, threslod: val < threslod

def search(arr_in, threslod = 100):
	''' returns array indicating which pixels were vidited '''
	def match(val):
		return matched(val, threslod)

	visited = zeros ((arr_in.shape[0], arr_in.shape[1]), dtype = uint8)

	# search for first searching 
	for row in range(arr_in.shape[0]):
		for col in range(arr_in.shape[1]):
			if match(arr_in[row, col]):
				visit(arr_in, row, col, visited, threslod)
				break
	
	# now visited contains letter
	print visited

def visit(arr_in, row, col, visited, threslod, iteration = 1):
	if visited[row, col] or not matched(arr_in[row, col], threslod): return
		
	visited[row, col] = 1 # match as visited
	
	
	# check if area visited so far is a letter
	# if it is, or is a part - go on
	# if visiting in one direction may make a letter - go on in that direction - else - stop in that direction
	
	for x in range(-1, 2):
		for y in range(-1, 2):
			if x!=0 or y!=0:
				try:
					visit(arr_in, row+x, col+y, visited, threslod, iteration + 1)
				except:
					pass

			
		
if __name__ == '__main__':
	arr = array([	[0, 2, 2, 0],
					[2, 0, 2, 0],
					[2, 2, 0, 0]], dtype = uint8) 
	search(arr, 1)
