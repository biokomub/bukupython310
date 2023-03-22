import re

text = "Halo bapak, halo ibu! Selamat datang di World Cup 2022!"
regex = re.compile("[H|h]..o") 
match = regex.findall(text) 

print(match) 