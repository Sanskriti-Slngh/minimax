class minMaxGameBase:
  
  # base class to store some of the information
  def __init__(self):
    self.current_payer = None
    self.board = None

  # Initial state of the game
  def initial_state():
    print("You have not defined your initial state")
    return

  # To find out whose turn given a state
  def player(self, state):
    print("You have not defined the player(s)")
    return 

  # all the possible actions given a state
  def actions(self, state):
    print("You have not defined the action(s)")
    return
  
  # what is next state, given a state and an action
  def result(self, state, action):
    print("You have not defined the result(s)")
    return

  # check if game is over
  def is_game_over(self, state):
    print("You have not defined when the game ends")
    return

  # given a state, what is the score
  def utility(self, state):
    print("You have not defined how the score is calculated")
    return
