import os
import fnmatch
import time
import urllib.request

import requests

print("What Server Would You Like To Install?\nA. Vanilla\nB. Forge\nC. Fabric")
version = input("Type A, B or C: ")

if version == "A":
    url = "https://piston-data.mojang.com/v1/objects/84194a2f286ef7c14ed7ce0090dba59902951553/server.jar"
    os.system("curl " + url + " server.jar -O server.jar")

    f2 = open("eula.txt", "w+")
    f2.write("eula=True")
    f2.close()
    ram = input("RAM (in GB): ")

    for file in os.listdir("."):
        if fnmatch.fnmatch(file, "minecraft_server.*.*.*.jar"):
            os.rename(file, "server.jar")

    f0 = open("amber-cfg.txt", "w+")
    f0.write("ram: " + ram)
    f0.close()

    print("Complete! Cleaning folder...")

    for file in os.listdir("."):
        if fnmatch.fnmatch(file, "*.*.*.json"):
            os.remove(file)
else:
    url = "https://meta.fabricmc.net/v2/versions/loader/1.20.1/0.14.22/0.11.2/server/jar"
    urllib.request.urlretrieve(url, "server.jar")

    f2 = open("eula.txt", "w+")
    f2.write("eula=True")
    f2.close()
    ram = input("RAM (in GB): ")

    f0 = open("amber-cfg.txt", "w+")
    f0.write("ram: " + ram)
    f0.close()

    print("Complete! Cleaning folder...")

    for file in os.listdir("."):
        if fnmatch.fnmatch(file, "*.*.*.json"):
            os.remove(file)