def ans():
    s = "leetcode"
    list_s = list(s)
    s_copy = list_s.copy()
    set_s = sorted(set(list_s), key=list_s.index)
    for v in set_s:
        s_copy.remove(v)
        if v in s_copy:
            continue
        else:
            return list_s.index(v)
    return -1
print(ans())