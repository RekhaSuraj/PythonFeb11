from abc import ABC,abstractmethod
# Abstract classes cannot be instantiated. (We cannot create an object of abstract classes)
# We have to implement all abstract methods in the child class.
# If we dont implement any abstract method in child class, we get error like below:
# TypeError: Can't instantiate abstract class DPS without an implementation for abstract method 'logout_time'

class School(ABC):

    @abstractmethod
    def login_time(self):
        pass

    @abstractmethod
    def logout_time(self):
        pass

#
# ob1 = School()
# ob1.logout_time()
# TypeError: Can('t instantiate abstract class School without an implementation for abstract '
#                'methods ')login_time', 'logout_time'


class DPS(School):

    def login_time(self):
        print('School starts at 8AM')

    def logout_time(self):
        print('School closes at 6PM')


obj_DPS = DPS()
obj_DPS.login_time()
obj_DPS.logout_time()

# School starts at 8AM
# School closes at 6PM