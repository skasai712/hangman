import re

string = "__one__ __two__ __three__"


matchs = re.findall("__.*?__", string, re.IGNORECASE)


print(matchs)

for match in matchs:
	print(match)
