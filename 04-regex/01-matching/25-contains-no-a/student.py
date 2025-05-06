# Write your code here
import re
def contains_no_a(string):
    return re.fullmatch(r"[^a]*", string)


print(contains_no_a(""))
print(contains_no_a("brt"))