import numpy as np
import pandas as pd
import sys

from Game import Game, Player, read_file, read_payoff, SolveForMixed, makeGame

def main(argv):
	game,Player1,Player2 = makeGame(argv)
	mixed_eq = game.Mixed_Eq()
	for i in mixed_eq:
		print(i)


if __name__ == '__main__':
	main(sys.argv)