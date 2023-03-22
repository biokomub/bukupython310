from timeit import timeit

kode_1 = """
import re

re.findall("a*", "aaaaaaaaaaaa")
"""

kode_2 = """
import re

re.findall("a*?", "aaaaaaaaaaaa")
"""

if __name__ == "__main__":
    result1 = timeit(kode_1)
    result2 = timeit(kode_2)
    print("Waktu eksekusi Greedy: "+ str(result1) + " detik")
    print("Waktu eksekusi Lazy: "+ str(result2) + " detik")