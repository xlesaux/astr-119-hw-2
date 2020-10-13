#python expceptions let you deal with unexpected results


try:
	print(a) #this will throw an excpeption
except:
	print("a is not defined")

#there are specific errors in python
try:
	print(a) #this is will throw name error
except NameError:
	print("a is still not defined")
except:
	print("something else went wrong!")

#this will break our program
#"since a is not defined"
print(a)