# Write your code here
import re
def is_valid_student_id(string):
    return re.fullmatch(r"(s|r|S|R)\d{7}", string)


print(is_valid_student_id("R1058961"))