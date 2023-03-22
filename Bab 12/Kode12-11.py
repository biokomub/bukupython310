import re

text = """
Pada sel normal, p53 diinaktivasi oleh negative regulator mdm2,
suatu E3 ubiquitin ligase. Jika sel terpapar oleh faktor stres
baik fisika maupun kimia dengan jumlah tertentu,
kompleks p53-mdm2 akan terdisosiasi oleh pathway tertentu,
sehingga p53 menjadi aktif.  
"""

print(re.findall("akti.", text))
print(re.findall("akti..", text))
print(re.findall("akti..si", text))
print(re.findall("ak..si", text))