import re

text = "Halo semua, Apa kabar?"

print(re.findall("[^abcde]", text))