#### (判断字符 是否 是 字母 或 数字字符) [.isalpha()；.isdigit()]
s = "0P"
s = s.lower()
s_list = []
for pat_s in s:
    if pat_s.isalpha() or pat_s.isdigit():
        s_list.append(pat_s)
rev_list = s_list[::-1]
if rev_list == s_list:
    print(True)
else:
    print(False)