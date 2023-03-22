import re

text = "ggaagtataaaatcgtaaca"

A = "tata"
B = "aaa"

print(re.findall(A+B, text))