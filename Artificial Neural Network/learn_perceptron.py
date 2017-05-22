def learn_perceptron(weights, bias, training_examples, learning_rate, max_epochs):
    
    for epoch in range(1, max_epochs + 1):
        #print("-" * 20, "epoch:", epoch, 20 * "-")
        #print("weights: ", weights)
        #print("bias: ", bias)
        seen_error = False
        
        
        for input, target in training_examples:
            a = bias + weights[0] * input[0] + weights[1] * input[1]
            output = int(a>=0)
            #print("input: {} output: {} target: {}".format(input, output, target))
            
            if output != target:
                seen_error = True
                # Now update the weights and bias
                weights[0] = weights[0] + learning_rate * input[0] * (target - output)
                weights[1] = weights[1] + learning_rate * input[1] * (target - output)
                bias = bias + learning_rate*(target-output)
                # print("updating the weights and bias to: ", weights, bias)

        if not seen_error:
            def perceptron(input_vector):
                a = bias + weights[0] * input_vector[0] + weights[1] * input_vector[1]
                output = int( a>=0)
                return output
            return perceptron
        

def main():
    weights = [2, -4]
    bias = 0
    learning_rate = 0.5
    examples = [
      ((0, 0), 0),
      ((0, 1), 0),
      ((1, 0), 0),
      ((1, 1), 1),
      ]
    max_epochs = 50
    
    classifier = learn_perceptron(weights, bias, examples, learning_rate, 50)
    if not classifier:
        print("No model could be learnt.")
    else:
        print(classifier((0,0)))
        print(classifier((0,1)))
        print(classifier((1,0)))
        print(classifier((1,1)))
        print(classifier((2,2)))
        print(classifier((-3,-3)))
        print(classifier((3,-1)))    
    
    
    weights = [2, -4]
    bias = 0
    learning_rate = 0.5
    examples = [
      ((0, 0), 0),
      ((0, 1), 1),
      ((1, 0), 1),
      ((1, 1), 0),
      ]
    max_epochs = 50
    
    classifier = learn_perceptron(weights, bias, examples, learning_rate, 50)
    if not classifier:
        print("No model could be learnt.")
    else:
        print(classifier((0,0)))
        print(classifier((0,1)))
        print(classifier((1,0)))
        print(classifier((1,1)))
        print(classifier((2,2)))
        print(classifier((-3,-3)))
        print(classifier((3,-1)))    
        
        
    weights = [1, 1]
    bias = -2
    learning_rate = 0.5
    examples = [
      ((0, 4), 0),
      ((-2, 1), 1),
      ((3, 5), 0),
      ((1, 1), 1),
      ]
    max_epochs = 50
    
    classifier = learn_perceptron(weights, bias, examples, learning_rate, 50)
    if not classifier:
        print("No model could be learnt.")
    else:
        print(classifier((0,4)))
        print(classifier((-2,1)))
        print(classifier((3,5)))
        print(classifier((1,1)))
        print(classifier((4,4)))
        print(classifier((-3,6)))
        print(classifier((3,-1)))            
          
if __name__ == "__main__":
    main()
