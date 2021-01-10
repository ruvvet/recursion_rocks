# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the largest number in a given array.

def find_max(list):
    # base case
    if len(list) == 1:
        return list[0]
    return max(list[0], find_max(list[1:]))


print(find_max([1, 4, 45, 6, -50, 10, 2]))

# print(find_max([1, 4, 45, 6, -50, 10, 2]))
# => 45
