import re

string = "Two too."


matchs = re.findall("t[ow]o", string, re.IGNORECASE)

print(matchs)
