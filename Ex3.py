import statistics
from random import randint
results = []
for i in range(1000):
    a = randint(1,6)
    b = randint(1,6)
    results.append(a+b)
print("--- Simulation Results (1000 rolls) ---")
print(f"Mean: {statistics.mean(results)}")
print(f"Median: {statistics.median(results)}")
print(f"Mode: {statistics.mode(results)}")