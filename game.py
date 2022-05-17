board = [ ["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"] ]
turn = 0
number = "q"

#PRINTS BOARD
def print_board(board):
	for row in board :
		for col in row :
			print(f"{col} ", end="" )
		print()

#REFRESH THE BOARD AGAIN FOR NEXT ROUND
def refresh_board(board):
	for col in range(0,3):
		for row in range(0,3):
			board[row][col] = "-"

#PRINTS GAME RULES		
def game_rule(board):
	print("User need to input a number between 1 to 9 to select their move.")
	print("Each number corresponds to a position in a 3x3 board.")
	print("By selecting each position, user occupy that place with his/her symbol.")
	print("That player (user or computer) wins whose symbols make a line of length 3, either row wise or column wise or diagonally.")
	import time
	time.sleep(2)
	print()
	print("Printing the board...")
	import time
	time.sleep(2)
	print()
	print_board(board)
	print("Number 1 corresponds to 1st row and 1st column.")
	print("Number 2 corresponds to 1st row and 2nd column.")
	print("Number 3 corresponds to 1st row and 3rd column.")
	print("Number 4 corresponds to 2nd row and 1st column.")
	print("Number 5 corresponds to 2nd row and 2nd column.")
	print("Number 6 corresponds to 2nd row and 3rd column.")
	print("Number 7 corresponds to 3rd row and 1st column.")
	print("Number 8 corresponds to 3rd row and 2nd column.")
	print("Number 9 corresponds to 3rd row and 3rd column.")
	print()
	print("If user input a number and position corresponding to that number is already occupied then user needs to input the number again.")
	print("User can select his/her symbol. (Either X or 0[zero])")
	start = input("Press Enter to start. ")

#CHECK WHETHER TO QUIT OR NOT 
def quit(number):
	if number == "q" or number == "Q":
		return True
	else:
		return False

#CHECKS FOR CORRET INPUT OF NUMBER
def correct_input(number):
	if not number.isnumeric():
		print("It is not a valid input !")
		print("Try again.")
		return False
	
	number = int(number)
	
	if number < 1 or number > 9:
		print("Input number out of bound !")
		print("Try again.")
		return False
	
	return True

#CHECKS IF SOMEONE HAS WON
def check_win(board,symbol):
	#Checking row wise
	for row in board:
		ans = True
		for col in row:
			if col != symbol:
				ans = False
				break
		if ans:
			return True
	
	#Checking col wise
	for col in range(0,3):
		ans = True
		for row in range(0,3):
			if board[row][col] != symbol:
				ans = False
				break
		if ans:
				return True
			
	#Checking diagonal wise
	if board[0][0]==symbol and board[1][1]==symbol and board[2][2]==symbol:
		return True
	if board[0][2]==symbol and board[1][1]==symbol and board[2][0]==symbol:
		return True
	
	return False

#CHECKS WHETHER THERE IS A DRAW OR NOT
def check_draw(board):
	for row in board:
		for col in row:
			if col == "-":
				return False
	return True

#MAKE ROW FROM NUMBER
def make_row(number):
	row = int(number/3)
	return row

#MAKE COLUMN FROM NUMBER
def make_col(number):
	col = int(number%3)
	return col
	
#ADD SYMBOL TO BOARD	
def add(row,col,symbol,board):
	board[row][col] = symbol

#GENERATE RANDOM NUMBER FROM 0 TO 8
def gen_random():
	from random import randrange
	ran = randrange(0, 9)
	return ran

#GENERATE RANDOM NUMBER FROM 1 TO 2
def gen_random2():
	from random import randrange
	ran = randrange(1, 3)
	return ran

#CHECKS WHETHER PARTICULAR ELEMENT IS ALREADY USED
def is_used(row,col,symbol,csymbol,board):
	if board[row][col] == symbol or board[row][col] == csymbol:
		return True
	else:
		return False

#CLEARS SCREEN
def clear():
    from os import system, name
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

#CHECKS WHETHER INPUT SYMBOL IS CORRECT OR NOT
def check_symbol(symbol):
	while(symbol != "X" and symbol != "0"):
		print("Please choose a correct symbol.")
		print("Allowed symbols X or 0[zero]")
		symbol = input("Please select your symbol: ")
		symbol = symbol.upper()
	return symbol		

#REINPUT NUMBER IN CASE IT IS INCORRECT
def reinput(number):
	while True:
		number = input("Enter position from 1 to 9 or press \"q\" to quit: ")
		if quit(number):
			print("Thanks for playing.")
			break
		if correct_input(number):
			break
	return number

#VALIDATION CHECK FOR INPUT LEVEL
def check_level(level):
	while(level != "D" and level != "E"):
		print("Please give a correct input for difficluty.")
		print("Allowed inputs E or D.")
		level = input("Please select difficulty: ")
		level = level.upper()
	return level

#COMPUTER MAKES HIS MOVE IN HARD MODE
def cturn(board,csymbol,symbol):
	best_score=-2
	best_r=0
	best_c=0
		
	for row in range(0,3):
		for col in range(0,3):
			if not is_used(row,col,symbol,csymbol,board):
				board[row][col] = csymbol
				score = minimax(board,csymbol,symbol,False)
				board[row][col] = "-"
				if(score > best_score):
					best_score = score
					best_r = row
					best_c = col
	
	add(best_r,best_c,csymbol,board)

#MINIMAX FUNCTION
def minimax(board,csymbol,symbol,maxi):
	if check_win(board,csymbol):
		return 1
	elif check_win(board,symbol):
		return -1
	elif check_draw(board):
		return 0
	
	if not maxi:
		best_score=2
		
		for row in range(0,3):
			for col in range(0,3):
				if not is_used(row,col,symbol,csymbol,board):
					board[row][col] = symbol
					score = minimax(board,csymbol,symbol,True)
					board[row][col] = "-"
					if(score < best_score):
						best_score = score
		return best_score
	else:
		best_score=-2
		
		for row in range(0,3):
			for col in range(0,3):
				if not is_used(row,col,symbol,csymbol,board):
					board[row][col] = csymbol
					score = minimax(board,csymbol,symbol,False)
					board[row][col] = "-"
					if(score > best_score):
						best_score = score
		return best_score


game_rule(board)
clear()

symbol = input("Please select your symbol: ")
symbol = symbol.upper()

symbol = check_symbol(symbol)

if symbol == "X":
	csymbol = "0"
else :
	csymbol = "X"

move = int(gen_random2())

while True:
	turn = 0
	
	level = input("Please select difficulty \"E\" for Easy or \"D\" for difficult: ") 
	level = level.upper()
	level = check_level(level)
	
	clear()
	import time
	time.sleep(1)
	
	print_board(board)
	if move%2 == 1:
		if level == "E":
			while (turn < 9):
				number = input("Enter position from 1 to 9 or press \"q\" to quit: ")
	
				if quit(number):
					print("Thanks for playing.")
					break
	
				if not correct_input(number):
					continue
			
				number = int(number) - 1
				row = make_row(number)
				col = make_col(number)
	
				if is_used(row,col,symbol,csymbol,board):
					print("This element is already marked.")
					print("Try again.")
					continue
		
				add(row,col,symbol,board)
				turn = turn + 1
	
				print_board(board)
				if check_win(board,symbol):
					print("User Win !!")
					break
			
				if turn == 9:
					print("Its a tie !!")
					break
		
				import time
				time.sleep(1)
		
				print("Computer's turn.")
	
				import time
				time.sleep(1)
	
				randomN = 0
				randomN = gen_random()
				ran_row = make_row(randomN)
				ran_col = make_col(randomN)
				if is_used(ran_row,ran_col,symbol,csymbol,board):
					while True:
						randomN = gen_random()
						ran_row = make_row(randomN)
						ran_col = make_col(randomN)
						if not is_used(ran_row,ran_col,symbol,csymbol,board):
							break
	
				add(ran_row,ran_col,csymbol,board)
				turn = turn + 1
	
				print_board(board)
				if check_win(board,csymbol):
					print("Computer Win !!")
					break
			
			if number == "q" or number == "Q":
				break
			
			again = input("DO YOU WANT TO PLAY AGAIN ? (Press Y or N): ")
			if again.upper() == "Y":
				move=move+1
				refresh_board(board)
				continue
			else:
				print("Thanks for playing.")
				break
			
		else:
			while (turn < 9):
				number = input("Enter position from 1 to 9 or press \"q\" to quit: ")
			
				if quit(number):
					print("Thanks for playing.")
					break
		
				if not correct_input(number):
					continue
			
				number = int(number) - 1
				row = make_row(number)
				col = make_col(number)
	
				if is_used(row,col,symbol,csymbol,board):
					print("This element is already marked.")
					print("Try again.")
					continue
		
				add(row,col,symbol,board)
				turn = turn + 1
			
				print_board(board)
				if check_win(board,symbol):
					print("User Win !!")
					break
		
				if turn == 9:
					print("Its a tie !!")
					break
		
				import time
				time.sleep(1)
	
				print("Computer's turn.")
	
				import time
				time.sleep(1)
	
				cturn(board,csymbol,symbol)
				turn = turn + 1
	
				print_board(board)
				if check_win(board,csymbol):
					print("Computer Win !!")
					break
			if number == "q" or number == "Q":
				break
			
			again = input("DO YOU WANT TO PLAY AGAIN ? (Press Y or N): ")
			if again.upper() == "Y":
				move=move+1
				refresh_board(board)
				continue
			else:
				print("Thanks for playing.")
				break
	
	else:
		if level == "E":
			while (turn < 9):		
				print("Computer's turn.")
	
				import time
				time.sleep(1)
	
				randomN = 0
				randomN = gen_random()
				ran_row = make_row(randomN)
				ran_col = make_col(randomN)
				if is_used(ran_row,ran_col,symbol,csymbol,board):
					while True:
						randomN = gen_random()
						ran_row = make_row(randomN)
						ran_col = make_col(randomN)
						if not is_used(ran_row,ran_col,symbol,csymbol,board):
							break
	
				add(ran_row,ran_col,csymbol,board)
				turn = turn + 1
	
				print_board(board)
				if check_win(board,csymbol):
					print("Computer Win !!")
					break
				
				if turn == 9:
					print("Its a tie !!")
					break
			
				number = input("Enter position from 1 to 9 or press \"q\" to quit: ")

				if quit(number):
					print("Thanks for playing.")
					break
	
				if not correct_input(number):
					number = reinput(number)
					
				if quit(number):
					break
			
				number = int(number) - 1
				row = make_row(number)
				col = make_col(number)
	
				if is_used(row,col,symbol,csymbol,board):
					while True:
						print("This element is already marked.")
						print("Try again.")
						number = input("Enter position from 1 to 9 or press \"q\" to quit: ")
						if quit(number):
							break
						if not correct_input(number):
							number = reinput(number)
						if quit(number):
							break
						number = int(number) - 1
						row = make_row(number)
						col = make_col(number)
						if not is_used(row,col,symbol,csymbol,board):
							break
				if quit(number):
					break
				
				add(row,col,symbol,board)
				turn = turn + 1
	
				print_board(board)
				if check_win(board,symbol):
					print("User Win !!")
					break
		
				import time
				time.sleep(1)
			
			if number == "q" or number == "Q":
				break
			
			again = input("DO YOU WANT TO PLAY AGAIN ? (Press Y or N): ")
			if again.upper() == "Y":
				move=move+1
				refresh_board(board)
				continue
			else:
				print("Thanks for playing.")
				break
		
		else:
			while (turn < 9):
				print("Computer's turn.")
	
				import time
				time.sleep(1)
	
				cturn(board,csymbol,symbol)
				turn = turn + 1
	
				print_board(board)
				if check_win(board,csymbol):
					print("Computer Win !!")
					break
			
				if turn == 9:
					print("Its a tie !!")
					break
			
				number = input("Enter position from 1 to 9 or press \"q\" to quit: ")
			
				if quit(number):
					print("Thanks for playing.")
					break
	
				if not correct_input(number):
					number = reinput(number)

				if quit(number):
					break
			
				number = int(number) - 1
				row = make_row(number)
				col = make_col(number)
	
				if is_used(row,col,symbol,csymbol,board):
					while True:
						print("This element is already marked.")
						print("Try again.")
						number = input("Enter position from 1 to 9 or press \"q\" to quit: ")
						if quit(number):
							break
						if not correct_input(number):
							number = reinput(number)
						if quit(number):
							break
						number = int(number) - 1
						row = make_row(number)
						col = make_col(number)
						if not is_used(row,col,symbol,csymbol,board):
							break
				if quit(number):
					break
				add(row,col,symbol,board)
				turn = turn + 1
		
				print_board(board)
				if check_win(board,symbol):
					print("User Win !!")
					break
		
				import time
				time.sleep(1)
			
			if number == "q" or number == "Q":
				break
			
			again = input("DO YOU WANT TO PLAY AGAIN ? (Press Y or N): ")
			if again.upper() == "Y":
				move=move+1
				refresh_board(board)
				continue
			else:
				print("Thanks for playing.")
				break

