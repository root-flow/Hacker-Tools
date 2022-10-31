#!/usr/bin/env python



import os



os.system("apt-get install figlet")

os.system("clear")

os.system("figlet FLOW")

os.system("figlet VPN KONTROL ARACI")



print("""



Vpn kontrol aracı aracına Hoş geldiniz :)



""")



hedefip=input("Hedef ip : ")

os.system("ike-scan "+hedefip)
