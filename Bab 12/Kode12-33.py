import re

text = "world123"

print(re.findall("(?![a-z]).*", text))