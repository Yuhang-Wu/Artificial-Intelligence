""" Write a function nb_classify(prior, likelihood, input_vector) that 
    takes the learnt prior and likelihood probabilities and classifies an (unseen) input vector. 
    The input vector will be a tuple of 12 integers (each 0 or 1) corresponding to attributes X1 to X12. 
    The function should return a pair (tuple) where the first is either "Spam" or "Not Spam" and the second is the certainty. 
    The certainty is the (posterior) probability of spam when the instance is classified as spam, 
    or the probability of 'not-spam' otherwise. If spam and 'not spam' are equally likely (i.e. p=0.5) then choose 'not spam'.

    This is a very simple function to implement as it only wraps the posterior function developed earlier.
    Supply the following functions you developed earlier: learn_prior and learn_likelihood. 
    Also include import statements and any other function that you may be using (e.g. posterior).
"""

import csv

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


def learn_prior(file_name, pseudo_count=0):
    
    total = 0
    is_spam = 0

    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]    
        
    for eachline in training_examples[1:]:
        if eachline[-1] == '1':
            is_spam += 1
        total += 1
        
    probability = (is_spam + pseudo_count) / (total + pseudo_count * 2)
        
    return probability


def learn_likelihood(file_name, pseudo_count=0):
    
    spams = 0
    likelihood = []
    false, true = 0, 1
    pairs = [[0,0] for i in range(12)]
    
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]
    
    for eachline in training_examples[1:]:
        
        is_spam = int(eachline[-1])
        if is_spam:
            spams += 1         
        
        for n, attribute in enumerate(eachline[:-1]):
            if int(attribute):
                if not is_spam:
                    pairs[n][false] += 1
                else:
                    pairs[n][true] += 1
        
    total = len(training_examples[1:])
    
    for false_num, true_num in pairs:
        not_spam = (false_num + pseudo_count) / (total - spams + 2 * pseudo_count)
        is_spam = (true_num + pseudo_count) / (spams + 2 * pseudo_count)
        likelihood.append((not_spam,is_spam))
    
    return likelihood


def nb_classify(prior, likelihood, input_vector):
    
    probability = posterior(prior, likelihood, input_vector)
    
    if probability <= 0.5:
        return ('Not Spam', 1-probability)
    elif probability > 0.5:
        return ('Spam', probability)
    

def main():
    
    prior = learn_prior("spam-labelled.csv")
    likelihood = learn_likelihood("spam-labelled.csv")

    input_vectors = [
        (1,1,0,0,1,1,0,0,0,0,0,0),
        (0,0,1,1,0,0,1,1,1,0,0,1),
        (1,1,1,1,1,0,1,0,0,0,1,1),
        (1,1,1,1,1,0,1,0,0,1,0,1),
        (0,1,0,0,0,0,1,0,1,0,0,0),
        ]

    predictions = [nb_classify(prior, likelihood, vector) 
                  for vector in input_vectors]

    for label, certainty in predictions:
        print("Prediction: {}, Certainty: {:.5f}"
              .format(label, certainty))
    
    
    prior = learn_prior("spam-labelled.csv", pseudo_count=1)
    likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)
    
    input_vectors = [
        (1,1,0,0,1,1,0,0,0,0,0,0),
        (0,0,1,1,0,0,1,1,1,0,0,1),
        (1,1,1,1,1,0,1,0,0,0,1,1),
        (1,1,1,1,1,0,1,0,0,1,0,1),
        (0,1,0,0,0,0,1,0,1,0,0,0),
        ]
    
    predictions = [nb_classify(prior, likelihood, vector) 
                   for vector in input_vectors]
    
    for label, certainty in predictions:
        print("Prediction: {}, Certainty: {:.5f}"
              .format(label, certainty))
        
if __name__ == '__main__':
    main()
