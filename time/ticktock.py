import sys
import time as t

c=0
try:
    while True:
        c = c+1
        print("Tick")
        t.sleep(1)
        c = c+1
        print("Tock")
        t.sleep(1)
except KeyboardInterrupt:
    print("\nIt has been %d seconds since you started this program" % c)
    sys.exit()
