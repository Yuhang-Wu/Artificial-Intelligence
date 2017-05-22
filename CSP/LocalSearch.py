import itertools
import random

"""
    The following to have a random restart whenever the greedy descent reaches a local minimum. 
    The program can find a solution for large values of n (e.g. n = 50) in a reasonable time. 
    In the following program it is assumed that the function greedy_descent returns a solution if one is found 
    or None otherwise.
"""
def random_restart(n):
    random.seed(0) # seeding so that the results can be replicated.
    assignment = list(range(1, n+1))
    while not greedy_descent(tuple(assignment)):
        random.shuffle(assignment)
        

def conflict_count(indexs):
    conflicts = 0
    assignments = [(row, col) for row, col in enumerate(indexs)]
    
    for assign1, assign2 in itertools.combinations(assignments,2):
        if abs(assign1[0] - assign2[0]) == abs(assign1[1] - assign2[1]):
            conflicts += 1
    return conflicts  
    
"""    
print(conflict_count((1, 2)))
print(conflict_count((1, 3, 2)))
print(conflict_count((1, 2, 3)))
print(conflict_count((1,)))
print(conflict_count((1, 2, 3, 4, 5, 6, 7, 8)))
print(conflict_count((2, 3, 1, 4)))
"""


def neighbours(assignment):
    neighbors = []
    for row, col in itertools.combinations(range(len(assignment)),2):
        neighbor = list(assignment)
        neighbor[row], neighbor[col] = assignment[col], assignment[row]
        neighbors.append(tuple(neighbor))
    return neighbors

"""
print(list(neighbours((1, 2))))
print(sorted(neighbours((1, 3, 2))))
print(sorted(neighbours((1, 2, 3))))
print(list(neighbours((1,))))
for neighbour in sorted(neighbours((1, 2, 3, 4, 5, 6, 7, 8))):
    print(neighbour)
for neighbour in sorted(neighbours((2, 3, 1, 4))):
    print(neighbour)
for neighbour in sorted(neighbours((2, 3, 1, 4))):
    print(neighbour)
"""


def greedy_descent(assignment):
    
    current_conflict = conflict_count(assignment)
    print("Assignment:", assignment, "Number of conflicts:", current_conflict)
    
    if current_conflict == 0:
        print("A solution is found.")
        return 0
    
    next_neighbor = min(sorted(neighbours(assignment)), key=conflict_count)
    next_conflict = conflict_count(next_neighbor)
    
    if next_conflict < current_conflict:
        return greedy_descent(next_neighbor)
        
    print("A local minimum is reached.")
    
"""
greedy_descent((1, 2, 3, 4, 5, 6))
greedy_descent((6, 5, 3, 4, 2, 1))
greedy_descent((2, 1, 3, 4, 6, 5))
greedy_descent((1,))
greedy_descent((1, 2))
greedy_descent(tuple(range(1, 4)))
greedy_descent(tuple(range(1, 6)))
greedy_descent(tuple(range(1, 11)))
"""
