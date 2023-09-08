import numpy as np
import pandas as pd

class Game():
    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2
    
    def print_dom(self):
        if player == '1':
            player = self.player1
        elif player == '2':
            player = self.player2
        player1.dominated()
        
    def getBR(self,player,strategy):
        if player == '1':
            player = self.player1
            other = self.player2
        elif player == '2':
            other = self.player1
            player = self.player2
        strat_idx = player.get_idx(strategy)
        BR_payoff = np.amax(other.payoff[:,strat_idx])
        BR = np.where(other.payoff[:,strat_idx] == BR_payoff)
        
        return BR[0],np.array(other.strat)[BR[0]][0]
    
    def IESDS(self):
        finished = 0
        while finished == 0:
            finished = 1
            dom,compare = self.player1.dominated()
            if len(dom) > 0:
                finished = 0
                self.player1.update_payoff(dom,0)
                self.player2.update_payoff(dom,1)
                for index in sorted(list(dom), reverse=True):
                    del self.player1.strat[index]
                
            dom,compare = self.player2.dominated()
            if len(dom) > 0:
                finished = 0
                self.player1.update_payoff(dom,1)
                self.player2.update_payoff(dom,0)
                for index in sorted(list(dom), reverse=True):
                    del self.player2.strat[index]
                    
        return self.player1.strat,self.player2.strat
                    
    def rationalizable(self):
        finished = 0
        while finished == 0:
            finished = 1
            rat = set()
            for strat in self.player2.strat:
                rat.update(list(self.getBR('2',strat)[0]))
            if len(self.player1.strat) > len(rat):
                finished = 0
                strat_updated = [self.player1.strat[i] for i in sorted(list(rat))]
                dom = set()
                for j in range(self.player1.n):
                    if j not in rat:
                        dom.add(j)
                self.player1.update_payoff(dom,0)
                self.player2.update_payoff(dom,1)
                self.player1.strat = strat_updated
            
            rat = set()
            for strat in self.player1.strat:
                rat.update(list(self.getBR('1',strat)[0]))
            if len(self.player2.strat) > len(rat):
                finished = 0
                strat_updated = [self.player2.strat[i] for i in sorted(list(rat))]
                dom = set()
                for j in range(self.player2.n):
                    if j not in rat:
                        dom.add(j)
                self.player2.update_payoff(dom,0)
                self.player1.update_payoff(dom,1)
                self.player2.strat = strat_updated
        return self.player1.strat,self.player2.strat
                
    def Nash_Eq(self):
        self.rationalizable()
        strats1 = self.player1.strat
        strats2 = self.player2.strat
        
        strat_BR1 = [list(self.getBR('1',strat)[0]) for strat in strats1]
        strat_BR2 = [list(self.getBR('2',strat)[0]) for strat in strats2]
        
        nash_eq = []
        
        for i,j in enumerate(strat_BR1):
            for k in j:
                if i in strat_BR2[k]:
                    nash_eq.append((strats1[i],strats2[k]))
        return nash_eq
    
    def Mixed_Eq(self):
        self.rationalizable()
        strats1 = self.player1.strat
        strats2 = self.player2.strat
        
        A = self.player1.payoff
        B = self.player2.payoff
        
        n1,n2 = self.player1.payoff.shape
        
        x = SolveForMixed(A,n1,n2)
        mixed1 = []
        for strat in self.player1.full_strat:
            if strat in strats1:
                mixed1.append(x[strats1.index(strat)])
            else:
                mixed1.append(0)
        
        x = SolveForMixed(B,n2,n1)
        mixed2 = []
        for strat in self.player2.full_strat:
            if strat in strats2:
                mixed2.append(x[strats2.index(strat)])
            else:
                mixed2.append(0)
                
        return mixed1,mixed2
        
                      
                
class Player():
    def __init__(self,n,strat,payoff):
        self.n = n
        self.strat = strat
        self.full_strat = strat
        self.payoff = payoff
        
    def dominated(self):
        payoff_arr1 = self.payoff
        strat = self.strat
        dom = set()
        compare = []
        for i in range(0,self.n):
            for j in range(i+1,self.n):
                if np.all(payoff_arr1[i,:] > payoff_arr1[j,:]):
                    dom.add(j)
                    compare.append((strat[j],strat[i]))
                elif np.all(payoff_arr1[i,:] < payoff_arr1[j,:]):
                    dom.add(i)
                    compare.append((strat[i],strat[j]))
        return (dom,compare)

    def get_idx(self,strategy):
        return self.strat.index(strategy)
    
    def update_payoff(self,dom,axis):
        self.payoff = np.delete(self.payoff,list(dom),axis)
        self.n = self.payoff.shape[0]
    
def read_payoff(s):
    payoff = s.split(',')
    a = tuple(map(float,payoff))
    return a

def read_file(f):
    with open(f, "r") as file:
        newline_break = []
        for readline in file: 
            line_strip = readline.strip()
            newline_break.append(line_strip)
    return (newline_break)

def SolveForMixed(A,n1,n2):
    a = []
    b = []

    for i in range(0,n1):
        for j in range(i+1,n1):
            a.append(A[i]-A[j])
            b.append(0)
    a.append([1 for i in range(n2)])
    b.append(1)

    x = np.linalg.solve(a, b)
    return x

def makeGame(argv):
	try:
		f = argv[1]
	except IndexError:
		print("Please Enter a File!!")
		raise

	input_arr = read_file(f)

	n1 = int(input_arr[0])
	strat_str = input_arr[1]
	strategies1 = strat_str.split()

	n2 = int(input_arr[2])
	strat_str = input_arr[3]
	strategies2 = strat_str.split()

	payoff_arr = []
	for i in range(n1):
	    s = input_arr[4 + i]
	    payoff_str = s.split()
	    payoff = list(map(read_payoff,payoff_str))
	    payoff_arr.append(np.array(payoff))

	payoff_arr = np.array(payoff_arr)

	payoff_arr1 = payoff_arr[:,:,0]
	payoff_arr2 = payoff_arr[:,:,1]

	Player1 = Player(n1,strategies1,payoff_arr1)
	Player2 = Player(n2,strategies2,payoff_arr2.T)

	game = Game(Player1,Player2)

	return game,Player1,Player2