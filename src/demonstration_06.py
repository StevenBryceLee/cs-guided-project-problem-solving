"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def get_count(input_str):
    vowels = ['a','e','i','o','u']
    return sum([1 if char in vowels else 0 for char in input_str])

print(get_count('aaaaa'))
print(get_count('yyyyy'))
print(get_count('aqaq'))

