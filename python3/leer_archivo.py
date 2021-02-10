filename="test.txt"

with open(filename) as f_obj:
    for line in f_obj:
        print(line.rstrip())
