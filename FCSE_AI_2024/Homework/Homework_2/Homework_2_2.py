from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.tree import export_text
# For image generation
import matplotlib.pyplot as plt
"""
For mapping the variables, this was used:
    Age: <30 = 1, [30,60] = 2, >60 = 3
    Diagnosis: SS = 1, FS = 2
    Astigmatism: N = 0, Y = 1
    Lens Type: SOFT = 0, RIGID = 1
"""
dataset = [
    [1, 1, 0],
    [1, 1, 1],
    [1, 2, 0],
    [1, 2, 1],
    [2, 1, 0],
    [2, 1, 1],
    [2, 2, 0],
    [2, 2, 0],
    [3, 1, 1],
    [3, 2, 1]
]

classes = [0, 1, 0, 1, 0, 1, 0, 1, 1, 0]

clf = DecisionTreeClassifier()
clf = clf.fit(dataset, classes)

plt.figure(figsize=(20,10))
tree.plot_tree(clf, feature_names=['Возраст', 'Дијагноза', 'Астигматизам'], class_names=['Мека', 'Тврда'], filled=True)
plt.show()