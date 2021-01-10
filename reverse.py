# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# Write a recursive function called `reverse`
# that accepts a ss and returns a reversed ss.


def reverse(ss):
    current = ''

    def add_to_end(s, current):

        if len(s) == 1:
            print('last', s[0] + current)
            return s[0] + current

        current = s[0] + current
        add_to_end(s[1:], current)

    add_to_end(ss, current)


print(reverse('hello'))


# print(reverse(""))
# => ""
# print(reverse("a"))
# => "a"
# print(reverse("ab"))
# => "ba"
# print(reverse("computer"))
# => "retupmoc"
# print(reverse(reverse("computer")))
# => "computer"
