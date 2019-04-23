#!/usr/bin/python

import os

#############################
#          Menu

print ("\033[36;1m#########################################")
print ("\033[36;1m# \033[37;1mCommand              Information     \033[36;1m #")
print ("\033[36;1m#########################################")
print (" ")
print ("  1>>tb               Variabel Penambahan ")
print ("  2>>kr               Variabel Pengurangan ")
print ("  3>>bg               Variabel Pembagian  ")
print ("  4>>x                Variabel Perkalian  ")
print ("  5>>about            Show About Author   ")
print ("  99>>exit            Exit The Program    ")
print (" ")
menu = input("insm >> ")

if menu==1:
    os.system('cd Kalkulator')
    os.system('python tambah.py')

if menu==2:
    os.system('cd Kalkulator')
    os.systen('python kurang.py')

if menu==3:
    os.system('cd Kalkulator')
    os.systen('python bagi.py')

if menu==4:
    os.system('cd Kalkulator')
    os.system('python kali.py')

if menu==5:
    print (' Author      : Andhika Adi Saputra')
    print (' Code name   : ExGeneralTz        ')
    print (' Team        : Insomnia Cyber Team')
    print (' Github      : https://github.com/ExGeneralTz')

if menu==99:
    os.system('exit')
