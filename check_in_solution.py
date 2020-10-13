#define the main
def main():
	i = 0    #declare an integer i
	x = 119.0  #declare a float x

	for i in range(120):  #loop i from 0 to 119
		if ((i%2)==0):    #if i is even
			x += 3.		  #add 3
		else:			  #if i is odd
			x -= 5.       #subtract 5 from x
	s = "%3.2e" % x     #make a string containing x

	print(s)

if __name__ == "__main__":
	main()