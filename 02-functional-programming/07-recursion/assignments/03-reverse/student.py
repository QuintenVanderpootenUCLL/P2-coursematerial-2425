def reverse_from_left(text):
    if text == "":
        return ""
    return text[0] + reverse_from_left(text[1:])

def reverse_from_right(text):
    if text == "":
        return ""
    return text[-1] + reverse_from_right(text[:-1])

text = "abcd"
print(reverse_from_left(text))  
print(reverse_from_right(text)) 
