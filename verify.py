def read_input(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    if len(lines) == 0:
        return [], "missing input value"

    index = 0
    test_cases = []

    while index < len(lines):
        n = int(lines[index])
        index += 1

        hos_prefs = []
        stu_prefs = []

        for _ in range(n):
            if index >= len(lines):
                return [], "missing input value"
            if len(lines[index].split()) != n:
                return [], "missing input value"
            hos_prefs.append(list(map(int, lines[index].split())))
            index += 1

        for _ in range(n):
            if index >= len(lines):
                return [], "missing input value"
            if len(lines[index].split()) != n:
                return [], "missing input value"
            stu_prefs.append(list(map(int, lines[index].split())))
            index += 1

        test_cases.append((n, hos_prefs, stu_prefs))

    return test_cases, ""


def verify(input_file, output_file):
    test_cases, input_reason = read_input(input_file)
    if input_reason != "":
        print(f"INVALID ({input_reason})")
        return

    out = []
    for line in open(output_file, "r"):
        out.append(line.strip())

    j = 0

    for case_num in range(len(test_cases)):
        n, hos_prefs, stu_prefs = test_cases[case_num]

        while j < len(out) and out[j] == "":
            j += 1

        matches = [0] * n
        seen_h = [0] * (n + 1)

        valid = True
        stable = True
        reason = ""
        blocking_pair = None

        for _ in range(n):
            if j >= len(out):
                valid = False
                reason = "missing output value"
                break

            parts = out[j].split()
            if len(parts) != 2:
                valid = False
                reason = "missing output value"
                break

            h, s = map(int, parts)
            j += 1

            if h < 1 or h > n:
                valid = False
                reason = "hospital out of range"
                break
            if seen_h[h] == 1:
                valid = False
                reason = "duplicate hospital"
                break

            seen_h[h] = 1
            matches[h - 1] = s

        if valid:
            for h in range(1, n + 1):
                if seen_h[h] != 1:
                    valid = False
                    reason = "duplicate hospital"
                    break

        if valid:
            seen_s = [0] * (n + 1)
            for h in range(1, n + 1):
                s = matches[h - 1]
                if s < 1 or s > n:
                    valid = False
                    reason = "student out of range"
                    break
                seen_s[s] += 1

            if valid:
                for s in range(1, n + 1):
                    if seen_s[s] != 1:
                        valid = False
                        reason = "duplicate/missing student"
                        break

        if valid:
            stu_match = [0] * (n + 1)
            for h in range(1, n + 1):
                stu_match[matches[h - 1]] = h

            for h in range(1, n + 1):
                curr_s = matches[h - 1]

                for s in hos_prefs[h - 1]:
                    if s == curr_s:
                        break

                    curr_h = stu_match[s]
                    if stu_prefs[s - 1].index(h) < stu_prefs[s - 1].index(curr_h):
                        stable = False
                        blocking_pair = (h, s)
                        break

                if not stable:
                    break

        if not valid:
            print(f"INVALID ({reason})")
        elif stable:
            print("VALID STABLE")
        else:
            bh, bs = blocking_pair
            print(f"UNSTABLE (blocking pair: {bh} {bs})")


if __name__ == "__main__":
    verify("input.txt", "output.txt")
