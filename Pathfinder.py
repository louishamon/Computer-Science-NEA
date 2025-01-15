from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

class Pathfinder:
    def __init__(self, new_matrix, new_start_pos, new_end_pos):
        self.matrix = new_matrix
        self.grid = Grid(matrix = self.matrix)
        self.start_pos = new_start_pos
        self.end_pos = new_end_pos
        self.start_x = self.start_pos[0] / 70
        self.start_y = self.start_pos[1] / 70
        self.end_x = self.end_pos[0] // 70
        self.end_y = self.end_pos[1] // 70
        self.path = []


    def update(self):
        pass

    def find_path(self):
        #print(self.start_x, self.start_y)
        start = self.grid.node(self.start_x, self.start_y)
        end = self.grid.node(self.end_x, self.end_y)
        finder = AStarFinder(diagonal_movement = DiagonalMovement.always)
        self.path = finder.find_path(start, end, self.grid)
        print(self.path)


    
