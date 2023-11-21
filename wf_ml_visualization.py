import pickle
import os
import pandas as pd
import matplotlib.pyplot as plt

def visualization(features):
    file_path = os.path.join('models', 'RandomForestRegressor.pkl')
        
    with open(file_path, 'rb') as file:
        model = pickle.load(file)

    importances = model.feature_importances_
    imp_df = pd.DataFrame({'Feature': features, 'Importance': importances})
    imp_df = imp_df.sort_values(by='Importance', ascending=False)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.bar(imp_df['Feature'], imp_df['Importance'], color='skyblue')
    plt.title('Feature Importances in Random Forest Model')
    plt.xlabel('Features')
    plt.ylabel('Importance')
    plt.xticks(rotation=45)
    plt.savefig('visuals/feature_importance.png')
    # plt.show()
    