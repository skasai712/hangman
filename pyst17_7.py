import re

string = "The ghost that says boo haunts the loo"


matchs = re.findall(".oo", string, re.IGNORECASE)


print(matchs)

for match in matchs:
	print(match)
