import random
import time
import matplotlib.pyplot as plt
from main import gale_shapley


def generate_random_preferences(n):
    hos_prefs = [random.sample(range(1, n + 1), n) for _ in range(n)]
    stu_prefs = [random.sample(range(1, n + 1), n) for _ in range(n)]
    return hos_prefs, stu_prefs


def verify_one(n, hos_prefs, stu_prefs, matches):

    valid = True
    seen = [0] * (n + 1)

    for h in range(1, n + 1):
        s = matches[h - 1]
        if s < 1 or s > n:
            valid = False
        else:
            seen[s] += 1

    for s in range(1, n + 1):
        if seen[s] != 1:
            valid = False

    stu_match = [0] * (n + 1)
    if valid:
        for h in range(1, n + 1):
            stu_match[matches[h - 1]] = h

    stable = True
    if valid:
        for h in range(1, n + 1):
            curr_s = matches[h - 1]

            for s in hos_prefs[h - 1]:
                if s == curr_s:
                    break

                curr_h = stu_match[s]

                if stu_prefs[s - 1].index(h) < stu_prefs[s - 1].index(curr_h):
                    stable = False

    return valid and stable


def measure_verify_runtime(n):
    hos_prefs, stu_prefs = generate_random_preferences(n)

    matches = gale_shapley(n, hos_prefs, stu_prefs)

    start_time = time.perf_counter()
    ok = verify_one(n, hos_prefs, stu_prefs, matches)
    end_time = time.perf_counter()

    return end_time - start_time


ns = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
runtimes = []

for n in ns:
    runtime = measure_verify_runtime(n)
    print(f"n={n}, verify_runtime={runtime:.6f} sec")
    runtimes.append(runtime)

plt.plot(ns, runtimes, marker='o')
plt.xlabel("Number of hospitals/students (n)")
plt.ylabel("Verifier running time (seconds)")
plt.title("Verifier Scalability")
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.show()
