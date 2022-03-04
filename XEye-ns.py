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
    print("\n[Working] --> XEye-ns is scanning your network subnet which is \""+ipra+"\"")
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
    print("\n\t\t\t\t[*] Thanks for using XEye-ns. Below are recommended courses for you :) [*]")
    print("\n\n\n --> The Facebook OSINT Hacking course: https://www.udemy.com/course/facebook-osint-hacking/?referralCode=1FEF1A87D703B6DAE484")
    print("\n --> The Kali Linux Command course: https://www.udemy.com/course/linux-command-lines-from-a-hackers-perspective/?referralCode=62A07A01780C21117592")
    print("\n---------------------------------------------------------")
    print("\n [Author] --> ENG.Mostafa Ahmad - Cybersecurity Expert and XEye founder")
checkpriv()
