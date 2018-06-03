import numpy as np
from math import sqrt
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier

"""
Neural network trained on simulated data of two distances
with their calculated direction.
"""

def main():
    def train_data():
        randomarray = np.random.randint(100, size=(100, 2))
        train_data = []
        for i in range(len(randomarray)):
            data_temp = []
            x1_temp = randomarray[i][0]
            x2_temp = randomarray[i][1]
            data_temp.append(x1_temp)
            data_temp.append(x2_temp)
            if x2_temp > x1_temp:
                m1 = 100# - (x1_temp/2)
                m2 = (x1_temp * 100) / x2_temp
                m2 = int(m2)
                #v = m2/10
                #v = int(v)
                #fr = sqrt((x2_temp*x2_temp) + (x1_temp * x1_temp))
                #fr = int(fr)
                #try:
                #    t = fr/v
                #    t = int(t)
                #    t = t/10 # max velocity at 90 degrees (straight)
                #except ZeroDivisionError:
                #    t = 0
                data_temp.append(m1)
                data_temp.append(m2)
                #data_temp.append(t)
                #print "x1: ", x1_temp
                #print "x2: ", x2_temp
                #print "V: ", v
                #print "Fr: ", fr
                #print"Time: ", t

            else:
                m1 = (x2_temp * 100) / x1_temp
                m1 = int(m1)
                m2 = 100
                #v = float(m1)/10
                #v = int(v)
                #fr = sqrt((x1_temp*x1_temp) + (x2_temp * x1_temp))
                #fr = int(fr)
                #try:
                #    t = fr/v
                #    t = int(t)
                #    t = t/10 # max velocity at 90 degrees (straight)
                #except ZeroDivisionError:
                #    t = 0
                data_temp.append(m1)
                data_temp.append(m2)
                #data_temp.append(t)
                ##print "x1: ", x1_temp
                ##print "x2: ", x2_temp
                ##print "V: ", v
                ##print "Fr: ", fr
                ##print "Time: ", t

            train_data.append(data_temp)

        train_data = np.array(train_data)
        return train_data

    def train(train_data):
        x = train_data[:, :2]
        y = train_data[:, 2:]
        forest = RandomForestClassifier(n_estimators=100, random_state=1)
        classifier = MultiOutputClassifier(forest, n_jobs=-1)
        classifier.fit(x, y)
        return classifier

    #print("Initializing")
    train_data = train_data()
    #print("Training..")
    classifier = train(train_data)
    #print("Trained")
    return classifier

def return_predicted(x1, x2, classifier):
    X = []
    x_temp = []
    x_temp.append(x1)
    x_temp.append(x2)
    X.append(x_temp)
    predicted = classifier.predict(X)
    return predicted[0][0], predicted[0][1]