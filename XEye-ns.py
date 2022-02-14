#! /usr/bin/env python3

import argparse
import scapy.all as sc

print("---------------------------------------------------------")
print(" \n[Welcoming] --> Welcome to XEye Network Scanner \n")
print(" [Info] --> This is a simple network scanner to get the hosts that are up and their Mac addresses\n\n")

def args():
    opts = argparse.ArgumentParser()
    opts.add_argument("-t","--target",dest="the_target",help="The target IP or Ip range")
    ip = opts.parse_args()
    if ip.the_target:
        scanning(ip.the_target)
    else:
        print(" [Info] --> Entering the interactive mode ")
        interct()
def interct():
    ip = input(" [Required] --> Enter the network range: ")
    if ip:
        scanning(ip)
    else:
        print(" [Warning] --> No Entry ")
        exit()
def scanning(ip):
    target = sc.ARP(pdst=ip)
    destmac = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    comb = destmac/target
    gotten = sc.srp(comb,timeout=3,verbose=False)[0]
    ips = []
    for el in gotten:
        gottenips = {"ips":el[1].psrc,"mac":el[1].hwsrc}
        ips.append(gottenips)
        #print("---------------------------------------------------------")
    printr(ips)
def printr(ipss):
    print("\n The IP \t\t The Mac Address\n ---------------------------------------------------------\n")
    for nn in ipss:
        print(nn["ips"]+"\t\t"+nn["mac"])
args()

