# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨`

# This function returns an array of all possible
# outcomes from flipping a coin N times.
# Input type: Integer
# H stands for Heads and T stands for tails
# Represent the two outcomes of each flip as "H" or "T"


# n = flip 3 times
# flip 1 'H' 'T', n =2
# flip 2 'HH' 'HT//'TT', 'TH', n =1
# .. each recursion subtract n, call the func twice to get both cases


def coin_flips(n):
    # final
    result = []
    current = ''

    def add_flips(n, result, current):

        # Base case
        if n == 1:
            result.append(current + 'H')
            result.append(current + 'T')
            return result

        # call function again with n-1, add h/t to temp var current
        add_flips(n-1, result, current+'H')
        add_flips(n-1, result, current+'T')

# call add flips with n, initialized result, and initialized current
    add_flips(n, result, current)

    return result


print(coin_flips(3))

# print(coinFlips(2))
# => ["HH", "HT", "TH", "TT"]
