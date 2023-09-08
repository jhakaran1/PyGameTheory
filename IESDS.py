import numpy as np
import pandas as pd
import sys

from Game import Game, Player, read_file, read_payoff, SolveForMixed, makeGame

def main(argv):
	game,Player1,Player2 = makeGame(argv)
	a,b = game.IESDS()
	for i in a:
		for j in b:
			print(i,j)


if __name__ == '__main__':
	main(sys.argv)
