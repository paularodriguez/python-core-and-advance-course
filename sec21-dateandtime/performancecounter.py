import time

# returns the current time in seconds
startTime = time.perf_counter()

time.sleep(3)

endTime = time.perf_counter()

print("Execution time: ", endTime - startTime)