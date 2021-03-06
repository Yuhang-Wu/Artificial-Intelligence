""" In order to see how well your classifier (e.g. a spam filter) will perform on unseen data (email),
    we have to feed it with some unseen input data that have already been labeled by human users and then 
    see what proportion are classified correctly.
    Write a function accuracy(predicted_labels, correct_labels) that returns the accuracy of a classifier based on 
    the given arguments. Both arguments are tuples of the same length and contain class labels. 
    Class labels may be of any type as long as they can be tested for equality.
"""

def accuracy(predicted_labels, correct_labels):
    
    return len([n for n in range(len(predicted_labels)) if predicted_labels[n] == correct_labels[n]]) / len(correct_labels)


def main():
    print(accuracy((True, True, True, False),
                   (True, True, False, False)))    
    
if __name__ == '__main__':
    main()
