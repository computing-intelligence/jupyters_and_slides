# Created by mqgao at 2018/11/11

"""
Feature: #Enter feature name here
# Enter feature description here

Scenario: #Enter scenario name here
# Enter steps here

Test File Location: # Enter

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import time


titanic_content = pd.read_csv(open('../../datasource/titanic_train.csv'))
titanic_content = titanic_content.dropna()
age_with_fare = titanic_content[['Age', 'Fare']]
age_with_fare = age_with_fare[ (age_with_fare['Age'] > 25) & (age_with_fare['Fare'] < 450) &  (age_with_fare['Fare'] > 160)]
age = np.array(age_with_fare['Age'].tolist())
fare = np.array(age_with_fare['Fare'].tolist())

# plt.scatter(age, fare)
# plt.show()


def loss(y_true, yhats): return np.mean(np.abs(y_true - yhats))
#
#
def model(x, a, b): return a * x + b

a = 0
b = 0

yhats = np.array([model(x, a, b) for x in age])


eps = 20

directions = [(1, -1), (1, 1), (-1, -1), (-1, 1)]

learning_rate = 1e-2

min_loss = float('inf')

batch = 0

total = 1000

while True:
    if loss(y_true=fare, yhats=yhats) < eps: break

    indices = np.random.choice(range(len(age)), size=10)

    sample_x = age[indices]
    sample_y = fare[indices]

    new_a, new_b = a, b

    for d in directions:
        da, db = d

        if min_loss != float('inf'):
            _a = a + da * min_loss * learning_rate
            _b = b + db * min_loss * learning_rate
        else:
            _a, _b = a + db, b + db

        y_hats = [model(x, _a, _b) for x in sample_x]
        l = loss(sample_y, np.array([model(x, a + da, b + db) for x in sample_x]))

        if l < min_loss:
            min_loss = l
            new_a, new_b = _a, _b

    if batch % 10 == 0:
        print('batch {}/ {} fare with {} * age + {}, with loss: {}'.format(batch, total, a, b, l))

    if batch > total: break

    batch += 1

    a, b = new_a, new_b

    # time.sleep(0.01)

print('the result is {}*age + {}'.format(a, b))
plt.scatter(age, fare)
plt.plot(age, [model(x, a, b) for x in age])
plt.show()

## 1. 是否是可以学习的
## 2. 判断有没有学习