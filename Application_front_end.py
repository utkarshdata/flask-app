import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
import seaborn as sns
import sympy
import pickle

df = pd.read_csv('/Users/utkarshvaibhav/Downloads/application_csv.csv')

df.sort_values(by=['Year'], inplace=True)

df.loc[(df.Key=='NYU Stern_2017'), 'Number_of_Applicants']=3700
df.loc[(df.Key=='Darden_2018'), 'Number_of_Applicants']=2545

#IQR is calculated as the difference between the 25th and the 75th percentile of the data.
#The percentiles can be calculated by sorting the selecting values at specific indices.
#The IQR is used to identify outliers by defining limits on the sample values that are a factor k of the IQR.
#The common value for the factor k is the value 1.5.

def removeOutlier(col):
    sorted(col)
    quant1, quant2 = col.quantile([0.25,0.75])
    IQR = quant2-quant1
    lowerRange = quant1-(1.5*IQR)
    upperRange = quant2+(1.5*IQR)
    return lowerRange, upperRange

lowScore, highScore = removeOutlier(df['Number_of_Applicants'])
df['Number_of_Applicants'] = np.where(df['Number_of_Applicants']>highScore, highScore, df['Number_of_Applicants'])
df['Number_of_Applicants'] = np.where(df['Number_of_Applicants']<lowScore, lowScore, df['Number_of_Applicants'])


categorical_cols = ['School','Year']
df = pd.get_dummies(df, columns=categorical_cols)
df.head()

X = df.iloc[:, [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]].values
x=X.tolist()

from sklearn.preprocessing import StandardScaler
stdscale = StandardScaler()
df['Number_of_Applicants'] = stdscale.fit_transform(df[['Number_of_Applicants']])

y = df.iloc[:, 1].values

#from sklearn.model_selection import train_test_split

#X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.20)

from sklearn.linear_model import Ridge
mdl = Ridge(alpha=0.5)
mdl.fit(X, y)
mdl.score(X, y)

pickle.dump(mdl, open('mdl.pkl','wb'))
