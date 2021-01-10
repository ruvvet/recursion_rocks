# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the factorial of a given number.


# 5! = 5 * 4!
# 4! = 4 * 3!
# 3! =3 * 2!
# ...
# 5! = 5 * 4 * 3 * 2 *1

def factorial(n):
    # Base case
    if n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(5))


# print(factorial(5))
# => 120
