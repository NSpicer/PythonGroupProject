import random

def tossCoin():
	coin=random.random
	heads=0
    	tails=0
    	if coin<.5:
    		heads=heads+1
    	else:
        	tails=tails+1
    	print heads
    	print tails

for i in range(10):
    tossCoin
        
