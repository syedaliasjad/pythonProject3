import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def marks_prediction(marks):
    x_train=np.linspace(0,2,num=50)
    y_train=np.linspace(0,20,num=50)
    X_df=pd.DataFrame(x_train).rename(columns={0:'X'})
    y_df=pd.DataFrame(y_train).rename(columns={0:'Y'})
    X=X_df.values
    y=y_df.values
    model =LinearRegression()
    model.fit(X,y)
    X_test=np.array(marks)
    X_test =X_test.reshape((1,-1))
    return model.predict(X_test)[0]