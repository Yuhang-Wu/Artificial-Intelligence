from search import *
import math
import heapq

class MapGraph(Graph):
    def __init__(self, map_str):
        map_list = list(map_str)
        self.rows = []
        each_row = []
        
        for element in map_list:
            if element != '\n':
                each_row.append(element)
            else:
                self.rows.append(each_row)
                each_row = []
                                
    def is_goal(self, node):
        for row in self.rows:
            if 'G' in row:
                coordinate = (self.rows.index(row), row.index('G'))
                return True and node == coordinate or False
    
    
    def starting_nodes(self):
        starting_points = []
        
        for row in self.rows:
            for col, node in enumerate(row):
                if node == 'S':
                    starting_points.append((self.rows.index(row), col))
        return starting_points
    
    
    def outgoing_arcs(self, tail_node):
        row, col = tail_node
        valid_position = [' ', 'S', 'G']
        movement = [('N' , -1, 0),
                    ('NE', -1, 1),
                    ('E' ,  0, 1),
                    ('SE',  1, 1),
                    ('S' ,  1, 0),
                    ('SW',  1, -1),
                    ('W' ,  0, -1),
                    ('NW', -1, -1)]
            
        for direction, move_row, move_col in movement:
            cur_row = row + move_row
            cur_col = col + move_col
            cur_point = self.rows[cur_row][cur_col]
                
            if cur_point in valid_position:
                yield Arc(tail_node,(cur_row, cur_col), direction, cost=1)  
    
    
    def estimated_cost_to_goal(self, node):
        row_n, col_n = node
            
        for row in self.rows:
            for col in row:
                if col == 'G':
                    #h_cost = max(abs(self.rows.index(row)-row_n), 
                                 #abs(row.index(col)-col_n))
                    h_cost = math.sqrt(pow(self.rows.index(row)-row_n, 2) + 
                                       pow(row.index(col)-col_n,2))
                    
        return h_cost
    
    
class AStarFrontier(Frontier):
    def __init__(self, map_graph):
        """ Initialized with an instance of a graph. A* frontier need to 
            access the estimated_cost_to_goal method of the graph object
        """
        self.map_graph = map_graph
        self.container = []
        self.visited = []
        self.FIFO = 0
        
    def add(self, path):
        f_cost = 0
        actual_cost = 0
        cur_head = path[-1].head
        h_cost = self.map_graph.estimated_cost_to_goal(cur_head)
        
        for edge in path:
            actual_cost += edge.cost

        f_cost = actual_cost + h_cost
        heapq.heappush(self.container,(f_cost, self.FIFO, path))
        self.FIFO += 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        while len(self.container) > 0:
            solution = heapq.heappop(self.container)[-1]   
            if solution[-1].head not in self.visited:
                self.visited.append(solution[-1].head)
                return solution
        raise StopIteration();


class LCFSFrontier(Frontier):
    
    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty list."""
        self.container = []
        self.visited = []
        self.FIFO = 0 #not necessary, adjust for lab

    def add(self, path):
        total_cost = 0.0
        for edge in path:
            total_cost += edge.cost
        heapq.heappush(self.container, (total_cost,self.FIFO, path))
        self.FIFO += 1
        

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.container) == 0:
            raise StopIteration();
        solution = heapq.heappop(self.container)[-1]
        
        if solution[-1] not in self.visited:
            self.visited.append(solution[-1].head)
        return solution


def print_map(map_graph, frontier, solution):
    
    SG = {'S', 'G'}
    star, dot = '*', '.'
    cur_row, cur_col = 0, 0
    
    if solution:
        for row in map_graph.rows:
            for col in row:
                cur_pos = (cur_row, cur_col)
                
                for edge in solution:
                    head_row, head_col = edge.head
                    
                    if cur_pos == edge.head \
                       and map_graph.rows[head_row][head_col] not in SG:
                        map_graph.rows[head_row][head_col] = star
                        
                for visit in frontier.visited:
                    visit_row, visit_col = visit
                    if visit == cur_pos \
                       and map_graph.rows[visit_row][visit_col] not in SG \
                       and map_graph.rows[visit_row][visit_col] != star:
                        map_graph.rows[visit_row][visit_col] = dot
                
                cur_col += 1
            cur_row, cur_col = cur_row + 1, 0
            
    for row in map_graph.rows:
        print(''.join(row))
        
        
def main():
    
    
    # ~~~~~~~~~~~~~~~~~~~~ A* Frontier ~~~~~~~~~~~~~~~~~~~~
    map_str = """\
+----------+
|    X     |
| S  X  G  |
|    X     |
+----------+
"""
    
    map_graph = MapGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)    
    
    map_str = """\
+---------+
|         |
|    G    |
|         |
+---------+
"""
    
    map_graph = MapGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)   
    
    map_str = """\
+----+
| S  |
| SX |
| X G|
+----+
"""
    
    map_graph = MapGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)    
    
    map_str = """\
+--+
|GS|
+--+
"""
    map_graph = MapGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution) 
    
    map_str = """\
+-------+
|     XG|
|X XXX  |
| S     |
+-------+
"""
    
    map_graph = MapGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)    
    
    
     # ~~~~~~~~~~~~~~~~~~~~ print graph ~~~~~~~~~~~~~~~~~~~~
    map_str = """\
+-------+
|     XG|
|X XXX  |
| S     |
+-------+
"""
    map_graph = MapGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution) 
    
    map_str = """\
+--+
|GS|
+--+
"""
    map_graph = MapGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)    
    
    map_str = """\
+----+
|    |
| SX |
| X G|
+----+
"""
    
    map_graph = MapGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)    
    
    map_str = """\
+------------+
|            |
|            |
|            |
|    S       |
|            |
|            |
| G          |
|            |
+------------+
"""
    
    map_graph = MapGraph(map_str)
    frontier = LCFSFrontier()
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)  
    
    map_str = """\
+------------+
|            |
|            |
|            |
|    S       |
|            |
|            |
| G          |
|            |
+------------+
"""
    
    map_graph = MapGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)   
    
    map_str = """\
+---------------+
|    G          |
|XXXXXXXXXXXX   |
|           X   |
|  XXXXXX   X   |
|  X S  X   X   |
|  X        X   |
|  XXXXXXXXXX   |
|               |
+---------------+
"""
    
    map_graph = MapGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)    
    
    map_str = """\
+---------+
|         |
|    G    |
|         |
+---------+
"""
    
    map_graph = MapGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution) 
    
    map_str = """\
+-------------+
|         G   |
| S           |
|         S   |
+-------------+
"""
    
    map_graph = MapGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)    
if __name__ == '__main__':
    main()
