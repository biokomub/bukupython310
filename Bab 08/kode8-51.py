ks = ["N7", "N5", "EN2"]
nb = ["Bacillus sp.", "Lysinibacillus sp."]
ls = ["Ayutthaya", "Ayutthaya", "Bangkok"]

tbl= zip(ks, nb, ls, strict = True)

for ks, nb, ls in tbl:
    print(f"{ks} {nb} {ls}")