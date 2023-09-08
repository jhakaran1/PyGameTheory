import numpy as np
import pandas as pd
import sys

from Game import Game, Player, read_file, read_payoff, SolveForMixed, makeGame

def main(argv):
	game,Player1,Player2 = makeGame(argv)
	mixed_eq = game.Mixed_Eq()
	player = input('Enter the Player Number (1 or 2)')
	strat = input("Enter the Strategy from Player's Strategy set")
	BR = game.getBR(player,strat)[1]
	print(BR)


if __name__ == '__main__':
	main(sys.argv)