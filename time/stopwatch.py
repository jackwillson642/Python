# This is a program of a simple stopwatch using the time module

import time as t # Here time is imported as t meaning that instead of 'time', I only have to type 't'

print("press ENTER to start and lap and Ctrl+C to end")

try:
    input() # Checking for ENTER
    startTime = t.time()
    while True:
        input() # Checking for ENTER
        lapTime = t.time()
        print(round(lapTime - startTime, 2)) # Round is used to round to 2 decimal places
except KeyboardInterrupt: # If Ctrl+C is presed
    endTime = t.time()
    print("\nTime: " + str(round(endTime - startTime, 2))) # Again round is used for the same reason
