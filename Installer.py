import os
import fnmatch
import time
import urllib.request

import requests

print("What Server Would You Like To Install?\nA. Vanilla\nB. Forge\nC. Fabric")
version = input("Type A, B or C: ")

if version == "A":
    url = "https://piston-data.mojang.com/v1/objects/84194a2f286ef7c14ed7ce0090dba59902951553/server.jar"
    os.system(f"curl {url} server.jar -O server.jar")

    with open("eula.txt", "w+") as f2:
        f2.write("eula=True")
    ram = input("RAM (in GB): ")

    for file in os.listdir("."):
        if fnmatch.fnmatch(file, "minecraft_server.*.*.*.jar"):
            os.rename(file, "server.jar")

    with open("amber-cfg.txt", "w+") as f0:
        f0.write("ram: " + ram)

    print("Complete! Cleaning folder...")

    for file in os.listdir("."):
        if fnmatch.fnmatch(file, "*.*.*.json"):
            os.remove(file)
else:
    url = "https://meta.fabricmc.net/v2/versions/loader/1.20.1/0.14.22/0.11.2/server/jar"
    os.system(f"curl {url} server.jar -O server.jar")

    with open("eula.txt", "w+") as f2:
        f2.write("eula=True")
    ram = input("RAM (in GB): ")

    with open("amber-cfg.txt", "w+") as f0:
        f0.write("ram: " + ram)

    print("Complete! Cleaning folder...")

    for file in os.listdir("."):
        if fnmatch.fnmatch(file, "*.*.*.json"):
            os.remove(file)
