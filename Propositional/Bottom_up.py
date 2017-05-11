import re

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
        

def forward_deduce(KB):
    """ Takes the string of KB containing propositional definite clauses
        and returns a set of atoms that can be derived fron the KB
    """
    kb = list(clauses(KB))
    logical = set()
    no_more_clause = False
    
    while not no_more_clause:
        no_more_clause = True
        
        for head, body in kb:
            if all(atom in logical for atom in body) and head not in logical:
                logical.add(head)
                no_more_clause = False
    return logical


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
   
    print(", ".join(sorted(forward_deduce(kb))))
    
if __name__ == '__main__':
    main()
