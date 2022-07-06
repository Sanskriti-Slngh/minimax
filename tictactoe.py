import numpy as np
import copy

agentX = "X"
agentO = "O"

class ticTacToe(minMaxGameBase):
  
  # Initial board state
  def initial_state(self):
    return np.array([['-','-','-'],
                     ['-','-','-'],
                     ['-','-','-']])

  # Given state, find out whose turn
  def player(self, board):
    xcount = np.sum(board == "X")
    ocount = np.sum(board == "O")
    if ocount < xcount:
      return agentO
    else:
      return agentX

  # find all possible actions
  # save indexes as tuples
  def actions(self, board):
    all = np.where(board == '-')
    ans = [(x, y) for x, y in zip(all[0], all[1])]
    return ans

  # how would the board look if this action were applied
  def result(self, board, action):
    result = copy.deepcopy(board)
    result[action[0], action[1]] = self.player(board)
    return result
    
  # return who wins (arbitary number is returned if game has no winner)
  def win(self, board):
    
    # rows
    if np.all(board[0,:] == board[0,0]) and np.all(board[0,0] != '-'):
      return board[0, 0]
    if np.all(board[1,:] == board[1,0]) and np.all(board[1,0] != '-'):
      return board[1, 0]
    if np.all(board[2,:] == board[2,0]) and np.all(board[2,0] != '-'):
      return board[2, 0]

    # column
    elif board[0, 0] == board[1, 0] and board[1, 0] == board[2, 0] and np.all(board[0,0] != '-'):
      return board[0, 0]
    elif board[0, 1] == board[1, 1] and board[1, 1] == board[2, 1] and np.all(board[0,1] != '-'):
      return board[0, 1]
    elif board[0, 2] == board[1, 2] and board[1, 2] == board[2, 2] and np.all(board[0,2] != '-'):
      return board[0, 2]
    
    # diagnols
    elif board[0, 0] == board[1, 1] and board[1, 1] == board[2, 2] and np.all(board[0,0] != '-'):
        return board[2, 2]
    elif board[0, 2] == board[1, 1] and board[1, 1] == board[2, 0] and np.all(board[0,2] != '-'):
        return board[2, 0]
    else:
        return 50 # arbitary number

  # terminal function
  def is_game_over(self, board):
    if (not (any('-' in i for i in board))) or (self.win(board) != 50):
      return True
    else:
      return False

  # score calculator
  def utility(self, board):
    if self.is_game_over(board):
      if self.win(board) == agentX:
        return 1
      elif self.win(board) == agentO:
        return -1
      else:
        return 0
 
# Algorthim to play the game
# Constant for every minimax problem
def minimax(game, board):
    if game.is_game_over(board):
      return None
    else:
      if game.player(board) == agentX:
        value, move = maxv(game, board)
        return move
      else:
        value, move = minv(game, board)
        return move

# maximizing agent
def maxv(game, board):
    if game.is_game_over(board):
      return game.utility(board), None

    v = float("-inf")
      
    for action in game.actions(board):
      val, act = minv(game, game.result(board, action))
      if val > v:
          v = val
          move = action
          if v == 1:
              return v, move

    return v, move

# minimizing agent
def minv(game, board):
    if game.is_game_over(board):
      return game.utility(board), None

    v = float("inf")
      
    for action in game.actions(board):
      val, act = maxv(game, game.result(board, action))
      if val < v:
          v = val
          move = action
          if v == -1:
              return v, move

    return v, move


# play the game
mygame = ticTacToe()

user = input("Who do you want to be? X|O \n")
board = mygame.initial_state()

f = True
while f:
  print(board)
  if mygame.is_game_over(board):
    winner = mygame.win(board)
    if winner is 50:
      print("TIED!")
      f = False
    else:
      print(winner + "wins!")
      f = False
  elif user == mygame.player(board):
    print("Users turn")
  else:
    print("Computers turn")

  if user != mygame.player(board) and not mygame.is_game_over(board):
    move = minimax(mygame, board)
    print(move)
    board = mygame.result(board, move)
  elif not mygame.is_game_over(board):
    move = input("what position? (row,column)")
    move = tuple(int(a) for a in move.split(","))
    while board[move[0], move[1]] != '-':
      print("this spot is already taken :(")
      move = input("what position? (row,column)")
      move = tuple(int(a) for a in move.split(","))
    board = mygame.result(board, move)
  else:
    continue
