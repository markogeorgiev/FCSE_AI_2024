import os
from sklearn.naive_bayes import *
from zad2_dataset import dataset

os.environ['OPENBLAS_NUM_THREADS'] = '1'
#from submission_script import *
#from dataset_script import dataset

if __name__ == '__main__':

    dataset_v2 = []

    for row in dataset:
        row_v2 = [float(el) for el in row]
        dataset_v2.append(row_v2)

    dataset = dataset_v2

    train_set = dataset[:int(0.85 * len(dataset))]
    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]

    test_set = dataset[int(0.85 * len(dataset)):]
    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]

    classifier = GaussianNB()

    classifier.fit(train_X, train_Y)

    print(classifier.score(test_X, test_Y))
    entry = [float(el) for el in input().split(' ')]

    predicted_class = classifier.predict([entry])

    print(int(predicted_class[0]))
    print(classifier.predict_proba([entry]))

    #submit_train_data(train_X, train_Y)
    #submit_test_data(test_X, test_Y)
    #submit_classifier(classifier)
    #submit_encoder(encoder)
