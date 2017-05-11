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