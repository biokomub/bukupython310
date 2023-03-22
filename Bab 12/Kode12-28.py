import re

text = """
Tiga puluh menit aku disini,
Kamu ada dimana? Hei!
Aih, sorry. Macet tadi.
"""

print(re.findall("^Ti", text))
print(re.findall("Hei!$", text))
print(re.findall("di.$", text))