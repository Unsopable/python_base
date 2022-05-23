# def a(s):
#     if len(s) == 1:
#         return s
#     length = len(s)
#     sum_gather = []
#     numbers = []
#     ##i指针指头部
#     for i in range(length):
#         char_start = s[i]
#         for j in range(i+1, length):
#             char_end= s[j]
#             ##如果现在 尾字符 与 头字符相等，推出内循环，则是回文数，推出
#             if char_start == char_end:
#                 item = s[i:j+1]
#                 sum_gather.append(item)
#                 numbers.append(len(item))
#                 break
#
#     if not numbers:
#         return s[0]
#     else:
#         max_index = numbers.index(max(numbers))
#         return sum_gather[max_index]
#
# res = a("aacabdkacaa")
# print(res)


# def b(s):
#     n = len(s)
#
#     def findbound(l, r):
#         while l >= 0 and r < n and s[l] == s[r]:
#             l -= 1
#             r += 1
#         return l + 1, r - 1
#
#     left, right = 0, 0
#     for i in range(n):
#         l_1, r_1 = findbound(i, i)
#         l_2, r_2 = findbound(i, i + 1)
#         if r_1 - l_1 > right - left:
#             left, right = l_1, r_1
#         if r_2 - l_2 > right - left:
#             left, right = l_2, r_2
#
#     return s[left: right + 1]
# res = b("aacabdkacaa")
# print(res)

def c(s):
    n = len(s)
    # 最大回文字符串得长度
    left, right = (0, 0)
    max_len = 1
    if n == 1:
        return s
    dp = [[False] * n for i in range(n)]
    ###dp[i][j]==True 表示 s[i]到s[j]字符串为回文串
    for j in range(n):
        dp[j][j] = True
    # print(dp)
    # 左右指针
    for r in range(n):
        for l in range(r):
            ###判断左右指针中得字符串是否为回文串（两边字符一样，且两端得中间字符串为回文串）
            ##如果符合条件，将dp中对应得位置变为True
            if s[r] == s[l] and (dp[l + 1][r - 1] or (r - l + 1 <= 3)):
                dp[l][r] = True
                if r - l + 1 > max_len:
                    max_len = r - l + 1
                    right = r
                    left = l
    print(dp)
    return s[left:right + 1]


res = c("aaaa")
print(res)
