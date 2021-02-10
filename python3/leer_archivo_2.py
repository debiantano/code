filename="test.txt"

with open(filename) as f_obj:
    lines=f_obj.readlines()
    print(lines)

for i in lines:
    print(i.rstrip())
