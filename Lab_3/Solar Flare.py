import os
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB

from zad1_dataset import dataset

os.environ['OPENBLAS_NUM_THREADS'] = '1'
#from submission_script import *
#from dataset_script import dataset

dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset[:int(0.75 * len(dataset))]
    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]
    train_X = encoder.transform(train_X)

    test_set = dataset[int(0.75 * len(dataset)):]
    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]
    test_X = encoder.transform(test_X)

    classifier = CategoricalNB()

    classifier.fit(train_X, train_Y)
    classifier.predict_proba(test_X)

    accuracy = 0

    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_X[i]])[0]
        true_class = test_Y[i]
        if predicted_class == true_class:
            accuracy += 1

    print(classifier.score(test_X, test_Y))
    entry = [el for el in input().split(' ')]
    encoded_entry = encoder.transform([entry])
    predicted_class = classifier.predict(encoded_entry)
    print(predicted_class[0])
    print(classifier.predict_proba(encoded_entry))


    # submit_train_data(train_X, train_Y)
    # submit_test_data(test_X, test_Y)
    # submit_classifier(classifier)
    # submit_encoder(encoder)
