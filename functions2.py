import numpy as np 
import sys #allows us to read command lines 

#define a function that returns a value
def expo(x):  #x is an argument to the function
	return np.exp(x) #return the np e^x function 

#define a subroutine that does not return a value
def show_expo(n):
	for i in range(n):
		print(expo(float(i))) #call the expo funciton


#define a main function 
def main():
	n = 10 #prove default value for n

	#check if there is a command line argument provided
	if(len(sys.argv)>1):
		n = int(sys.argv[1])

	#print value of n
	print("n is equal to",n)

	#printe^x n times
	show_expo(n)

#run the main func
if __name__ == "__main__":
	main()

