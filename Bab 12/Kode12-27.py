import re

kode_1 = re.findall("a*", "aaaaaaaaaaaa")
kode_2 = re.findall("a*?", "aaaaaaaaaaaa")

print("Hasil Greedy: ", kode_1)
print("Hasil Lazy: ", kode_2)