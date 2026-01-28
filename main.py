while free_hos:
        hos = free_hos[0]
        stu = hos_prefs[hos][next_proposal_index[hos]]
        next_proposal_index[hos] += 1

        if stu_matches[stu] is None:
            hos_matches[hos] = stu
            stu_matches[stu] = hos
            free_hos.pop(0)
        else:
            curr= stu_matches[stu]
            if stu_prefs[stu].index(hos) < stu_prefs[stu].index(curr):
                hos_matches[hos] = stu
                stu_matches[stu] = hos
                hos_matches[curr] = None
                free_hos.pop(0)
                free_hos.append(curr)

    return hos_matches[1:], stu_matches[1:]
