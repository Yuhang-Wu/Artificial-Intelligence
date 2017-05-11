import csv

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
        

def main():

    prior = learn_prior("spam-labelled.csv")
    print("Prior probability of spam is {:.5f}.".format(prior))    
    
    prior = learn_prior("spam-labelled.csv")
    print("Prior probability of not spam is {:.5f}.".format(1 - prior))    
    
    prior = learn_prior("spam-labelled.csv", pseudo_count = 1)
    print(format(prior, ".5f"))
    
    prior = learn_prior("spam-labelled.csv", pseudo_count = 2)
    print(format(prior, ".5f"))    
    
    prior = learn_prior("spam-labelled.csv", pseudo_count = 10)
    print(format(prior, ".5f"))    
    
    prior = learn_prior("spam-labelled.csv", pseudo_count = 100)
    print(format(prior, ".5f"))    
    
    prior = learn_prior("spam-labelled.csv", pseudo_count = 1000)
    print(format(prior, ".5f"))    

if __name__ == '__main__':
    main()
