""" Write a function learn_likelihood(file_name, pseudo_count=0) that 
    takes the file name of a training set (for the spam detection problem) and an optional pseudo-count parameter 
    and returns a sequence of pairs of likelihood probabilities. As described in the representation of likelihood, 
    the length of the returned sequence (list or tuple) must be 12. Each element in the sequence is a pair (tuple) 
    of real numbers such that 
    likelihood[i][False] is P(X[i]=true|Spam=false) and likelihood[i][True] is P(X[i]=true|Spam=true ).
"""

import csv   

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

def main():
    
    likelihood = learn_likelihood("spam-labelled.csv")
    print(len(likelihood))
    print([len(item) for item in likelihood])	    
    
    likelihood = learn_likelihood("spam-labelled.csv")
    print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
    print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
    print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
    print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))    
    
    likelihood = learn_likelihood("spam-labelled.csv")
    print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
    print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
    print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
    print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))
    
    # Laplace smoothing using pseudo_count
    likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)
    print("With Laplacian smoothing:")
    print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
    print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
    print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
    print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))    
    

if __name__ == '__main__':
    main()
