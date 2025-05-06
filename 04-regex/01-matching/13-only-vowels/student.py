# Write your code here
import re
def only_vowels(string):
    return re.fullmatch(r"(a|e|i|o|u)*", string)

print(only_vowels(''))
print(only_vowels("aeiou"))