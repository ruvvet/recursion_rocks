# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the Nth number in the fibonacci sequence.
# https://en.wikipedia.org/wiki/Fibonacci_number
# For this function, the first two fibonacci numbers are 1 and 1


# n=5 >> 5
# fib(5) = fib(4) + fib (3)
# fib(5) = (fib(3) + fib(2)) + (fib(2) + fib(1))
# ...
# fib(5) =...

def fib(n):

    # Base case
    if n == 0:
        return 0
    # exceptions
    elif n == 1:
        return 1
    elif n < 0:
        return 0

    # Recursive case
    return fib(n-1) + fib(n-2)


print(fib(7))

# print(fib(-1))
# => 0
# print(fib(0))
# => 0
# print(fib(1))
# => 1
# print(fib(2))
# => 1
# print(fib(7))
# => 13
