import random
import math

# this parameter is to check if we were unsuccessfull in solving the test case
FAILED = False

# this function is to calculate the heuristic value of the board
def kills(board):
    num = 0
    for col in range(size):
        for anotherCol in range(col+1, size):
            # for in line collision
            if board[col] == board[anotherCol]:
                num += 1
            # for diagonall collision
            elif abs(board[col] - board[anotherCol]) == (anotherCol - col):
                num += 1 #
    return num

# choose if we accept the random choice with certain probability or not
def step_SimulatedAnnealing(board):
    temperature = len(board)**2
    # we have fixed the annealingRate to 0.95 for the code 
    annealingRate = 0.95
    while True:
        randomRow = random.randint(0,len(board)-1)
        randomCol = random.randint(0,len(board)-1)
        originCollisionNum = kills(board)
        originRow = board[randomCol]
        board[randomCol] = randomRow
        newCollisionNum = kills(board)
        temperature = max(temperature * annealingRate, 0.02)
        # now we decide if the next move is a good one or bad one with low probability
        if newCollisionNum < originCollisionNum:
            return board
        else:
            deltaE = newCollisionNum - originCollisionNum
            acceptProbability = min(math.exp(deltaE / temperature), 1)
            if random.random() <= acceptProbability:
                return board
            else:
                board[randomCol] = originRow
    return board

# this function is here to decide if the code has reached the lowest heuristic value or not 
def solution_SimulatedAnnealing(board):
    # the success rate will increase by increasing the maxRound but the time to calculate will also increase
    maxRound = 500000
    count = 0
    while True:
        collisionNum = kills(board)
        if collisionNum == 0:
            return board
        board = step_SimulatedAnnealing(board)
        count += 1
        if(count >= maxRound):
            # if the number of tries to fix the test case exceeds from maxRound then the test case fails
            global FAILED
            FAILED = True
            return board

# this is the main fuction which recives the initial test case and send back the status pass/fail
def m(caseNum,board):
    print("case: ", caseNum)
    global FAILED
    FAILED = False
    board = solution_SimulatedAnnealing(board)
    if FAILED:
        return board, "Failed!"
    else:
        return board, "Success"

# board size
size = int(input("size of board = \n"))
result = "Simulated Annealing Hill Climbing" + " result:\n\n"
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
    board, status = m(i,board)
    if(status == "Success"):
        # when we are Successfull in the code we add one to successCase
        successCase+=1
        result += str(board) + "\n"
    else:
        result += str(board) + status + "\n"
result += "Total case number: " + str(ncase) + ", Success case number: " + str(successCase) + '\n'
result += "Success rate: " + str(successCase / float(ncase)) + '\n'
# here we add all the results in the file SAHC.txt 
f = open("SAHC" + '.txt', 'w+')
f.write(result)
f.close()
