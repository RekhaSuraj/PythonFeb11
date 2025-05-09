# Using the LEGB Rule for Python Scope
# Python resolves names using the so-called LEGB rule, which is named after the Python scope for names. The letters in LEGB stand for Local, Enclosing, Global, and Built-in. Here’s a quick overview of what these terms mean:

# Local (or function) scope is the code block or body of any Python function or lambda expression. 
# This Python scope contains the names that you define inside the function. 
# These names will only be visible from the code of the function. It’s created at function call, not 
# at function definition,
#  so you’ll have as many different local scopes as function calls. 
# This is true even if you call the same function multiple times, or recursively. 
# Each call will result in a new local scope being created.

# Enclosing (or nonlocal) scope is a special scope that only exists for nested functions. 
# If the local scope is an inner or nested function, then the enclosing scope is the scope of the outer or enclosing function. 
# This scope contains the names that you define in the enclosing function. 
# The names in the enclosing scope are visible from the code of the inner and enclosing functions.

# Global (or module) scope is the top-most scope in a Python program, script, or module. 
# This Python scope contains all of the names that you define at the top level of a program or a module.
#  Names in this Python scope are visible from everywhere in your code.

# Built-in scope is a special Python scope that’s created or loaded whenever you run a script or open an interactive session.
#  This scope contains names such as keywords, functions, exceptions, and other attributes that are built into Python.
#  Names in this Python scope are also available from everywhere in your code. 
# It’s automatically loaded by Python when you run a program or script.


# Nested Functions: The Enclosing Scope
# Enclosing or nonlocal scope is observed when you nest functions inside other functions. 
# The enclosing scope was added in Python 2.2. It takes the form of the local scope of any enclosing function’s local scopes.
#  Names that you define in the enclosing Python scope are commonly known as nonlocal names.
#  """
# print(v1)





