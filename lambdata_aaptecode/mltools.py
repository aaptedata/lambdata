#!/c/Users/aapte/AppData/Local/Programs/Python/Python38/python
""" This package has some useful machine learning tools. """

def train_validation_test_split(
    X, y, train_size=0.8, val_size=0.1, test_size=0.1, 
    random_state=None, shuffle=True):

    '''Splits the features and target data into train, validation and test sets'''
    from sklearn.model_selection import train_test_split   

    assert train_size + val_size + test_size == 1

    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, shuffle=shuffle)
    
    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val, y_train_val, test_size=val_size/(train_size+val_size), 
        random_state=random_state, shuffle=shuffle)
    
    return X_train, X_val, X_test, y_train, y_val, y_test

def conf_matrix_2d(y_test, y_pred):

    '''Delivers a 2x2 pandas confusion matrix for binary data'''
    assert len(y_test) == len(y_pred)
    import pandas as pd
    matrix = pd.crosstab(y_test, y_pred, dropna=False, margins=True)
    matrix.rename(index={'0': 'Actual False', '1': 'Actual True'},
                  columns={'0': 'Tested False', '1': 'Tested True'})
    return matrix