my_Name1 = input(" Enter your first name: ")
my_Name2 = input(" Enter your  last name: ")

print ("\n Hello, \n ")

name_format = ' {first} {last}.'

print( name_format.format( first=my_Name1, last=my_Name2),"Welcome!")