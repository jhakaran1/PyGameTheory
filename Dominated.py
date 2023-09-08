import numpy as np
import pandas as pd
import sys

from Game import Game, Player, read_file, read_payoff, SolveForMixed, makeGame

def main(argv):
	game,Player1,Player2 = makeGame(argv)
	mixed_eq = game.Mixed_Eq()
	player_no = input('Enter the Player Number (1 or 2)')
	if player_no == '1':
		player = Player1
	else:
		player = Player2
	dom,compare = player.dominated()
	print(BR)


if __name__ == '__main__':
	main(sys.argv)