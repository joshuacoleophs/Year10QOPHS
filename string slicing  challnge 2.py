#Ask a user to enter their first name
#Ask a user to enter their last name
#Join them together with a space between the first and last name
#Store the length of their whole name in a variable
#Display there whole name
#Display the length of their whole name (including the space)

f_name = str(input("Enter your first name >>> "))
l_name = str(input("Enter your last name >>> "))

full_name = f_name + " " + l_name
print(full_name)
print(len(full_name))
