#Tic tac toe basic game  using python
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

# this checks if the game is still going on
playing = True

winner = None

#whose turn is it...
current_player = "X"


#game board created here...
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():

    #display the board
    display_board()

    while playing:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()


#the game has ended
    if winner == 'X' or winner == 'O':
        print(winner + ' won.')
    elif winner == None:
        print('Tie')


def handle_turn(player):
    print(player + "'s turn")
    position = input('\nEnter the position from 1-9: ')

    valid = False
  
    while not valid:
      while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input('\nEnter the position from 1-9: ')
      position = int(position) - 1

      if board[position] == "-":
        valid = True
      
      else:
        print("The spot is secured, try elsewhere!")

    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    global winner

    #check rows
    row_winner = check_rows()
    #check column
    column_winner = check_columns() 
    #check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
      winner = row_winner
    elif column_winner:
      winner = column_winner
    elif diagonal_winner:
      winner = diagonal_winner

    else:
      winner = None

   


def check_rows():
  #set playing variable as a globale
  global playing
  #check if which row matches

  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"

  if row_1 or row_2 or row_3:
    playing = False
  
  if row_1:
    return board[0]

  elif row_2:
    return board[3]

  elif row_3:
    return board[6]

  else:
    return None


  

#check the columns
def check_columns():
  #set the global variable
  global playing

  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"

  if column_1 or column_2 or column_3:
    playing =  False

  if column_1:
    return board[0]

  elif column_2:
    return board[1]

  elif column_3:
    return board[2]
 #or return None if there's no winner
  else:
    return None


def check_diagonals():
  #set playing as globals
  global playing
  
  #check the diagonals

  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[6] == board[4] == board[2] != "-"

  if diagonal_1 or diagonal_2:
  #set playing to False
    playing = False

    if diagonal_1:
       return board[0]

    elif diagonal_2: 
       return board[2]

   #or return None if there's no winner
    else:
     return None


def check_if_tie():
    global playing
    #check_if_board is ful
    if "-" not in board:
      playing = False
    
    #check o and x's winning points
      return

#flip player from "x" to "o"
def flip_player():
  #current_player as global
  global current_player

  #if current player is x change to o 
  if current_player == "X":
    current_player = "O"
  
  #if the current_player is o change it x
  elif current_player == "O":
    current_player = "X"


    return


play_game()
