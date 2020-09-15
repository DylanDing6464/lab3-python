# Author: Dylan Ding dvd5567@psu.edu
# Collaborator: Eric Wang evw5332@psu.edu
# Collaborator: Matthew Nagle men5266@psu.edu
# Collaborator: Ryan Morgan rkm5607@psu.edu
# Section: 7
# Breakout: 1

def sum_n(n):
	if n == 0: 
		return 0
	return n + sum_n(n - 1)

def print_n(s, n):
  if len(s) == 0:
    return s
  return s + print_n(s, n-1) 
	
def run():
	n = int(input("Enter an int: "))
	print(f"{sum_n(n)}")
	
	s = input("Enter a string: ")
	print(f"{print_n(s, n)}")
	
if __name__ == "__main__":
	run()
	
  
