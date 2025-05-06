# Write your code here
import re
def is_number(string):
    return re.fullmatch("\d+(\.?\d+)?", string)


print(is_number("12."))
