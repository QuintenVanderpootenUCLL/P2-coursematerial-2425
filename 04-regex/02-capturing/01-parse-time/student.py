import re
def parse_time(string):
    parse = re.fullmatch(r"(\d{2}):(\d{2}):(\d{2})(\.\d{3})?", string)
    last = 0
    if parse == None:
        return None
    if parse.group(4):
        last = int(parse.group(4)[1:])
    return (int(parse.group(1)), int(parse.group(2)), int(parse.group(3)), last)

print(parse_time("11:12:13"))