# What is an abstract class in Python?
# What is an interface in Python?
# Difference between abstract class and interface in Python
#
# What is an Abstract class in Python?
# A blueprint for other classes might be thought of as an abstract class. You may use it to define a collection of methods
#
#
# 1.what is the advantage of declaring abstract methods in Parent class ?
# a).By declaring abstract methods in parent class we can providing guidelines to the child classes,
#  such that which methods compulsory they should implement.
#
# 2. Can a contain both abstract and non-abstract methods ?
# a).yes
# Note : if a class contains both abstract and non-abstract methods then child class is responsible to provide implementation only for abstract methods.
#
# The Most Important Conclusion :
# 1.If a class contains at least one abstract mehtods and if we are extending ABC class then instantiation is not possible.
# " For Abstract class with abstract methods, instantiation is not possible ".

# What is an Interface in Python?
# 1.An abstract class can contains both abstract and non-abstract methods.
# 2.If an abstract class contains only abstract methods, such type of abstract class is nothing but interface.
# 3.100% pure abstract class is nothing but interface.
# Interface simply acts as a Service Requirement Specifications(SRS).


from abc import ABC,abstractmethod

class RBI(ABC):

    @abstractmethod
    def CreateAccount(self):
        pass

    @abstractmethod
    def Deposit(self):
        pass

    @abstractmethod
    def Withdraw(self):
        pass

    @abstractmethod
    def Credit(self):
        pass


class HDFC(RBI):

    def CreateAccount(self):
        print('Submit documents')


    def Deposit(self):
        print('Min Deposit amount is 1000Rs')


    def Withdraw(self):
        print("Min Withdraw amount is 500Rs")


    def Credit(self):
        print('Credit money greater than or equal to 1')



class Canara(RBI):

    def CreateAccount(self):
        print('Submit documents along with photo')


    def Deposit(self):
        print('Min deposit amount is 500 Rs')


    def Withdraw(self):
        print('Min Withdraw amount is 100Rs')


    def Credit(self):
        print('Credit is greater than or equal to 1')


obj_HDFC = HDFC()
obj_HDFC.CreateAccount()
obj_HDFC.Deposit()
obj_HDFC.Withdraw()
obj_HDFC.Credit()

# Submit documents
# Min Deposit amount is 1000Rs
# Min Withdraw amount is 500Rs
# Credit money greater than or equal to 1