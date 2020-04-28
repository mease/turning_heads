import os
from sklearn.model_selection import train_test_split

X = y = os.listdir('gen')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=0)

for x in X_train:
    os.rename('gen/'+x , 'data/train/'+x)

for x in X_test:
    os.rename('gen/'+x , 'data/test/'+x)