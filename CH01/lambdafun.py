"""
This code block explain the usage of lambda functions

The term lambda comes from a form of mathematical calculus invented by Alonzo Church. The good
news is that you don’t need to know anything about the math to use lambda functions! The idea
behind a lambda function is that it is an anonymous function block, usually very small, that you can
insert into code that then calls the lambda function just like a normal function. Lambda functions
are not things you will use often, but they are very handy when you would otherwise have to create a
lot of small functions that are used only once. They are often used in GUI or network programming
contexts, where the programming toolkit requires a function to call back with a result.
A lambda function is defi ned like this:
lambda <param1, param2, ...,paramN> : <expression>


"""

# Suppose you have write a code to compute straight line for value given as mentioned below
# this is how you will use lambda function to compute that in a line.


straight_line = lambda m, x, c: m * x + c

print(straight_line(2, 4, -3))
