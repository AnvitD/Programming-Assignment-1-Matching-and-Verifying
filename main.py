def gale_shapley(n, hos_prefs, stu_prefs):

    hos_prefs = [None] + hos_prefs
    stu_prefs = [None] + stu_prefs

    hos_matches = [None] * (n + 1)
    stu_matches = [None] * (n + 1)
    free_hos = list(range(1, n + 1))
    next_proposal_index = [0] * (n + 1)

    while free_hos:
        hos = free_hos[0]
        stu = hos_prefs[hos][next_proposal_index[hos]]
        next_proposal_index[hos] += 1

        if stu_matches[stu] is None:
            hos_matches[hos] = stu
            stu_matches[stu] = hos
            free_hos.pop(0)
        else:
            curr = stu_matches[stu]
            if stu_prefs[stu].index(hos) < stu_prefs[stu].index(curr):
                hos_matches[hos] = stu
                stu_matches[stu] = hos
                hos_matches[curr] = None
                free_hos.pop(0)
                free_hos.append(curr)

    return hos_matches[1:] 


def read_input(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    index = 0
    test_cases = []

    while index < len(lines):
        n = int(lines[index])
        index += 1

        hos_prefs = []
        stu_prefs = []

        for _ in range(n):
            hos_prefs.append(list(map(int, lines[index].split())))
            index += 1

        for _ in range(n):
            stu_prefs.append(list(map(int, lines[index].split())))
            index += 1

        test_cases.append((n, hos_prefs, stu_prefs))

    return test_cases


def write_output(filename, results):
    with open(filename, "w") as f:
        for case_index, matches in enumerate(results):
            for i, s in enumerate(matches, start=1):
                f.write(f"{i} {s}\n")
            if case_index != len(results) - 1:
                f.write("\n") 


test_cases = read_input("example.txt")
results = []

for n, hos_prefs, stu_prefs in test_cases:
    matches = gale_shapley(n, hos_prefs, stu_prefs)
    results.append(matches)

write_output("output.txt", results)

def verify(input_file, output_file):
    test_cases = read_input(input_file)

    out = []
    for line in open(output_file, "r"):
        out.append(line.strip())

    j = 0

    for case_num in range(len(test_cases)):
        n, hos_prefs, stu_prefs = test_cases[case_num]

        while j < len(out) and out[j] == "":
            j += 1

        matches = [0] * n
        for _ in range(n):
            h, s = map(int, out[j].split())
            j += 1
            matches[h - 1] = s

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

        if valid and stable:
            print("Case", case_num + 1, "PASS (valid + stable)")
        elif valid and (not stable):
            print("Case", case_num + 1, "FAIL (valid + NOT stable)")
        else:
            print("Case", case_num + 1, "FAIL (NOT valid + NOT stable)")


verify("example.txt", "output.txt")
