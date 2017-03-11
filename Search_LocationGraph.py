import math
import heapq
from search import *

class LocationGraph(ExplicitGraph):
    
    def __init__(self, nodes, locations, edges, starting_list, goal_nodes, estimates=None):
        
        edge_list = set()
        for tail, head in edges:
            
            longitude = abs(locations[tail][0] - locations[head][0])
            atitude = abs(locations[tail][1] - locations[head][1])
            cost = math.sqrt(math.pow(longitude, 2) + math.pow(atitude, 2))
            
            edge_list.add((tail, head, cost))
            edge_list.add((head, tail, cost))
            
        edge_list = sorted(edge_list)
        ExplicitGraph.__init__(self, nodes, edge_list, starting_list, goal_nodes)
        

class LCFSFrontier(Frontier):
    
    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty list."""
        self.container = []

    def add(self, path):
        total_cost = 0.0
        for edge in path:
            total_cost += edge.cost
        heapq.heappush(self.container, (total_cost, path))
        

    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self.container) == 0:
            raise StopIteration();
        solution = heapq.heappop(self.container)[1]
        return solution
        
        
def main():
    
    #Example 1 - LocationGraph
    graph = LocationGraph(nodes=set('ABC'),
                      locations={'A': (0, 0),
                                 'B': (3, 0),
                                 'C': (3, 4)},
                      edges={('A', 'B'), ('B','C'),
                             ('B', 'A'), ('C', 'A')},
                      starting_list=['A'],
                      goal_nodes={'C'})

    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)
    
    #Example 2 - LocationGraph
    graph = LocationGraph(nodes=set('ABC'),
                      locations={'A': (0, 0),
                                 'B': (3, 0),
                                 'C': (3, 4)},
                      edges={('A', 'B'), ('B','C'),
                             ('B', 'A')},
                      starting_list=['A'],
                      goal_nodes={'C'})

    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)
    
    #Example 3 - LocationGraph
    pythagorean_graph = LocationGraph(
    nodes=set("abc"),
    locations={'a': (5, 6),
               'b': (10,6),
               'c': (10,18)},
    edges=[tuple(s) for s in {'ab', 'ac', 'bc'}],
    starting_list=['a'],
    goal_nodes={'c'})

    solution = next(generic_search(pythagorean_graph, LCFSFrontier()))
    print_actions(solution)
    
    #Example 1 - LCFS
    graph = LocationGraph(nodes=set('ABC'),
                      locations={'A': (0, 0),
                                 'B': (3, 0),
                                 'C': (3, 4)},
                      edges={('A', 'B'), ('B','C'),
                             ('B', 'A'), ('C', 'A')},
                      starting_list=['A'],
                      goal_nodes={'C'})

    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)
    
    #Example 2 - LCFS
    graph = LocationGraph(nodes=set('ABC'),
                      locations={'A': (0, 0),
                                 'B': (3, 0),
                                 'C': (3, 4)},
                      edges={('A', 'B'), ('B','C'),
                             ('B', 'A')},
                      starting_list=['A'],
                      goal_nodes={'C'})

    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)
    
    #Example 3 - LCFS
    pythagorean_graph = LocationGraph(
    nodes=set("abc"),
    locations={'a': (5, 6),
               'b': (10,6),
               'c': (10,18)},
    edges=[tuple(s) for s in {'ab', 'ac', 'bc'}],
    starting_list=['a'],
    goal_nodes={'c'})

    solution = next(generic_search(pythagorean_graph, LCFSFrontier()))
    print_actions(solution)
    
if __name__ == "__main__":
    main()
