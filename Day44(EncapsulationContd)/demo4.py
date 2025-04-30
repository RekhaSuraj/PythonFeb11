# Public vs Protected vs Private identifiers in Python:
#
#
# Access Modifier | Syntax Example    | Access Level                              | Accessible in Subclass?               | Accessible Outside Class?            | Internal Name?
# Public          | self.name         | No restriction (Fully open)               | ✅ Yes                                |✅ Yes                                | name
# Protected       | self._name        | Meant for internal use (by convention)    | ✅ Yes                                | ⚠️ Yes (but discouraged)            | _name
# Private         | self.__name       | Strongest level of hiding                 | ⚠️ Difficult (requires name mangling) | ⚠️ Difficult (via name mangling)   | _ClassName__name