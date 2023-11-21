import os
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

def train_data(X, y):
    os.makedirs('models', exist_ok=True)
    
    rfr_model = RandomForestRegressor(n_estimators=100, random_state=42)
    # for name, model in models.items():

    rfr_model.fit(X, y)
    model_path = os.path.join('models', 'RandomForestRegressor.pkl')
    with open(model_path, 'wb') as file:
        pickle.dump(rfr_model, file)

    return rfr_model
    # print(f'RandomForestRegressor model saved at {model_path}')