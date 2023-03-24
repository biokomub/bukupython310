#contoh match... case...

Nucleobase = "Z"
match Nucleobase:
    case "A":
       print("Adenine")
    case "T":
       print("Thymine")
    case "C":
        print("Cytosine")
    case "G":
        print("Guanine")
    case "U":
        print("Uracil")
    case _:
        print("Bukan nucleobase")

print("Ini diluar match... case...")