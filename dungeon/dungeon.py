import copy
import random

class Dungeon(object):

	def __init__(self,treasure,adventurer,troll,network):
		self.treasure = treasure
		self.adventurer = adventurer
		self.troll = troll
		self.network = network


	def update_dungeon(self):
		self.adventurer=random_move(self.network, self.adventurer)
		self.troll=random_move(self.network, self.troll)

	def outcome(self):
	    if self.adventurer==self.troll:
	        return -1
	    if self.adventurer in self.treasure:
	        return 1
	    return 0

	def run_to_result(self):
	    dungeon=copy.deepcopy(self)
	    max_steps=1000
	    for _ in range(max_steps):
	        result= outcome(dungeon)
	        if result != 0:
	            return result
	        update_dungeon(dungeon)
	    # don't run forever, return 0 (e.g. if there is no treasure and the troll can't reach the adventurer)
	    return result


def random_move(network, current_loc):
	targets=network[current_loc]
	return random.choice(targets)


def success_chance(dungeon):
    trials=10000
    successes=0
    for _ in range(trials):
        outcome = run_to_result(dungeon)
        if outcome == 1:
            successes+=1
    success_fraction = successes/trials
    return success_fraction