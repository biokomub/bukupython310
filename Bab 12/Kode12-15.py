import re

text = """
Sagittarius A*, adalah lubang hitam super masif,
yang terletak di pusat Galaksi Bima Sakti. 
Letaknya sekitar 26.673 ± 42 tahun cahaya dari bumi.
"""

print(re.findall("*", text))