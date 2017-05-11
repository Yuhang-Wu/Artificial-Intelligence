""" Write a function joint_prob(network, assignment) that 
    given a belief network and a complete assignment of all the variables in the network, 
    returns the probability of the assignment (being true). The data structure of the network is as described above. 
    The assignment is a dictionary where keys are the variable names and the values are either True or False.
"""

def joint_prob(network, assignment):
    
    probability = 1
    
    for key, value in network.items():
        parent_value = tuple([assignment[parent] for parent in value['Parents']]) 
        
        if assignment[key]:
            probability *= network[key]['CPT'][(parent_value)]
        else:
            probability *= 1 - network[key]['CPT'][(parent_value)]
            
    return probability

""" Write a function query(network, query_var, evidence) that given a belief network, 
    the name of a variable in the network, and some evidence, returns the posterior distribution of query_var. 
    The parameter network is a belief network whose data structure was described earlier. 
    The parameter query_var is the name of the variable we are interested in and is of type string. 
    The parameter evidence is a dictionary whose elements are assignments to some variables in the network; 
    the keys are the name of the variables and the values are Boolean.
    
    The function must return a pair of real numbers where 
    the first element is the probability of query_var being false given the evidence and 
    the second element is the probability of query_var being true given the evidence.

"""

def query(network, query_var, evidence):
    
    answer = {}
    selected = {}
    assignment = evidence.copy() #or can just use: assignment = evidence
    query_val = [True, False]
    hidden_vars = network.keys() - evidence.keys() - {query_var} #hint   
    
    for state in query_val:
        sum_hidden = 0
        
        for values in itertools.product((True, False), repeat=len(hidden_vars)):
            hidden_assignments = {var:val for var,val in zip(hidden_vars, values)} #hint
            
            assignment[query_var] = state
            assignment.update(hidden_assignments)
            
            sum_hidden+= joint_prob(network, assignment)
        
        selected[state] = sum_hidden
    
    for state in query_val:
        answer[state] = selected[state] / sum(selected.values())
    return answer

def main():  
    # --------------- --------------- test for joint_prob(network, assignment) --------------- ---------------
    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.2
                }},
    }
    
    p = joint_prob(network, {'A': True})
    print("{:.5f}".format(p))    
    
    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.2
                }},
    }
    
    p = joint_prob(network, {'A': False})
    print("{:.5f}".format(p))    
    
    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.1
                }},
                
        'B': {
            'Parents': ['A'],
            'CPT': {
                (True,): 0.8,
                (False,): 0.7,
                }},
        }
     
    p = joint_prob(network, {'A': False, 'B':True})
    print("{:.5f}".format(p))     
    
    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.1
                }},
                
        'B': {
            'Parents': ['A'],
            'CPT': {
                (True,): 0.8,
                (False,): 0.7,
                }},
        }
     
    p = joint_prob(network, {'A': False, 'B':False})
    print("{:.5f}".format(p))    
    
    network = {
        'Burglary': {
            'Parents': [],
            'CPT': {
                (): 0.001
                }},
                
        'Earthquake': {
            'Parents': [],
            'CPT': {
                (): 0.002,
                }},
        'Alarm': {
            'Parents': ['Burglary','Earthquake'],
            'CPT': {
                (True,True): 0.95,
                (True,False): 0.94,
                (False,True): 0.29,
                (False,False): 0.001,
                }},
    
        'John': {
            'Parents': ['Alarm'],
            'CPT': {
                (True,): 0.9,
                (False,): 0.05,
                }},
    
        'Mary': {
            'Parents': ['Alarm'],
            'CPT': {
                (True,): 0.7,
                (False,): 0.01,
                }},
        }
    
    p = joint_prob(network, {'John': True, 'Mary': True,
                             'Alarm': True, 'Burglary': False,
                             'Earthquake': False})
    print("{:.8f}".format(p))      
    
    # --------------- --------------- test for query(network, query_var, evidence) --------------- ---------------
    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.2
                }},
    }
    
    answer = query(network, 'A', {})
    print("P(A=true)={:.5f}".format(answer[True]))
    print("P(A=false)={:.5f}".format(answer[False]))    
    
    network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
            
    'B': {
        'Parents': ['A'],
        'CPT': {
            (True,): 0.8,
            (False,): 0.7,
            }},
    }
 
    answer = query(network, 'B', {'A': False})
    print("P(B=true|A=false) = {:.5f}".format(answer[True]))
    print("P(B=false|A=false) = {:.5f}".format(answer[False])) 
    
    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.1
                }},
                
        'B': {
            'Parents': ['A'],
            'CPT': {
                (True,): 0.8,
                (False,): 0.7,
                }},
        }
     
    answer = query(network, 'B', {})
    print("P(B=true) = {:.5f}".format(answer[True]))
    print("P(B=false) = {:.5f}".format(answer[False]))    
    
    
    network = {
        'Burglary': {
            'Parents': [],
            'CPT': {
                (): 0.001
                }},
                
        'Earthquake': {
            'Parents': [],
            'CPT': {
                (): 0.002,
                }},
        'Alarm': {
            'Parents': ['Burglary','Earthquake'],
            'CPT': {
                (True,True): 0.95,
                (True,False): 0.94,
                (False,True): 0.29,
                (False,False): 0.001,
                }},
    
        'John': {
            'Parents': ['Alarm'],
            'CPT': {
                (True,): 0.9,
                (False,): 0.05,
                }},
    
        'Mary': {
            'Parents': ['Alarm'],
            'CPT': {
                (True,): 0.7,
                (False,): 0.01,
                }},
        }
    
    answer = query(network, 'Burglary', {'John': True, 'Mary': True})
    print("Probability of a burglary when both\n"
          "John and Mary have called: {:.3f}".format(answer[True]))     
    
    
    network = {
        'Burglary': {
            'Parents': [],
            'CPT': {
                (): 0.001
                }},
                
        'Earthquake': {
            'Parents': [],
            'CPT': {
                (): 0.002,
                }},
        'Alarm': {
            'Parents': ['Burglary','Earthquake'],
            'CPT': {
                (True,True): 0.95,
                (True,False): 0.94,
                (False,True): 0.29,
                (False,False): 0.001,
                }},
    
        'John': {
            'Parents': ['Alarm'],
            'CPT': {
                (True,): 0.9,
                (False,): 0.05,
                }},
    
        'Mary': {
            'Parents': ['Alarm'],
            'CPT': {
                (True,): 0.7,
                (False,): 0.01,
                }},
        }
    
    answer = query(network, 'John', {'Mary': True})
    print("Probability of John calling if\n"
          "Mary has called: {:.5f}".format(answer[True])) 
    
    
if __name__ == '__main__':
    main()
