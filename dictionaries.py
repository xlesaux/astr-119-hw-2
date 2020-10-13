#define a dictionary data structure


#dictionaries have a key:value for its elements
example_dict = {
	"class" : "Astr 119",
	"prof"  : "Brant",
	"awesomeness" : 10
}	

print(type(example_dict))
print(example_dict)

#get a value via key
course = example_dict["class"]
print(course)

#change a value at key
example_dict["awesomeness"] += 1

print(example_dict)

#print dictionary element by element 
for x in example_dict.keys():
	print(x,example_dict[x])