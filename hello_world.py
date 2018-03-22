#See if the user wants the console to print "Hello, world."
print("Do you want me to say hello to the world?")
desires = input("Should I? \n")
if desires.lower() == "yes":
	print("Hello world.")
else:
	print("I blame Chris for this!")