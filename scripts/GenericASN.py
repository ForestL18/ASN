import requests
from lxml import etree
import time
import os

# 自定义关键词列表
keywords = ["Google", "Twitter", "Facebook", "Netflix", "Telegram"]

# 创建 GenericASN 文件夹
if not os.path.exists("GenericASN"):
    os.makedirs("GenericASN")

def initFile(keyword):
    localTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(f"GenericASN/{keyword}-ASN.list", "w") as asnFile:
        asnFile.write(f"// {keyword} ASN Information. (https://github.com/ForestL18/ASN) \n")
        asnFile.write("// Last Updated: UTC " + localTime + "\n")
        asnFile.write("// Made by Vincent, Modified by Forest, All rights reserved. " + "\n\n")

def saveASN(keyword):
    url = f"https://bgp.he.net/search?search%5Bsearch%5D={keyword}&commit=Search"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }
    r = requests.get(url=url, headers=headers).text
    tree = etree.HTML(r)
    asns = tree.xpath('//*[@id="search"]/table/tbody/tr')
    initFile(keyword)
    for asn in asns:  # No need to skip header row as it's part of tbody
        asnNumber = asn.xpath('td[1]/a')[0].text
        asnDescription = asn.xpath('td[3]')[0].text
        if asnNumber and asnNumber.startswith("AS"):  # Check if asnNumber starts with "AS"
            asnInfo = "IP-ASN,{}".format(asnNumber.replace('AS', ''))
            with open(f"GenericASN/{keyword}-ASN.list", "a") as asnFile:
                asnFile.write(asnInfo)
                asnFile.write("\n")

# 依次处理每个关键词
for keyword in keywords:
    saveASN(keyword)
