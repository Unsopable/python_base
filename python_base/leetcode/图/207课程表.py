


prerequisites = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]

# dic = dict()
# for prerequisite in prerequisites:
#     # print(type(prerequisite))
#     for index,content in enumerate(prerequisite):
#         # print(index,content)
#         dic[content] = list(set(dic.get(content,[]) + prerequisite[:index]))

# print(type(dic))
# dic=sorted(dic.items(),key=lambda x:len(x[1])) ###[(3, []), (4, [1, 2]), (1, [3]), (2, [3])]

# dic = {val[0]:val[1] for val in dic}
# print(dic,type(dic)) ###{3: [], 4: [1, 2], 1: [3], 2: [3]} <class 'dict'>


# # numCourses = 5   
# for key,val in dic.items():
#     ### 如果字典的值为空，则表示这门课能学习
#     if not val:
#         # numCourses -= 1
#         ### 其他课，如果有val为前置课，就可以pop掉
#         # dic = { i:v.pop(key) for i,v in dic.items()}
#         for i,v in dic.items():
#             if key in v:
#                 v.remove(key)
#                 dic[i] = v
#         print("Sda   ",dic)
#     else:
#         continue
# # for val in dic.values:
# #     if val:
# #         # return false
# #         pass
# # return True    
# print(dic)   


# # print(numCourses-1)