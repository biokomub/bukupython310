import re

text = "Belajar C++ bersama di sini amat menyenangkan"

print("Sebelum diganti: ", text)
print("Sesudah diganti: ", (re.sub("C\+\+", "Python", text)))