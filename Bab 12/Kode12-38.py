import re

text = "Halo bapak, halo ibu! Selamat datang di World Cup 2022!"
match = re.findall("[H|h]..o", text) 

print(match) 