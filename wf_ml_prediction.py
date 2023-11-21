import pickle
import os
import numpy as np


def predictions_model(X_test, y_test):
    file_path = os.path.join('models', 'RandomForestRegressor.pkl')
    
    with open(file_path, 'rb') as file:
        rfr_model = pickle.load(file)
    
    prediction = rfr_model.predict(X_test)
    return prediction

if __name__ == "__main__":
    X = np.array([['64567.03','40','90','2.9']])
    print(predictions_model(X,[]))
    # model_paths = {
    #     "RandomForestRegressor": os.path.join('models', 'RandomForestRegressor.pkl'),
    #     "LinearRegression": os.path.join('models', 'LinearRegression.pkl'),
    #     "GradientBoostingRegressor": os.path.join('models', 'GradientBoostingRegressor.pkl')
    # }

    # models = {}
    # for name, path in model_paths.items():
        # with open(model_path, 'rb') as file:
        #     model[name] = pickle.load(file)
        # print(f'{name} model loaded.')

    # predictions = {}

    # for name, model in models.items():
    #     predictions[name] = model.predict(X_test)
        # print(f'Predictions from {name} model obtained.')

    # os.makedirs('evaluation', exist_ok=True)
    # summary = os.path.join('evaluation', f'summary.txt')

    # with open(summary, 'w') as file:
    #     for model_name, model_pred in predictions.items():
    #         file.write(f'Evaluation Metrics for {model_name}:\n')
    #         for metric_name, metric_function in evaluation_metrics.items():
    #             metric_value = metric_function(y_test, model_pred)
    #             file.write(f"  {metric_name}: {metric_value}\n")
    #         file.write("\n")