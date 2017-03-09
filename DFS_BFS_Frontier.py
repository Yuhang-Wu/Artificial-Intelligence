""" DFS && BFS Algorithm """

from search import *


class FunkyNumericGraph(Graph):
    """A graph where nodes are numbers. A node (number) n leads to n-1 and
    n+2. Nodes that are divisible by 10 are goal nodes."""
    
    def __init__(self, starting_number):
        self.starting_number = starting_number

    def outgoing_arcs(self, tail_node):
        yield Arc(tail_node, tail_node - 1, label="1down", cost=1)
        yield Arc(tail_node, tail_node + 2, label='2up', cost=1)

    def starting_nodes(self):
        yield self.starting_number

    def is_goal(self, node):
        return True and node % 10 == 0 or False


class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty list."""
        self.container = []


    def add(self, path):
        #raise NotImplementedError
        #print('current path:', path) #
        self.container.append(path)
        #print('the current self.container is --->', self.container) #

    def __iter__(self):
        #raise NotImplementedError
        return self
    
    def __next__(self):
        if len(self.container) == 0:
            raise StopIteration();
        return self.container.pop()
    
    
class BFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty list."""
        self.container = []


    def add(self, path):
        #raise NotImplementedError
        #print('current path:', path) #
        self.container.append(path)
        #print('the current self.container is --->', self.container) #

    def __iter__(self):
        #raise NotImplementedError
        return self
    
    def __next__(self):
        if len(self.container) == 0:
            raise StopIteration();
        return self.container.pop(0)
  
    
class OrderedExplicitGraph(ExplicitGraph):
    def __init__(self, nodes, edges, starting_list, goal_nodes, estimates=None):
        edge_list = sorted(edges, reverse = True)
        
        ExplicitGraph.__init__(self, nodes, edge_list, starting_list, goal_nodes)

def main():
    """
    # Example 1 - DFS
    graph = ExplicitGraph(nodes=set('SAG'),
                          edge_list=[('S','A'), ('S', 'G'), ('A', 'G')],
                          starting_list=['S'],
                          goal_nodes={'G'})
    solutions = generic_search(graph, DFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)
    
    # Example 2 - DFS
    graph = ExplicitGraph(nodes=set('SAG'),
                          edge_list=[('S', 'G'), ('S','A'), ('A', 'G')],
                          starting_list=['S'],
                          goal_nodes={'G'})
    solutions = generic_search(graph, DFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)
    
    #Example 3 - DFS
    available_flights = ExplicitGraph(
        nodes=['Christchurch', 'Auckland', 
               'Wellington', 'Gold Coast'],
        edge_list=[('Christchurch', 'Gold Coast'),
                   ('Christchurch','Auckland'),
                   ('Christchurch','Wellington'),
                   ('Wellington', 'Gold Coast'),
                   ('Wellington', 'Auckland'),
                   ('Auckland', 'Gold Coast')],
        starting_list=['Christchurch'],
        goal_nodes={'Gold Coast'})
    
    my_itinerary = next(generic_search(available_flights, DFSFrontier()), None)
    print_actions(my_itinerary)    
    
    #Example 4 - DFS
    graph = ExplicitGraph(nodes=set('SAG'),
                          edge_list=[('S', 'G'), ('S','A'),
                                     ('A', 'S'), ('A', 'G')],
                          starting_list=['S'],
                          goal_nodes={'G'})
    
    solutions = generic_search(graph, DFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)    
    
    #Example 5 - DFS
    graph = ExplicitGraph(nodes=['Knowledge',
                                 'Commerce',
                                 'Wisdom',
                                 'Wealth',
                                 'Happiness'],
                          edge_list=[('Knowledge', 'Wisdom'),
                                 ('Commerce', 'Wealth'),
                                 ('Happiness', 'Happiness')],
                          starting_list=['Commerce'],
                          goal_nodes={'Happiness'})
    
    solutions = generic_search(graph, DFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)    
    
    #Example 6 - BFS
    graph = ExplicitGraph(nodes=set('SAG'),
                          edge_list = [('S','A'), ('S', 'G'), ('A', 'G')],
                          starting_list = ['S'],
                          goal_nodes = {'G'})
    
    solutions = generic_search(graph, BFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)    
    
    #Example 7 - BFS
    flights = ExplicitGraph(nodes=['Christchurch', 'Auckland', 
                                   'Wellington', 'Gold Coast'],
                            edge_list = [('Christchurch', 'Gold Coast'),
                                     ('Christchurch','Auckland'),
                                     ('Christchurch','Wellington'),
                                     ('Wellington', 'Gold Coast'),
                                     ('Wellington', 'Auckland'),
                                     ('Auckland', 'Gold Coast')],
                            starting_list = ['Christchurch'],
                            goal_nodes = {'Gold Coast'})
    
    my_itinerary = next(generic_search(flights, BFSFrontier()), None)
    print_actions(my_itinerary)    
    
    #Example 8 - BFS
    flights = ExplicitGraph(nodes=['Christchurch', 'Auckland',
                                   'Wellington', 'Gold Coast'],
                            edge_list = [('Christchurch', 'Gold Coast'),
                                     ('Christchurch','Auckland'),
                                     ('Christchurch','Wellington'),
                                     ('Wellington', 'Gold Coast'),
                                     ('Wellington', 'Auckland'),
                                     ('Auckland', 'Gold Coast')],
                            starting_list = ['Christchurch'],
                            goal_nodes = {'Gold Coast'})
    
    my_itinerary = next(generic_search(flights, BFSFrontier()), None)
    print_actions(my_itinerary)   
    
    #Example 9 - BFS
    graph = ExplicitGraph(nodes=set('SABG'),
                          edge_list = [('S','A'), ('S', 'B'),
                                   ('B','S'), ('A', 'G')],
                          starting_list = ['S'],
                          goal_nodes = {'G'})
    
    solutions = generic_search(graph, BFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)    
    
    #Example 10 - OrderedExplicitGraph
    graph = OrderedExplicitGraph(nodes=set('SAG'),
                                 edges={('S','A'), ('S', 'G'), ('A', 'G')},
                                 starting_list=['S'],
                                 goal_nodes={'G'})
    
    solutions = generic_search(graph, DFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)    
    
    #Example 11 - OrderedExplicitGraph
    graph = OrderedExplicitGraph(nodes=set('SAG'),
                                 edges={('S', 'G'), ('S','A'), ('A', 'G')},
                                 starting_list=['S'],
                                 goal_nodes={'G'})
    
    solutions = generic_search(graph, DFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)    

    #Example 12 - OrderedExplicitGraph
    graph = OrderedExplicitGraph(nodes=set('SABG'),
                                 edges={('S', 'A'), ('S','B'),
                                        ('B', 'S'), ('A', 'G')},
                                 starting_list=['S'],
                                 goal_nodes={'G'})
    
    solutions = generic_search(graph, DFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)    

    #Example 13 - OrderedExplicitGraph
    flights = OrderedExplicitGraph(nodes={'Christchurch', 'Auckland',
                                          'Wellington', 'Gold Coast'},
                                   edges={('Christchurch', 'Gold Coast'),
                                          ('Christchurch','Auckland'),
                                          ('Christchurch','Wellington'),
                                          ('Wellington', 'Gold Coast'),
                                          ('Wellington', 'Auckland'),
                                          ('Auckland', 'Gold Coast')},
                                   starting_list=['Christchurch'],
                                   goal_nodes={'Gold Coast'})
    
    my_itinerary = next(generic_search(flights, DFSFrontier()), None)
    print_actions(my_itinerary)    
    """
    
    #Example 14 - FunkyNumbericGraph
    graph = FunkyNumericGraph(4)
    for node in graph.starting_nodes():
        print(node)    
    
    #Example 15 - FunkyNumbericGraph
    graph = FunkyNumericGraph(4)
    for arc in graph.outgoing_arcs(7):
        print(arc)    
        
    #Example 15 - FunkyNumbericGraph
    graph = FunkyNumericGraph(3)
    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(solutions))
    print()
    print_actions(next(solutions))    
    
    #Example 15 - FunkyNumbericGraph
    from itertools import dropwhile
    
    graph = FunkyNumericGraph(3)
    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(dropwhile(lambda path: path[-1].head <= 10, solutions)))    
        
if __name__ == "__main__":
    main()