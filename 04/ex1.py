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
for i in range(len(numbers)):
    for b in boards:
        if(check_board(b, numbers[:i+1]) > 0):
            print(check_board(b, numbers[:i+1])*int(numbers[i]))
            exit()

