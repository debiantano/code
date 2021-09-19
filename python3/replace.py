import os

s=os.environ["PATH"]
s=s.replace(":", "\n")
print(s)
