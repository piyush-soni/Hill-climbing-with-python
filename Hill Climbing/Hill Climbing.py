import random

# this parameter is used to check if the code is stuck on a local minima
Repeat = 0

# this function is to calculate the heuristic value of the board
def kills(board):
    v = 0
    for i in range(size):
        for j in range(i+1,size):
            # for in line collision
            if(board[i] == board[j]):
                v+=1
            # for diagonall collision
            if(abs(board[i]-board[j]) == (j-i)):
                v+=1
    return v

# this function is used to calculate the next best neighbour for the board
def  hill_climbing(board):
    global Repeat
    convert = {}
    length = len(board)
    for col in range(length):
        for row in range(length):
            if board[col] == row:
                continue
            board_copy = list(board)
            board_copy[col] = row
            convert[(col,row)] = kills(board_copy)

    answers = []
    conflict_now = kills(board)
    ok = 0
    for key,value in convert.items():
        if value < conflict_now:
            conflict_now = value
            ok = 1
    # if the ok parameter is toggled then the code has reached local/global minima
    if(ok == 0):
        Repeat = 1
        return board
    # we take all the best options and add them to a list
    for key,value in convert.items():
        if value == conflict_now:
            answers.append(key)
    # we choose randomly from the best options with same heuristic value
    if len(answers) > 0:
        x = random.randint(0,len(answers)-1)
        col = answers[x][0]
        row = answers[x][1]
        board[col] = row
    return board


def hc(caseNUM,board):
    global Repeat
    print("case: ", caseNUM)
    while(kills(board) != 0):
        board = hill_climbing(board)
        if(Repeat == 1):
            break
    if(kills(board) != 0 and Repeat == 1):
        Repeat = 0
        return board, "Failed"
    else:
        return board, "Success"

# board size
size = int(input("size of board = \n"))
result = "Hill Climbing" + " result:\n\n"
# number of test cases
ncase = int(input("number of test cases = \n"))
# initially the Success cases are zero 
successCase = 0
for i in range(ncase):
    # a new board is created
    board = []
    for v in range(size):
        board.append(random.randint(0,size-1))
    # we print the original board in the file
    result += "Case:  " + str(board) + " ----> "
    board, status = hc(i,board)
    if(status == "Success"):
        # when we are Successfull in the code we add one to successCase
        successCase+=1
        result += str(board) + "\n"
    else:
        result += str(board) + status + "\n"
result += "Total case number: " + str(ncase) + ", Success case number: " + str(successCase) + '\n'
result += "Success rate: " + str(successCase / float(ncase)) + '\n'
# here we add all the results in the file HC.txt 
f = open("HC" + '.txt', 'w+')
f.write(result)
f.close()
