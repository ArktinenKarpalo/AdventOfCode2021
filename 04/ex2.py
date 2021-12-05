import sys
input = sys.stdin.read().split("\n\n")
numbers = input[0].split(",")
boards = input[1:]
boards = list(map(lambda y: list(map(lambda x: x.split(), y.split("\n"))), boards))

def check_board(board, numbers):
    sm = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] not in numbers:
                 sm += int(board[i][j])
    for i in range(5):
        match1 = 0
        match2 = 0
        for j in range(5):
            if board[i][j] in numbers:
                match1 += 1
            if board[j][i] in numbers:
                match2 += 1
        if match1 == 5 or match2 == 5:
            return sm
    return 0
ans = 0
won = set()
for i in range(len(numbers)):
    for j in range(len(boards)):
        if(j not in won and check_board(boards[j], numbers[:i+1]) > 0):
            ans = check_board(boards[j], numbers[:i+1])*int(numbers[i])
            won.add(j)
print(ans)

