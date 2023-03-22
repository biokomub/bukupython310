import re

text = """
Tiga puluh menit aku disini,
Kamu ada dimana? Hei!
Aih, sorry. Macet tadi.
"""

print(re.findall("^Ti", text, flags = re.MULTILINE))
print(re.findall("Hei!$", text, flags = re.MULTILINE))
print(re.findall("di.$", text, flags = re.MULTILINE))