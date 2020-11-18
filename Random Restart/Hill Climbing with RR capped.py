import random
import time
# this function is to calculate the heuristic value of the board and maximize the result as the highest value can be 28
def value(board):
	v = 0
	for i in range(size):
		for j in range(i+1,size):
			# for in line collision
			if(board[i] == board[j]):
				v+=1
			# for diagonall collision
			if(abs(board[i]-board[j]) == (j-i)):
				v+=1
	return 28 - v

# this fuction is to check if the next possible value can bring correct solution or we need a random restart
def code(board):
	c = 0
	while(True):
		# we set the initial values as the best values for default
		bestBoard = list(board)
		boardValue = bestvalue = value(board)
		if(bestvalue == 28):
			# this means we have solved the testcase
			return 1, bestBoard
		c+=1
		currentBoard = list(board)
		# to check the best move in the currentBoard for highest value() value 
		for i in range(size):
			temp = currentBoard[i]
			for j in range(size):
				if(j == board[i]):
					continue
				currentBoard[i] = j
				currentValue = value(currentBoard)
				if(currentValue > bestvalue):
					bestvalue = currentValue
					bestBoard = list(currentBoard)
			currentBoard[i] = temp
		if(bestvalue <= boardValue):
			# we are now looped so we need a random restart
			return 0, bestBoard
		board = list(bestBoard)



def m():
	# initially we set success to 0 so we keel looping to find the answer or can perform a rendom restart
	success = 0
	c = 0
	while(True):
		# here we create a test case or after random restart a new board
		board = []
		for i in range(size):
			board.append(random.randint(0,size-1))
		if(c == 0):
			zoom = list(board)
		success,board = code(board)
		c+=1
		if(success or (c > ((cappedValue) + 1)) ):
			print(board)
			print("Restart number"+str(c)+"\n")
			return str(board), str(c), str(zoom)
			break



# to check how many random restart we need in average
avg = 0
# size of the board
size = int(input("size of board = \n"))
result = "Random Restart Hill Climbing" + " result:\n\n"
# number of test cases
ncase = int(input("number of test cases = \n"))
ok = 0
cappedValue = int(input("Capped value of Random Restart = \n"))
ti = time.time()
for i in range(ncase):
	board, c, original = m()
	# after adding thee random restart function we get our accuracy to 100 % in avg restarts given 
	avg += int(c)
	 # we print the original board and its solution in the file
	if(int(c) > cappedValue):
		result += "Case:  " + original + " ----> " + "Failed" + "\n"
	else:
		ok+=1
		result += "Case:  " + original + " ----> " + board + ": Random Restart taken - "+ c + "\n"
avg = avg / ncase
result += "average Random Restart are : "+str(avg) + '\n'
result += "Total case number: " + str(ncase) + ", Success case number: " + str(ok) + '\n'
result += "Success rate: " + str(ok / float(ncase)) + '\n'
result += "random restarts were capped at "+ str(int(cappedValue)) + '\n'
tf = time.time()
result += "average time taken is : "+ str( time.localtime(tf-ti).tm_sec / float(ncase) ) + 'sec\n'
# here we add all the results in the file RRHC.txt 
f = open("RRHC" + '.txt', 'w+')
f.write(result)
f.close()
