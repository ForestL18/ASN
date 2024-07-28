'''
Author: Vincent Young
Mender: ForestL18
Date: 2022-11-17 02:29:30
LastEditors: ForestL18
LastEditTime: 2024-07-28 21:23:30
FilePath: /ASN/scripts/ChinaASN.py
Telegram: https://t.me/missuo

Copyright © 2022 by Vincent, All Rights Reserved. 
'''
import requests
from lxml import etree
import time

def initFile():
    localTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open("China-ASN.list", "w") as asnFile:
        asnFile.write("# ASN Information in China. (https://github.com/ForestL18/ASN) \n")
        asnFile.write("# Last Updated: UTC " + localTime + "\n")
        asnFile.write("# Made by Vincent, All rights reserved. " + "\n")
        asnFile.write("# Mended by ForestL18, All rights reserved. " + "\n\n")

def saveLatestASN():
    url = "https://bgp.he.net/country/CN"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    r = requests.get(url = url, headers = headers).text
    tree = etree.HTML(r)
    asns = tree.xpath('//*[@id="asns"]/tbody/tr')
    initFile()
    for asn in asns:
        asnNumber = asn.xpath('td[1]/a')[0].text.replace('AS','')
        asnName = asn.xpath('td[2]')[0].text
        if asnName != None:
            asnInfo = "IP-ASN,{}".format(asnNumber)
            with open("China-ASN.list", "a") as asnFile:
                asnFile.write(asnInfo)
                asnFile.write("\n")

saveLatestASN()
