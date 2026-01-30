def gale_shapley(n, hos_prefs, stu_prefs):
    if n == 0 or not hos_prefs or not stu_prefs:
        return []

    if len(hos_prefs) != n or len(stu_prefs) != n:
        raise ValueError("Number of hospitals and students does not match the length of their preference lists.")

    for i, prefs in enumerate(hos_prefs, 1):
        if sorted(prefs) != list(range(1, n + 1)):
            raise ValueError(f"Hospital {i} preference list does not contain all students exactly once.")

    for i, prefs in enumerate(stu_prefs, 1):
        if sorted(prefs) != list(range(1, n + 1)):
            raise ValueError(f"Student {i} preference list does not contain all hospitals exactly once.")
        
    if n == 1:
        return [1]
    
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


if __name__ == "__main__":
    test_cases = read_input("input.txt")
    results = []

    for n, hos_prefs, stu_prefs in test_cases:
        matches = gale_shapley(n, hos_prefs, stu_prefs)
        results.append(matches)

    write_output("output.txt", results)
