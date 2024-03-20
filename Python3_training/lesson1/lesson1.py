#The 'print' function allows you to print information to the console.
print(12, 23,)
print('apple', 'pen')
#The parameter 'sep' is used in the print() function to specify the separator between the different arguments being printed.
print(12, 23, sep='-')
print('apple', 'pen', sep='-')
#The comma between the arguments in the print() function is what allows for the separation of values.

#The end parameter is used in the print() function in Python to specify what will be printed at the end of printing the arguments.
print(12, 23, sep='-', end='\n')#In Python, the special character \n represents a newline
print('apple', 'pen', sep='-', end='?')

#Let's try the same code without using \n to see the result.
'''
print(12, 23, sep='-', end='') #without using \n
print('apple', 'pen', sep='-', end='?')

The result was:
12-23apple-pen? 
'''
#Can you see it? It didn't break the line!