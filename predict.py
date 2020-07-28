import pandas as pd
import numpy as np
from sklearn.linear_model import SGDClassifier

train = pd.read_csv('C:/Users/utilisateur/Desktop/exo_louis_28-07-2020/train.csv')
test = pd.read_csv('C:/Users/utilisateur/Desktop/exo_louis_28-07-2020/test2.csv')

train = train.dropna()
test = test.dropna()

target_column = 'SeriousDlqin2yrs'
y_train = train[target_column].values
#print(y_train)

x_train = train.drop(target_column, axis=1).values
#print(x_train)

x_test = test.drop(target_column, axis=1).values
y_test = test[target_column].values

#model = XGBClassifier()
model = SGDClassifier(loss="modified_huber")
model.fit(x_train, y_train)

predictions = model.predict(x_test)
y_test_proba = model.predict_proba(x_test)[:,1]
#print(y_test_proba)

Id = x_test[:, [0]].astype(int)
#print(Id)

df = pd.DataFrame(data=np.column_stack((Id,predictions,y_test_proba)),columns=['Id','Predictions','Probability'])
df.Id = df['Id'].astype(int)
print(df.head())

df.to_csv("C:/Users/utilisateur/Desktop/exo_louis_28-07-2020/test2-predictions.csv", index=False)
