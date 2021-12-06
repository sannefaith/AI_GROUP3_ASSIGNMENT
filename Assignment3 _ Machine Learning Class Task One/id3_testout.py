import numpy as np
import pandas as pd
from collections import deque

# generate some data
# define features and target values

data_df = pd.read_csv(r"C:\Users\hp\Documents\AI\assignments\task3\data\data.csv") #importing the dataset from the disk


data_df.head()

# separate target from predictors
X = np.array(data_df.drop('Fast', axis=1).copy())
y = np.array(data_df['Fast'].copy())
feature_names = list(data_df.keys())[:3]

# import and instantiate our DecisionTreeClassifier class
from id3 import DecisionTreeClassifier

# instantiate DecisionTreeClassifier
tree_clf = DecisionTreeClassifier(X=X, feature_names=feature_names, labels=y)
print("System entropy {:.4f}".format(tree_clf.entropy))
# run algorithm id3 to build a tree
tree_clf.id3()
tree_clf.printTree()


