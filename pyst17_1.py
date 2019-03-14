import re

l = "Beautiful is better than ugly."
matchs = re.findall("beautiful", l, re.IGNORECASE)

print(matchs)
