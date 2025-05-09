# Arrays
import array
print(help(array))
# This module defines an object type which can efficiently represent
#     an array of basic values: characters, integers, floating point
#     numbers.  Arrays are sequence types and behave very much like lists,
#     except that the type of objects stored in them is constrained.

# Array Allows homogenous datatypes
# what are the typecodes in array
print(array.typecodes)
# bBuhHiIlLqQfd


# | Type Code | C Type             | Python Type  | Size (bytes) | Description                    | Range Example                   |
# | --------- | ------------------ | ------------ | ------------ | ------------------------------ | ------------------------------- |
# | `'b'`     | signed char        | int          | 1            | Signed integer                 | -128 to 127                     |
# | `'B'`     | unsigned char      | int          | 1            | Unsigned integer               | 0 to 255                        |
# | `'u'`     | wchar\_t           | Unicode char | 2 (platform) | Unicode character (deprecated) | Single Unicode chars            |
# | `'h'`     | signed short       | int          | 2            | Signed short integer           | -32,768 to 32,767               |
# | `'H'`     | unsigned short     | int          | 2            | Unsigned short integer         | 0 to 65,535                     |
# | `'i'`     | signed int         | int          | 2 or 4       | Signed integer (platform size) | Typically -2^31 to 2^31−1       |
# | `'I'`     | unsigned int       | int          | 2 or 4       | Unsigned integer               | 0 to 2^32−1                     |
# | `'l'`     | signed long        | int          | 4            | Signed long integer            | -2,147,483,648 to 2,147,483,647 |
# | `'L'`     | unsigned long      | int          | 4            | Unsigned long integer          | 0 to 4,294,967,295              |
# | `'q'`     | signed long long   | int          | 8            | Signed 64-bit integer          | -2^63 to 2^63−1                 |
# | `'Q'`     | unsigned long long | int          | 8            | Unsigned 64-bit integer        | 0 to 2^64−1                     |
# | `'f'`     | float              | float        | 4            | 32-bit floating point          | ±3.4E±38                        |
# | `'d'`     | double             | float        | 8            | 64-bit floating point          | ±1.8E±308

