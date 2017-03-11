import re
from search import *

def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    Author: Kourosh Neshatian
    Last Modified: 31 Jul 2015

    """
    ATOM   = r"[a-z][a-zA-z\d_]*"
    HEAD   = r"\s*(?P<HEAD>{ATOM})\s*".format(**locals())
    BODY   = r"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*".format(**locals())
    CLAUSE = r"{HEAD}(:-{BODY})?\.".format(**locals())
    KB     = r"^({CLAUSE})*$".format(**locals())

    #assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")

class KBGraph(Graph):
    def __init__(self, kb, query):
        self.KB = list(clauses(kb))
        self.query = query
        
    def is_goal(self, node):
            return True and not node or False    
        
    def starting_nodes(self):
        yield self.query
    
    def outgoing_arcs(self, tail_node):
        #print(tail_node)
        cur_node = tail_node.pop()
        #print(cur_node)
        for head, body in self.KB:
            if cur_node == head:
                yield Arc(tail_node, tail_node.union(body), None, 0)
                


class BFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty list."""
        self.container = []


    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self.container) == 0:
            raise StopIteration();
        return self.container.pop(0)


class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty list."""
        self.container = []


    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self.container) == 0:
            raise StopIteration();
        return self.container.pop()
    
    
def main():
    kb = """
    a :- b, c.
    b :- d, e.
    b :- g, e.
    c :- e.
    d.
    e.
    f :- a,
         g.
    """
    
    query = {'a'}
    if next(generic_search(KBGraph(kb, query), BFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")
        
        
    kb = """
    a :- b, c.
    b :- d, e.
    b :- g, e.
    c :- e.
    d.
    e.
    f :- a,
         g.
    """
            
    query = {'a', 'b', 'd'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")    
            
if __name__ == '__main__':
    main()
