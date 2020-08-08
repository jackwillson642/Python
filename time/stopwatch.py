import time


# Commandline based stopwatch

print("Press Enter to start and lap and Ctrl+c to end")

try:
    input()
    print("Started")
    stime = time.time()

    while True:
        input()
        etime = time.time()
        result = ("Time: %s" % (round((etime - stime), 3)))
        print(result)

except KeyboardInterrupt:
    print("\nEnded\n")
    etime = time.time()
    result = ("Time: %s" % (round((etime - stime), 3)))
    print(result)
