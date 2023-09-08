All the classes, methods and functons are defined in Game.py.
You will have to navigate to the directory PyGameTheory.

Running the programs:-
To find the dominated strategies run "python3 Dominated.py 'input file'" then enter the player number to get the strategy pair with first one being dominated by the second one. For example, in this directory run "python3 Dominated.py Ex1.txt" then enter 1 as input to get player 1's strategy pair.

To find the Best Response to a strategy run "python3 BR.py 'input file'" then enter the inputs as directed, first the player number, then one of the strategies from her strategy set, then the output will be the other player's Best Response. For example, in this directory run "python3 BR.py Ex1.txt" then enter 1 and then U, output should be L.

To find the IESDS strategies, run "python3 IESDS.py 'input file'". For example, in this directory run "python3 IESDS.py Ex1.txt". The output will be all the pairs of strategies for player 1 and player 2 that survive IESDS elimination.

To find the rationalizable strategies, run "python3 rationalizable.py 'input file'". For example, in this directory run "python3 rationalizable.py Ex1.txt". The output will be all the pairs of strategies for player 1 and player 2 that are rationalizable.

To find the Nash Equilibrium, run "python3 NashEq.py 'input file'". For example, in this directory run "python3 NashEq.py Ex1.txt". The output will be all the pairs of strategies for player 1 and player 2 that are in the Nash Equilibrium for the game.

To find the Mixed-Strategy Nash Equilibrium, run "python3 MixedEq.py 'input file'". For example, in this directory run "python3 MixedEq.py Ex1.txt". The output will be all the mixed strategy profile of each strategy for player 1 in line 1 and player 2 in line 2, where each value indicates the probability of the corresponding strategy. If only pure strategy is possible, it shows p(s) = 1 for the pure strategy s and 0 for all the other strategies.
