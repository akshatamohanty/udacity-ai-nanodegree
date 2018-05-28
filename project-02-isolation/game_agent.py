"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random
import math


class SearchTimeout(Exception):
	"""Subclass base exception for code clarity. """
	pass


def custom_score(game, player):
	"""Calculate the heuristic value of a game state from the point of view
	of the given player.

	This should be the best heuristic function for your project submission.

	Note: this function should be called from within a Player instance as
	`self.score()` -- you should not need to call this function directly.

	Parameters
	----------
	game : `isolation.Board`
		An instance of `isolation.Board` encoding the current state of the
		game (e.g., player locations and blocked cells).

	player : object
		A player instance in the current game (i.e., an object corresponding to
		one of the player objects `game.__player_1__` or `game.__player_2__`.)

	Returns
	-------
	float
		The heuristic value of the current game state to the specified player.
	"""
	moves_left_player = len(game.get_legal_moves(player)); 
	moves_left_opponent = len(game.get_legal_moves(game.get_opponent(player)));
	aggressive_factor = 4;
	return float(moves_left_player) - aggressive_factor*float(moves_left_opponent);


def custom_score_2(game, player):
	"""Calculate the heuristic value of a game state from the point of view
	of the given player.

	Note: this function should be called from within a Player instance as
	`self.score()` -- you should not need to call this function directly.

	Parameters
	----------
	game : `isolation.Board`
		An instance of `isolation.Board` encoding the current state of the
		game (e.g., player locations and blocked cells).

	player : object
		A player instance in the current game (i.e., an object corresponding to
		one of the player objects `game.__player_1__` or `game.__player_2__`.)

	Returns
	-------
	float
		The heuristic value of the current game state to the specified player.
	"""
	moves_left_player = len(game.get_legal_moves(player)); 
	return float(moves_left_player)


def custom_score_3(game, player):
	"""Calculate the heuristic value of a game state from the point of view
	of the given player.

	Note: this function should be called from within a Player instance as
	`self.score()` -- you should not need to call this function directly.

	Parameters
	----------
	game : `isolation.Board`
		An instance of `isolation.Board` encoding the current state of the
		game (e.g., player locations and blocked cells).

	player : object
		A player instance in the current game (i.e., an object corresponding to
		one of the player objects `game.__player_1__` or `game.__player_2__`.)

	Returns
	-------
	float
		The heuristic value of the current game state to the specified player.
	"""
	moves_left_player = len(game.get_legal_moves(player)); 
	moves_left_opponent = len(game.get_legal_moves(game.get_opponent(player)));
	return float(moves_left_player)/1+float(moves_left_opponent)

class IsolationPlayer:
	"""Base class for minimax and alphabeta agents -- this class is never
	constructed or tested directly.

	********************  DO NOT MODIFY THIS CLASS  ********************

	Parameters
	----------
	search_depth : int (optional)
		A strictly positive integer (i.e., 1, 2, 3,...) for the number of
		layers in the game tree to explore for fixed-depth search. (i.e., a
		depth of one (1) would only explore the immediate sucessors of the
		current state.)

	score_fn : callable (optional)
		A function to use for heuristic evaluation of game states.

	timeout : float (optional)
		Time remaining (in milliseconds) when search is aborted. Should be a
		positive value large enough to allow the function to return before the
		timer expires.
	"""
	def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
		self.search_depth = search_depth
		self.score = score_fn
		self.time_left = None
		self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
	"""Game-playing agent that chooses a move using depth-limited minimax
	search. You must finish and test this player to make sure it properly uses
	minimax to return a good move before the search time limit expires.
	"""
	def get_move(self, game, time_left):
		"""Search for the best move from the available legal moves and return a
		result before the time limit expires.

		**************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

		For fixed-depth search, this function simply wraps the call to the
		minimax method, but this method provides a common interface for all
		Isolation agents, and you will replace it in the AlphaBetaPlayer with
		iterative deepening search.

		Parameters
		----------
		game : `isolation.Board`
			An instance of `isolation.Board` encoding the current state of the
			game (e.g., player locations and blocked cells).

		time_left : callable
			A function that returns the number of milliseconds left in the
			current turn. Returning with any less than 0 ms remaining forfeits
			the game.

		Returns
		-------
		(int, int)
			Board coordinates corresponding to a legal move; may return
			(-1, -1) if there are no available legal moves.
		"""
		self.time_left = time_left

		# Initialize the best move so that this function returns something
		# in case the search fails due to timeout
		best_move = (-1, -1)

		try:
			# The try/except block will automatically catch the exception
			# raised when the timer is about to expire.
			return self.minimax(game, self.search_depth)

		except SearchTimeout:
			pass  # Handle any actions required after timeout as needed

		# Return the best move from the last completed search iteration
		return best_move

	# def getScore(self, board, level):

	# 	if self.time_left() < self.TIMER_THRESHOLD:
	# 		raise SearchTimeout()

	# 	## check board is not terminating state
	# 	if board.is_winner(board.active_player) or board.is_loser(board.active_player):
	# 		return board.utility(board.active_player)

	# 	## check if winner or loser
	# 	# if( board.utility(player) != 1) and curr_depth != depth:
	# 	#     return board.utility(player)

	# 	current_depth = level + 1
	# 	if current_depth == self.search_depth:
	# 		return self.score(board, board.active_player)

	# 	moves_left = board.get_legal_moves(board.active_player)
	# 	scores = [];
	# 	for move in moves_left:
	# 		new_board = board.forecast_move(move)
	# 		scores.append(self.getScore(new_board, current_depth))
		
	# 	if current_depth % 2 == 0:
	# 		score = min(scores)
	# 	else:
	# 		score = max(scores)

	# 	return score

	def max_value(self, game, level, player):
		if self.time_left() < self.TIMER_THRESHOLD:
			raise SearchTimeout()

		current_depth = level + 1
		if current_depth == self.search_depth:
			return self.score(game, player)

		moves = game.get_legal_moves(game.active_player)
		score = -math.inf
		for move in moves:
			new_board = game.forecast_move(move)
			score = max(score, self.min_value(new_board, current_depth, player))

		return score

	def min_value(self, game, level, player):
		if self.time_left() < self.TIMER_THRESHOLD:
			raise SearchTimeout()

		current_depth = level + 1
		if current_depth == self.search_depth:
			return self.score(game, player)

		moves = game.get_legal_moves(game.active_player)
		score = math.inf
		for move in moves:
			new_board = game.forecast_move(move)
			score = min(score, self.max_value(new_board, current_depth, player))

		return score

	def minimax(self, game, depth):
		"""Implement depth-limited minimax search algorithm as described in
		the lectures.

		This should be a modified version of MINIMAX-DECISION in the AIMA text.
		https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

		**********************************************************************
			You MAY add additional methods to this class, or define helper
				 functions to implement the required functionality.
		**********************************************************************

		Parameters
		----------
		game : isolation.Board
			An instance of the Isolation game `Board` class representing the
			current game state

		depth : int
			Depth is an integer representing the maximum number of plies to
			search in the game tree before aborting

		Returns
		-------
		(int, int)
			The board coordinates of the best move found in the current search;
			(-1, -1) if there are no legal moves

		Notes
		-----
			(1) You MUST use the `self.score()` method for board evaluation
				to pass the project tests; you cannot call any other evaluation
				function directly.

			(2) If you use any helper functions (e.g., as shown in the AIMA
				pseudocode) then you must copy the timer check into the top of
				each helper function or else your agent will timeout during
				testing.
		"""
		if self.time_left() < self.TIMER_THRESHOLD:
			raise SearchTimeout()

		best_move = (-1, -1)

		## print("game check", game.is_winner(game.active_player), game.is_loser(game.active_player))
		player = game.active_player
		moves = game.get_legal_moves(player)
		# ## print(len(moves))

		# ## print("moves applied", game.move_count)
		if len(moves) == 0:
			return best_move

		## first move when player 1
		# if game.move_count == 0:
		# 	return (3, 3)

		## Get scores of the child states of the board passed
		moves_scores = []
		score = -math.inf
		for move in moves:
			new_board = game.forecast_move(move)
			board_value = self.min_value(new_board, 0, player)
			if score < board_value:
				score = board_value
				best_move = move
			# new_board = game.forecast_move(move)
			# moves_scores.append(self.getScore(new_board, 0))
		return best_move;


class AlphaBetaPlayer(IsolationPlayer):
	"""Game-playing agent that chooses a move using iterative deepening minimax
	search with alpha-beta pruning. You must finish and test this player to
	make sure it returns a good move before the search time limit expires.
	"""

	def get_move(self, game, time_left):
		"""Search for the best move from the available legal moves and return a
		result before the time limit expires.

		Modify the get_move() method from the MinimaxPlayer class to implement
		iterative deepening search instead of fixed-depth search.

		**********************************************************************
		NOTE: If time_left() < 0 when this function returns, the agent will
			  forfeit the game due to timeout. You must return _before_ the
			  timer reaches 0.
		**********************************************************************

		Parameters
		----------
		game : `isolation.Board`
			An instance of `isolation.Board` encoding the current state of the
			game (e.g., player locations and blocked cells).

		time_left : callable
			A function that returns the number of milliseconds left in the
			current turn. Returning with any less than 0 ms remaining forfeits
			the game.

		Returns
		-------
		(int, int)
			Board coordinates corresponding to a legal move; may return
			(-1, -1) if there are no available legal moves.
		"""
		self.time_left = time_left
		self.search_depth = 0

		# Initialize the best move so that this function returns something
		# in case the search fails due to timeout
		best_move = (-1, -1)

		while self.time_left() > self.TIMER_THRESHOLD:
			try:
				# The try/except block will automatically catch the exception
				# raised when the timer is about to expire.
				self.search_depth = self.search_depth + 1
				best_move = self.alphabeta(game, self.search_depth)
				if best_move == (-1, -1):
					break
				#return self.alphabeta(game, self.search_depth)
			except SearchTimeout:
				self.search_depth = 0
				return best_move
				# pass  # Handle any actions required after timeout as needed

		# Return the best move from the last completed search iteration
		return best_move


	def max_value(self, game, alpha, beta, level, player):
		if self.time_left() < self.TIMER_THRESHOLD:
			raise SearchTimeout()

		current_depth = level + 1
		if current_depth == self.search_depth:
			return self.score(game, player)

		score = -math.inf
		moves = game.get_legal_moves(game.active_player)
		for move in moves:
			new_game = game.forecast_move(move)
			score = max(score, self.min_value(new_game, alpha, beta, current_depth, player))
			if score >= beta:
				return score
			alpha = max(alpha, score)

		return score

	def min_value(self, game, alpha, beta, level, player):
		if self.time_left() < self.TIMER_THRESHOLD:
			raise SearchTimeout()

		current_depth = level + 1
		if current_depth == self.search_depth:
			return self.score(game, player)

		score = math.inf
		moves = game.get_legal_moves(game.active_player)
		for move in moves:
			new_game = game.forecast_move(move)
			score = min(score, self.max_value(new_game, alpha, beta, current_depth, player))
			if score <= alpha:
				return score
			beta = min(beta, score)

		return score

	def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
		"""Implement depth-limited minimax search with alpha-beta pruning as
		described in the lectures.

		This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
		https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

		**********************************************************************
			You MAY add additional methods to this class, or define helper
				 functions to implement the required functionality.
		**********************************************************************

		Parameters
		----------
		game : isolation.Board
			An instance of the Isolation game `Board` class representing the
			current game state

		depth : int
			Depth is an integer representing the maximum number of plies to
			search in the game tree before aborting

		alpha : float
			Alpha limits the lower bound of search on minimizing layers

		beta : float
			Beta limits the upper bound of search on maximizing layers

		Returns
		-------
		(int, int)
			The board coordinates of the best move found in the current search;
			(-1, -1) if there are no legal moves

		Notes
		-----
			(1) You MUST use the `self.score()` method for board evaluation
				to pass the project tests; you cannot call any other evaluation
				function directly.

			(2) If you use any helper functions (e.g., as shown in the AIMA
				pseudocode) then you must copy the timer check into the top of
				each helper function or else your agent will timeout during
				testing.
		"""
		if self.time_left() < self.TIMER_THRESHOLD:
			raise SearchTimeout()

		best_move = (-1, -1)
		player = game.active_player
		moves = game.get_legal_moves(game.active_player)

		if len(moves) == 0:
			return best_move

		score = -math.inf
		alpha = -math.inf
		beta = math.inf
		for move in moves:
			new_game = game.forecast_move(move)
			move_value = self.min_value(new_game, alpha, beta, 0, player)
			if move_value > score:
				alpha =  move_value
				score = move_value
				best_move = move

		return best_move

		# TODO: finish this function!
		# raise NotImplementedError