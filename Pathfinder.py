from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

class Pathfinder:
    def __init__(self, new_matrix, new_start_pos, new_end_pos):
        self.matrix = new_matrix
        self.grid = Grid(matrix = self.matrix)
        self.start_pos = new_start_pos
        self.end_pos = new_end_pos
        self.start_x = int(self.start_pos[0] // 70)
        self.start_y = int(self.start_pos[1] // 70)
        self.end_x = int(self.end_pos[0] // 70)
        self.end_y = int(self.end_pos[1] // 70)
        self.path = []


    def update(self):
        pass

    def find_path(self):
        start = self.grid.node(1,1)
        end = self.grid.node(4,5)
        finder = AStarFinder(diagonal_movement = DiagonalMovement.always)
        self.path, _ = finder.find_path(start, end, self.grid)
        self.grid_cleanup()
        #print(self.grid)
        #print(self.path)
        
        