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
  if n == 0:
    return 
  print(s)
  print_n(s, n-1) 
	
def run():
  n = input("Enter an int: ")
  n= int(n)
  sum_n(n)
  print(f"sum is {sum_n(n)}.")
  s = input("Enter a string: ")
  print_n(s, n)

if __name__ == "__main__":
	run()
	
  
