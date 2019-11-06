from ..dungeon import Dungeon

def test_dungeon():
	d1 = Dungeon([4],0,1,[[1],[2,3],[1],[2,3],[1,2]])
	d1.update_dungeon()