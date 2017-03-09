from search import *
import math

class LocationGraph(ExplicitGraph):
    def __init__(self, nodes, locations, edges, starting_list, goal_nodes, estimates=None):
        
        edge = set()
        for tail, head in edges:
            
            longitude = locations[tail][0] - locations[head][0]
            latitude = locations[tail][1] - locations[head][1]
            
            cost = math.sqrt(abs(longitude**2) + abs(latitude**2))
            
            edge.add((tail, head, cost))
            edge.add((head, tail, cost))
            
        edge_list = sorted(edge)
        ExplicitGraph.__init__(self, nodes, edge_list, starting_list, goal_nodes, estimates=None)
        
        
def main():
    
    #Example 1
    graph = LocationGraph(nodes=set('ABC'),
                          locations={'A': (0, 0),
                                     'B': (3, 0),
                                     'C': (3, 4)},
                          edges={('A', 'B'), ('B','C'),
                                 ('C', 'A')},
                          starting_list=['A'],
                          goal_nodes={'C'})
    
    
    for arc in graph.outgoing_arcs('A'):
        print(arc)
    
    for arc in graph.outgoing_arcs('B'):
        print(arc)
    
    for arc in graph.outgoing_arcs('C'):
        print(arc)    
        
        
    print('\n')
    #Example 2
    pythagorean_graph = LocationGraph(
        nodes=set("abc"),
        locations={'a': (5, 6),
                   'b': (10,6),
                   'c': (10,18)},
        edges=[tuple(s) for s in {'ab', 'ac', 'bc'}],
        starting_list=['a'],
        goal_nodes={'c'})
    
    for arc in pythagorean_graph.outgoing_arcs('a'):
        print(arc)    
        

if __name__ == "__main__":
    main()