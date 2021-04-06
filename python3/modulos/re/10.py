import re

cad=input("> ")

n=re.findall(r"10",cad)
print(len(n))
