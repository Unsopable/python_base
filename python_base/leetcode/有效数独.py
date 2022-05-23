def ans():
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    ####### 三个部分 [行，列，九宫格]
    col = [[] * 9 for k in range(9)]
    row = [[] * 9 for k in range(9)]
    box = [[] * 9 for k in range(9)]

    ###### i 为行坐标，j 为纵坐标
    for i in range(9):
        for j in range(9):
            #### 坐标点 对应 的字符
            temp = board[i][j]
            #### 判断字符是否是数字，如果 是 则添加到三个部分中，否则继续
            if not temp.isdigit():
                continue
            #### 如果 该数 在部分里则 返回 False
            if temp in col[i]:
                return False
            if temp in row[j]:
                return False
            if temp in box[(j // 3) * 3 + (i // 3)]:
                return False

            col[i].append(temp)
            row[j].append(temp)
            box[(j // 3) * 3 + (i // 3)].append(temp)
    return True