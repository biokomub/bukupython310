#berpindah direktori kerja 

import os

curr_dir = os.getcwd()
ch_dir = "E:\\NEW PROJECTS\\BUKU 310\\Material"
os.chdir(ch_dir)
curr_dir_now = os.getcwd()

print("Direktori kerja saat ini adalah:", curr_dir)
print("Pindah ke:", ch_dir)
print("Direktori kerja saat ini adalah:", curr_dir_now)