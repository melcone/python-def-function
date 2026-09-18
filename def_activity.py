"""
A function is used for abstracting and making code more maintanable.
It groups related lines of codes that perform a task, which can then be executed multiple times with ease by simply calling the function how many times needed.
How it's used for abstracting is that you can name the function into something that describes what the code inside the function does.
This allows developers to use the function without needing to read and understand the internal code.

"print()" is an example of a function. It is one of the many built in functions in python.
The internal code of the "first_function()" below is a bunch of functions, so they're functions inside another function!
"""
def my_first_function():
    print('This text is printed because the code called the "thisIsAFunction" function')
    print('This is another line of text to show that it can run multiple lines of code')
    print('This is another line of text to show that it can run multiple lines of code')

my_first_function()