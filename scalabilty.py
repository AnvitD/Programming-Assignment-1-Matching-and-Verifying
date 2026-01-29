import random
from main import gale_shapley
import time
import matplotlib.pyplot as plt

n = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]


def generate_random_preferences(n):
    hos_prefs = [random.sample(range(1, n+1), n) for _ in range(n)]
    stu_prefs = [random.sample(range(1, n+1), n) for _ in range(n)]
    return hos_prefs, stu_prefs


def measure_runtime(n):
    hos_prefs, stu_prefs = generate_random_preferences(n)
    
    start_time = time.time()
    matches = gale_shapley(n, hos_prefs, stu_prefs)
    end_time = time.time()
    
    return end_time - start_time


ns = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
runtimes = []

for n in ns:
    runtime = measure_runtime(n)
    print(f"n={n}, runtime={runtime:.6f} sec")
    runtimes.append(runtime)

plt.plot(ns, runtimes, marker='o')
plt.xlabel("Number of hospitals/students (n)")
plt.ylabel("Running time (seconds)")
plt.title("Gale-Shapley Matching Engine Scalability")
plt.xscale('log') 
plt.yscale('log')  
plt.grid(True)
plt.show()

