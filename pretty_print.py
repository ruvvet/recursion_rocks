# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# Write a function that accepts a complex dictionary
# and prints out all of it's keys and all of its values.
# The dictionary can have dictionaries nested inside of it
# 'dictionary' is the dictionary that's currently being iterated over.
# 'indent' is a string representing the current level of indentation
# ...
# pretty_print(inner_dictionary, indent + '..');
# ...

def pretty_print(dictionary, indent):
    # base case
    for k, v in sorted(dictionary.items(), key=lambda x: x[0]):
        if isinstance(v, dict):
            print(('.') * indent + (f'{k}:'))
            pretty_print(v, indent+1)
        else:
            print((".") * indent + f'{k}: {v}')


o1 = {"a": 1, "b": 2}
o2 = {"a": 1, "b": 2,
      "c": {"name": "Bruce Wayne", "occupation": "Hero"},
      "d": 4}
o3 = {"a": 1, "b": 2,
      "c": {"name": "Bruce Wayne", "occupation": "Hero", "friends": {
          "spiderman": {"name": "Peter Parker"},
          "superman": {"name": "Clark Kent"}}},
      "d": 4}


pretty_print(o3, 3)


# print(pretty_print(o1, "-"))
# print(pretty_print(o2, " "))
# print(pretty_print(o3, ".."))
# ..a: 1
# ..b: 2
# ..c:
# ....name: Bruce Wayne
# ....occupation: Hero
# ....friends:
# ......spiderman:
# ........name: Peter Parker
# ......superman:
# ........name: Clark Kent
# ..d: 4
