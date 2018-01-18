import random

def game_outcome(bankroll, bet):
    """Output outcome of one game.

	Args:
		bankroll: Amount of money in bankroll at current game in series.
		bet: Size of bet to be placed in current game in series.

	Returns:
		bankroll: Amount of money at conclusion of game.
		bet: Size of bet to be placed in concurrent game in series.

	"""
	game_conclusion = random.randint(0, 1)
	print(game_conclusion)
    return bankroll, bet

def main():
    num_games = 7
	bankroll = 100
	bet = 1
	for n in range(num_games):
		game_outcome(bankroll, bet)

if __name__ == '__main__':
    main()
