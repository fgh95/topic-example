from ..dungeon import Dungeon

def test_dungeon():
	d1 = Dungeon([1],0,2,[[1],[0,2],[1]])
	d1.update_dungeon()