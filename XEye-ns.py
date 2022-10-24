#! /usr/bin/env python3

import subprocess
import re
import scapy.all as sc

print("\n\n\n\t\t\t\t\t\t[*] Welcome to XEye Network Scanner [*]")
print("\n\n\n[Info] --> With \"XEye-ns\" you can scan the network and find all the devices IPs and Mac addresses")
ipr = subprocess.getoutput("ip r | grep proto | cut -d\" \" -f1")
ipra = re.search(r"(?:\d{1,3}\.){3}\d{1,3}(?:/\d\d?)?",str(ipr)).group(0)
def scan(ip):
    print("\n-----------------------------------------------------------------------------------")
    print("\n[Working] --> XEye-ns is scanning your network subnet which is \""+ipra+"\" - Please wait .......")
    ipa = sc.ARP(pdst=ip)
    ipe = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    # sc.ls(sc.Ether())
    ipc = ipe/ipa
    # ipc.show()
    # print(ipc.summary())
    an = sc.srp(ipc,timeout=3,verbose=False)[0]
    # print(an.summary())
    for each in an:
        # print(each[1].show())
        print("\n\t\t\t\t\t\t[*] --> The IP: "+each[1].psrc +"\n\t\t\t\t\t\t[*] --> The Mac: "+each[1].hwsrc+"\n")
        print("\t\t\t\t\t\t--------------------------------------")
    TheEnd()
def checkpriv():
    who=subprocess.getoutput("whoami")
    checwho = re.search(r"root",str(who))
    if checwho is None:
        print("\n[Required] --> Please run the tool with \"sudo\" - Exiting ......")
    else:
        scan(ipra)
def TheEnd():
    print("\t\t\t\t[*] Thanks for using XEye-tp. Below are our Social Media OSINT Hacking bundle recommended for you :) [*]")
    print("\n [***] --> The Ultimate Social Media OSINT Hacking Bundle(70% OFF): https://rb.gy/sgxib8")
    print("*******************************************************************************************************")
    print("\n [Author] Eng.Mostafa Ahmad - Cybersecurity Expert and \"XEye\" founder.")
    print("\n [Author] --> ENG.Mostafa Ahmad - Cybersecurity Expert and XEye founder")
checkpriv()
