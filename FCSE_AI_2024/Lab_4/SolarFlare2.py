import math
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder
#from Lab_3.zad2_dataset import dataset

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset


if __name__ == '__main__':
    percent = int(input())/100


    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset[int(len(dataset) * (1 - percent)):]
    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]
    train_X = encoder.transform(train_X)

    test_set = dataset[:int(len(dataset) * (1 - percent))]
    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]
    test_X = encoder.transform(test_X)

    clf = DecisionTreeClassifier(criterion=input(), random_state=0)
    clf.fit(train_X, train_Y)

    print('Depth:', clf.get_depth())
    print('Number of leaves:', clf.get_n_leaves())
    print('Accuracy:', clf.score(test_X, test_Y))
    feature_importances = list(clf.feature_importances_)
    print('Most important feature:', feature_importances.index(max(feature_importances)))
    print('Least important feature:', feature_importances.index(min(feature_importances)))

    submit_train_data(train_X, train_Y)
    submit_test_data(test_X, test_Y)
    submit_classifier(clf)
    submit_encoder(encoder)

