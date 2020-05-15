# 1+2
try:

    a = 1/0

except (TypeError, ZeroDivisionError):
    print("ZeroDivisionError: division by zero")

# 3.The finally clause executed no matter what.

try:
    x = 1 
finally:
    print("finally")


#  4.  catch *all* exceptions - generic except clause, which handles any exception (bare except).

# 5. it will catch all exceptions and handle every case in the same way

# 6. except IOError - input/output operation fails,
# such as the print statement or the open() function when trying to open a file that does not exist.
# It is also raised for operating system-related errors.
# except ZeroDivisionError -  dividing by zero.
