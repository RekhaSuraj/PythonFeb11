# Concrete Methods in Abstract Base Classes :
# Concrete classes contain only concrete (normal)methods whereas abstract classes may contain both concrete methods
# and abstract methods.
# The concrete class provides an implementation of abstract methods,
# the abstract base class can also provide an implementation by invoking the methods via super().

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

    def KYC(self): #concrete method
        print('Know your customer')


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

class Basic:

    def perform_operation(self,bank_name:RBI):
        bank_name.CreateAccount()
        bank_name.Deposit()
        bank_name.Withdraw()
        bank_name.Credit()
        bank_name.KYC()


ob1 = Basic()
ob1.perform_operation(HDFC())
print()

ob1.perform_operation(Canara())

# Submit documents
# Min Deposit amount is 1000Rs
# Min Withdraw amount is 500Rs
# Credit money greater than or equal to 1
# Know your customer
#
# Submit documents along with photo
# Min deposit amount is 500 Rs
# Min Withdraw amount is 100Rs
# Credit is greater than or equal to 1
# Know your customer