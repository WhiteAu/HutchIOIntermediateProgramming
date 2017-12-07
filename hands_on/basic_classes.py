import numpy as np

class Estimator():
    def __init__(self):
        '''
        Insert variable declarations here!
        Self.whatever = None
        '''

    def train(self, train_x, train_y):
        '''
        A training function that wraps the call to your linear regression model,
        and does some basic checking of dimensionality (AKA dim(x) is compatible with dim(y))

        :param train_x:
        :param train_y:
        :return some indicator of success if you complete, otherwise, throw some sort of descriptive error:
        '''

        return None

    def predict(self, test_x):
        '''

        :param test_x: a 2-d array modeling the variables/features of interest in our model. should be a compatible dimension as
        train_x from the train() call.
        :return: a vector/1-d array of predictions for each instance of test_x
        '''

        return None





def main():
    '''
    put your test loop here. It should create a new Estimator, train it, and predict some new dataset.

    '''

if __name__ == "__main__":
    '''
    the above is a common bit of code that will conditionally run whatever is within the conditional statement
    if the file it is in is the main entry point into the code 
    IE: it is invoked like 
    >: python basic_classes.py
    '''

    main()