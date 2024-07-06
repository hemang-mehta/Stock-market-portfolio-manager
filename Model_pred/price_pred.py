import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import RobustScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
import warnings

warnings.filterwarnings("ignore", category=UserWarning)


def predict_stock_movement(stock_name, curr_data):
    # Reading the csv file
    data = pd.read_csv(f'D:/PDPU/TY/APP_project/Model_pred/{stock_name}.NS.csv')
    
    #removing rows containing null values
    data.dropna(axis = 0, inplace = True)
    
    data['Change'] = data['Close'].diff()

    # converting output to 0 and 1 for negative and positive values respectively
    data['Change'] = data['Change'].apply(lambda x: 0 if x < 0 else 1)
    
    # scaling the data using robust scaler
    rscaler = RobustScaler()
    Dep_var = data.drop('Change', axis = 'columns')
    s_data = rscaler.fit_transform(Dep_var)
    scaled_data = pd.DataFrame(s_data, columns = Dep_var.columns)
    
    #splitting dataset into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(scaled_data, data['Change'], test_size=0.1)

    # Applying Logistic Regression model
    lr_classifier = LogisticRegression()
    lr_classifier.fit(x_train, y_train)
    y_pred = lr_classifier.predict(x_test)
    lr_acc = accuracy_score(y_test, y_pred) * 100

    # Applying KNN model
    knn_classifier = KNeighborsClassifier(n_neighbors=1)
    knn_classifier.fit(x_train,y_train)
    y_pred = knn_classifier.predict(x_test)
    knn_acc = accuracy_score(y_test, y_pred) * 100

    # Applying Support Vector Machine Model
    svm_classifier = SVC(kernel='rbf')
    svm_classifier.fit(x_train, y_train)
    y_pred = svm_classifier.predict(x_test)
    svm_acc = accuracy_score(y_test, y_pred) * 100

    if lr_acc > knn_acc and svm_acc:
        model = lr_classifier
    elif knn_acc > svm_acc:
        model = knn_classifier
    else:
        model = svm_classifier

    testing = np.array(curr_data).reshape(1,-1)
    predict = model.predict(testing)
    return predict

symbols = ['INFY', 'RELIANCE', 'TCS']
for i in symbols:
    path = f'Model_pred\{i}.NS.csv'
    pred_val = predict_stock_movement(i, [140.720001, 140.929993, 140.139999, 140.160004, 140.160004, 372543])
    print(f'For {i} -> ')
    if pred_val == 1:
        print('Bullish Trade')
    else:
        print('Bearish Trade')