""" Naïve Bayes models are commonly used for classification. They are a special form of Bayesian networks, 
    therefore we could represent them with the same verbose data structure introduced in the previous quiz. 
    
    However, in this quiz we use a more compact representation that is more convenient for learning. 
    We can afford to have a simpler representation because the Bayesian network of all naïve Bayes models are very simple: 
    they are all a directed tree of depth one where the root is the class variable (target feature) 
    and the number of leaf nodes is equal to the number of input features in the problem.
    
    In this quiz, we assume that all the variables in a naïve Bayes network are binary. 
    For a network with n binary input features X[1] to X[n], we represent the conditional probability tables (CPTs) 
    that are required in the network, with the following two objects:
    
    prior: a real number representing p(Class=true). The probability p(Class=false) can be obtained by 1 - prior.
    likelihood: a tuple of length n where each element is a pair of real numbers such that 
        likelihood[i][False] is p(X[i]=true|C=false) and likelihood[i][True] is p(X[i]=true|C=true ). 
        That is, likelihood contains the 2*n CPTs that are required at leaf nodes.
    
    Write a function posterior(prior, likelihood, observation) that returns the posterior probability of 
    the class variable being true, given the observation; that is, it returns p(Class=true|observation). 
    The argument observation is a tuple of n Booleans such that observation[i] is the observed value (True or False) 
    for the input feature X[i]. 

"""

def posterior(prior, likelihood, observation):
    
    prb_true = prior
    prb_false = 1 - prior
    
    for n, node in enumerate(likelihood):
        false, true = node
        
        if observation[n]:
            prb_false *= false
            prb_true *= true
        else:
            prb_false *= 1 - false
            prb_true *= 1 - true            
   
    alpha = prb_false + prb_true
    probability = prb_true / alpha
    
    return probability

def main():
    prior = 0.05
    likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))
    
    #observation = (True, True, True)
    #observation = (True, False, True)
    #observation = (False, True, False)
    observation = (False, False, False)
    
    class_posterior_true = posterior(prior, likelihood, observation) 
    print("P(C=False|observation) is approximately {:.5f}"
          .format(1 - class_posterior_true))   
    print("P(C=True |observation) is approximately {:.5f}"
          .format(class_posterior_true))      

if __name__ == '__main__':
    main()
