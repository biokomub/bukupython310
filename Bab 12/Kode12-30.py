import re

text = """
Ini caret (^)
Ini dolar ($)
Perhatikan tanda – tanda ini. 
"""

print(re.findall("\^", text))
print(re.findall("\$", text))