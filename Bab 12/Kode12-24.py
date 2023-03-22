import re

text = "aaaaaat"

print(re.findall("a{4,6}", text))