import re

text = "Halo semua! Selamat datang di World Cup 2022!"
x = re.search("2022", text) 

print("Text: ", text)
print("Span letak karakter:", x.span()) 
print("Letak karakter awal", x.start())
print("Letak karakter akhir:", x.end()) 