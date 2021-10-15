import pandas as pd
delays_df = pd.read_csv('Lots_of_flight_data.csv')
str = delays_df.shape

print(str)

X = delays_df.loc[:,['DISTANCE', 'CRS_ELAPSED_TIME']]
X.head()

y = delays_df.loc[:,['ARR_DELAY']]
y.head()

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
                                                    X, 
                                                    y, 
                                                    test_size=0.3, 
                                                    random_state=42
                                                   )

x = X_train.shape
print(x)