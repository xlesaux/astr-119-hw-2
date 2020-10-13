import numpy as np 

#integers
i = 10
print("The tpy eof i is ",type(i))

a_i = np.zeros(i,dtype=int)
print("The type of a_i is", type(a_i))
print("The type of a_i[0] is", type(a_i[0]))


#floats
x = 119.0 #floating point number
print("The type of x is ", type(x)) #print out the type

y = 1.19e2
print("The type of y is ", type(y)) #print out the type

z = np.zeros(i,dtype=float) #delcare an array of floats
print("The type of z is ", type(z)) #print out the type
print("The type of z[0] is ", type(z[0])) #print out the type

