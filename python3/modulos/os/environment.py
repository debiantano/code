import os

env=os.environ

for item in env:
    print(item, env[item])

print("\n")

print(env["PATH"])
os.system("echo $PATH")
