# If we want to use the module with a different name, we can use from..import…'as' statement.
# as serves as alias (aka)
import demo1 as arithmetic

print(arithmetic.addition(20,30))
print(arithmetic.subtraction(60,10))

# Summary
# 1. We can import a module by directly giving "import <file_name or class_name>"
# 2. We can import multiple modules by giving "import <file_name1, file_name2>" (separated by commas)
# 3. We can import specific functions from a file by giving "from <file_name> import <function_name>"
# 4. We can import all functions from a file by giving "from <file_name> import *"
# 5. We can rename a module by giving "import <file_name> as <new_name>"("as" keyword should be used for renaming)