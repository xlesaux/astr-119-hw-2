import numpy as np 

def main():
	i = 0      #integers can be delared with a number
	n = 10     #another one
	x = 119    #foating point numers are delcareed with a "."



	y = np.zeros(n,dtype=float)  #declares 10 seros as faots using np

	#use loop to iterate with a variable 

	for i in range(n) :   #i in range [0, n-1]
		y[i] = 2.0 * float(i) + 1   #set y = 2i+1 as flaots

	# also simpy iterate through a variable 
	for y_element in y:
		print(y_element)

		
if __name__ == "__main__":
	main()