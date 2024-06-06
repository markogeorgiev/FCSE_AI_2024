import os
from sklearn.ensemble import RandomForestClassifier

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset



if __name__ == '__main__':
    col_to_remove = int(input())

    clf = RandomForestClassifier(n_estimators=int(input()), criterion=input(), random_state=0)

    new_dataset = []
    for row in dataset:
        new_row = row[:col_to_remove] + row[col_to_remove + 1:]
        new_dataset.append(new_row)

    dataset = new_dataset

    train_set = dataset[:int(len(dataset) * 0.85)]
    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]

    test_set = dataset[int(len(dataset) * 0.85):]
    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]

    clf.fit(train_X, train_Y)
    print(f'Accuracy: {clf.score(test_X, test_Y)}')

    data = input().split()
    new_data =[float(num_str) for num_str in data]

    d_new_data = new_data[:col_to_remove] + new_data[col_to_remove + 1:]

    print(clf.predict([d_new_data])[0])
    print(clf.predict_proba([d_new_data])[0])

    submit_train_data(train_X, train_Y)
    submit_test_data(test_X, test_Y)
    submit_classifier(clf)
