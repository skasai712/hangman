import re

string = "123 hi 34 hello."


matchs = re.findall("\d", string, re.IGNORECASE)


print(matchs)
