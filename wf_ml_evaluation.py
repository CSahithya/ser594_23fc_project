import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import wf_ml_evaluation_transformation as transform
import wf_ml_training as train
import wf_ml_prediction as predict
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR

def prepare_data(data):
    features = ['gdp', 'illiterate', 'unemployment', 'population']
    target = 'crime_rate_factor'   
    return features, target

if __name__ == "__main__":
    data = transform.data_transform()
    features, target = prepare_data(data)

    X_train, X_test, y_train, y_test = train_test_split(data[features], data[target], test_size=0.2, random_state=42)
    
    train.train_data(X_train, y_train)
    prediction = predict.predictions_model(X_test, y_test)

    
    evaluation_metrics = {
        "Mean Squared Error": mean_squared_error,
        "Mean Absolute Error": mean_absolute_error,
        "R-squared": r2_score
    }
    
    os.makedirs('evaluation', exist_ok=True)
    summary = os.path.join('evaluation', f'summary.txt')

    with open(summary, 'w') as file:
        file.write(f'Evaluation Metrics for model - RandomForestRegressor:\n')
        for metric_name, metric_function in evaluation_metrics.items():
            metric_value = metric_function(y_test, prediction)
            file.write(f"  {metric_name}: {metric_value}\n")

    models = {
        "Linear Regression": LinearRegression(),
        "Gradient Boosting Regressor": GradientBoostingRegressor(random_state=42),
        "Support Vector Regressor": SVR()
    }
    
    predictions = {}

    for _, model in models.items():
        model.fit(X_train, y_train)

    with open(summary, 'a') as file:
        file.write(f'\nAlternative Models\n')
        for name, model in models.items():
            predictions[name] = model.predict(X_test)
            file.write(f'Evaluation Metrics for model - {name}:\n')
            for metric_name, metric_function in evaluation_metrics.items():
                metric_value = metric_function(y_test, predictions[name])
                file.write(f"  {metric_name}: {metric_value}\n")
            file.write("\n")

            

    

    
    
    