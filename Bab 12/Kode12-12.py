import re

text = """
Pada sel normal, p53 diinaktivasi oleh negative regulator mdm2,\n
suatu E3 ubiquitin ligase. Jika sel terpapar oleh faktor stres\n
baik fisika maupun kimia dengan jumlah tertentu,\n
kompleks p53-mdm2 akan terdisosiasi oleh pathway tertentu,\n
sehingga p53 menjadi aktif.  
"""

print(re.findall("mdm2...s", text, flags = re.DOTALL))
print(re.findall("stres..ba", text, flags = re.DOTALL))
print(re.findall("tentu,..ko", text, flags = re.DOTALL))
print(re.findall("tentu,..se", text, flags = re.DOTALL))