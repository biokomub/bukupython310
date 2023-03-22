import re

text1 = "aaaaat"
text2 = "aaaaatt"
text3 = "aaaaattttt"
text4 = "aaaaattttt"
text5 = "aaaaaaaaaa"
text6 = "kodon nukelotida"

print(re.findall("a+t", text1))
print(re.findall("at+", text2))
print(re.findall("at+", text3))
print(re.findall("at+?", text4))
print(re.findall("at+", text5))
print(re.findall("[a-t]+", text6))
print(re.findall("[a-z]+", text6))