"""
백트래킹 왤케 어려운가
참조 : https://www.acmicpc.net/board/view/81589
"""
empty = []
board = []
for i in range(9):
    tmp = list(map(int, input().split()))
    for j in range(9):
        if tmp[j] == 0:
            empty.append((i, j))
    board.append(tmp)


def check(i, j, val):
    # side중복 있는지
    for z in range(9):
        if j != z and board[i][z] == val:
            return False
        # topdown중복 있는지
        if i != z and board[z][j] == val:
            return False
    # 3x3중복 있는지
    ri = i//3
    rj = j//3
    for y in range(ri*3, ri*3+3):
        for x in range(rj*3, rj*3+3):
            if [y, x] != [i, j] and board[y][x] == val:
                return False
    return True


def backTracking(oi):
    if len(empty) == oi:
        for _ in board:
            print(" ".join(map(str, _)))
        exit()
    # 검토 안되면 return false
    for z in range(1, 10):
        i, j = empty[oi]
        if check(i, j, z) == False:
            continue
        board[i][j] = z
        backTracking(oi+1)
        board[i][j] = 0


backTracking(0)

"""empty = []
board = []
for i in range(9):
    tmp = list(map(int, input().split()))
    for j in range(9):
        if tmp[j] == 0:
            empty.append((i, j))
    board.append(tmp)


def findCandidate():
    print("cndd")


def checkTopDown(board, i, j):
    tmp = [0 for i in range(9)]
    for z in range(9):
        if board[z][j] != 0:
            tmp[board[z][j]-1] = 1
    result = []
    for z in range(9):
        if tmp[z] == 0:
            result.append(z+1)
    return result


def checkSide(board, i, j):
    tmp = [0 for i in range(9)]
    for z in range(9):
        if board[i][z] != 0:
            tmp[board[i][z]-1] = 1
    result = []
    for z in range(9):
        if tmp[z] == 0:
            result.append(z+1)
    return result


def checkBlock(board, i, j):
    ri = i//3
    rj = j//3
    tmp = [0 for i in range(9)]
    for i in range(ri*3, ri*3+3):
        for j in range(rj*3, rj*3+3):
            if board[i][j] != 0:
                tmp[board[i][j]-1] = 1
    result = []
    for i in range(9):
        if tmp[i] == 0:
            result.append(i+1)
    return result

    # 후보군 찾아서 적용하기
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            print(i, j)
            print("ch side:", checkSide(board, i, j))
            print("ch topdown:", checkTopDown(board, i, j))
            print("ch block:", checkBlock(board, i, j))
            print()
"""
