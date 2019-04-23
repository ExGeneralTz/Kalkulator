#!/usr/bin/python
import os

print ("\033[36;1m########################################")
print ("\033[37;1m          Variable Pengurangan          ")
print ("\033[36;1m########################################")
os.system("date")
print (" ")

#MemintaInputKepadaUser
angka1 = input('\033[33;1mMasukan Bilangan Ke-1 : ')
angka2 = input('\033[33;1mMasukan Bilangan Ke-2 : ')

hasil = float(angka1) - float(angka2)

print ('\033[36;1mJawaban Anda Adalah =',hasil)
