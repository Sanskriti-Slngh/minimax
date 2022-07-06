import numpy as np
import copy
import base

agentX = "X"
agentO = "O"

class ticTacToe(base.minMaxGameBase()):
  
  # Initial board state
  def initial_state(self):
    return np.array([['-','-','-'],
                     ['-','-','-'],
                     ['-','-','-']])

  # Given state, find out whose turn
  def player(self, board):
    count = np.sum(board == "-")
    if count%2 == 0:
      return agentO
    else:
      return agentX

  # find all possible actions
  # save indexes as tuples
  def actions(self, board, player_override="none"):
    if player_override != "none":
      player = player_override
    else:
      player = self.player(board)
    if player in board:
      agent = np.where(board == player)
      agentc = [(x, y) for x, y in zip(agent[0], agent[1])]
      c = agentc[0]

      f = []
      x_vals = [-1, 0, 1]
      y_vals = [-1, 0, 1]

      for xc in x_vals:
        for yc in y_vals:
          if (c[0] + xc) < 0 or (c[0] + xc) > 2:
            continue
          else:
            if (c[1] + yc) < 0 or (c[1] + yc) > 2:
              continue
            else:
              f.append((c[0] + xc, c[1] + yc))
      
      final = []
      for i in f:
        if board[i[0], i[1]] == "-":
          final.append(i)

      return final
    else:
      all = np.where(board == '-')
      final = [(x, y) for x, y in zip(all[0], all[1])]
      return final

  # how would the board look if this action were applied
  def result(self, board, action):
    result = copy.deepcopy(board)
    if self.player(board) in board:
      agent = np.where(board == self.player(board))
      agentc = [(x, y) for x, y in zip(agent[0], agent[1])]
      result[agentc[0][0], agentc[0][1]] = "*"
    result[action[0], action[1]] = self.player(board)
    return result

  # terminal function
  def is_game_over(self, board):
    x_c = self.actions(board, "X")
    o_c = self.actions(board, "O")
    if x_c == [] or o_c == []:
      return True
    else:
      return False

  def win(self, board):
    if self.player(board) == agentX and self.is_game_over(board):
      return agentX
    if self.player(board) == agentO and self.is_game_over(board):
      return agentO

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
    print(winner + " wins!")
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
    actions = mygame.actions(board, user)
    while board[move[0], move[1]] != '-' or move not in actions:
      print("this spot is not possible :(")
      move = input("what posit1ion? (row,column)")
      move = tuple(int(a) for a in move.split(","))
    board = mygame.result(board, move)
  else:
    continue
