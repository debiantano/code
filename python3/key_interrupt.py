import sys, time

try:
    for i in range(1,100):
        print(i)
        time.sleep(1)

except KeyboardInterrupt:
    sys.exit(1)
