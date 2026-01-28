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
            curr= stu_matches[stu]
            if stu_prefs[stu].index(hos) < stu_prefs[stu].index(curr):
                hos_matches[hos] = stu
                stu_matches[stu] = hos
                hos_matches[curr] = None
                free_hos.pop(0)
                free_hos.append(curr)

    return hos_matches[1:], stu_matches[1:]

print(gale_shapley( 3,
    [[1,2,3], 
     [2,3,1], 
     [2,1,3]], 
    [[2,1,3],  
     [1,2,3],  
     [1,2,3]]
))  
