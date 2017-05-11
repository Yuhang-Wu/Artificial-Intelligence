"""
function MAX-VALUE(state) returns a utility value
    if TERMINAL-TEST(state) then return UTILITY(state)
    v <- -inf
    for each a in ACTIONS(state) do
        v <- MAX(v, MINI-VALUE(RESULT(s,a)))
    return v

function MINI-VALUE(state) returns a utility value
    if TERMINAL-TEST(state) then return UTILITY(state)
    v <- +inf
    for each a in ACTIONS(state) do
        v <- MIN(v, MAX-VALUE(RESULT(s,a)))
    return v
"""

def max_value(tree):
    v = float("-inf")
    if type(tree) == int:
        return tree
    
    for node in tree:
        v = max(v, min_value(node))
    return v
        
def min_value(tree):
    v = float("inf")
    if type(tree) == int:
        return tree   
    
    for node in tree:
        v = min(v, max_value(node))
    return v

def main():
    tree = 3
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree))    
    
    tree = [1, 2, 3]
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree))    
    
    tree = [1, 2, [3]]
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree))    
    
    tree = [[1, 2], [3]]
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree))    
    
    tree = [[1, 2], [3, 4]]
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree))   
    
    tree = [[2, 3, 4], [1, 100, -100]]
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree))    
    
    tree = [[3, 12, 8], [2, 4, 6], [14, 5, 2]]
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree))
    
    tree = [[[3, 12], 8], [2, [4, 6]], [14, 5, 2]]
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree)) 
    
    tree = [[1, 4], [3, 5], [2]]
    print("Game tree:", tree)
    print("Root utility for maximiser:", max_value(tree))
    print("Root utility for minimiser:", min_value(tree))    

if __name__ == '__main__':
    main()
