import re

text = "ggaag tataa aatgg taaca"

print(re.findall("(tataa|aatgg)", text))