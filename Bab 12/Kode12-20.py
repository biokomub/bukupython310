import re

text1 = "y"
text2 = "ye"
text3 = "yes"
text4 = "yessssss"
text5 = ""


print(re.findall("yes?", text1))
print(re.findall("yes?", text2))
print(re.findall("yes?", text3))
print(re.findall("yes?", text4))
print(re.findall("yes?", text5))