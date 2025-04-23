# class --> blue print or template
# object---> instance or copy of the class
# members--> variables and methods present in class
# types of variable
# 	1. instance variable
# 		a. to store private information (unique to the object)
# 		b. associated with object
# 		c. access used using objectname or self
# 		d. each object will have its own copy the variable
# 	2. class variable
# 		a. to store common information (same for all the object)
# 		b. associated with Class
# 		c. access used using ClassName or cls
# 		d. each object will point to same variable
#
# types of methods
#
# 	1. class methods
# 		a. created using @classmethod -->decorator
# 		b. takes cls as argument
# 		c. associated with class
# 		d. we can call it by using class name
# 		e. class methods can access only class variable (and not instance variable)
#
# 	2. instance methods
# 		a. created without using any decorator
# 		b. takes self as argument
# 		c. associated with object
# 		d. we can call it by using object
# 		e. instance methods can access both instance variable & class variable
#
# 	3. static methods
# 		a. created using @staticmethod -->decorator
# 		b. does not take cls/self argument
# 		c. associated with class
# 		d. we can call it by using class name
# 		e. we do not access any variable of the class or instance
#
# Note:
#
# 1.using class name we can access class variable and class methods
# 2. using object we can access we can access both instance & class variable, we can call both instance & class methods
#
# How do u declare instance variable and class variable?
# instance variable--> using self or object name
# class variable--> declare it inside the calss (outside of any method) without using any keywords
#
# How do u decide whether variable should be instance or class variable?
# if we are storing private information or unique information then it will be instance variable
# if we are storing public information or common information then it will be class variable
#
#
# How do u decide whether method should be instance method or class method?
# 1. if method is accessing only class variable then that method should be declared as class method
# 2. if method is accessing only instance variable  or both intance & class variable then method should be declared as instance method
# 3. if method is not accessing any variable of the class/object--> then method should be declared as static method
#
# only class variable--> Class Method
# only intance variable--> Instance Method
# both--> Instance Method
# none-->Static Method
#
# visibility (for both var & method)
# 1 public --> accessible everywhere
# 2. private --> accessible only with in the class
#
