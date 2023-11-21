import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import wf_ml_evaluation_transformation as transform
import wf_ml_training as train
import wf_ml_prediction as predict
import wf_ml_visualization as visualize
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR

def prepare_data(data):
    features = ['gdp', 'illiterate', 'unemployment', 'population', 'executions', 'gun_law']
    target = 'murders'   
    return features, target

def adjusted_r_squared(r_squared, n, p):
    return (1 - (1 - r_squared) * (n - 1) / (n - p - 1))


def experimentation(model):
    y1 = model.predict([["60012.985","14.3","3.75","1.085","0","0.494011976"]]) # 0.019230769
    y2 = model.predict([["55331.69","14.9","2.7","3.2","0","0.149700599"]]) # 0.038461538
    print("Prediction for the first record:",y1)
    print("Prediction for the second record:",y2)
    print("\nTrend across feature gun_law")
    y3 = model.predict([["55331.69","14.9","2.7","3.2","0","0.149700599"]])
    y4 = model.predict([["55331.69","84.9","2.7","3.2","0","0.149700599"]])
    print("Prediction for the first record:(lower illiteracy)",y3)
    print("Prediction for the second record:(higher illiteracy)",y4)
    y5 = model.predict([["55331.69","14.9","2.7","3.2","0","0.149700599"]])
    y6 = model.predict([["55331.69","14.9","62.7","3.2","0","0.149700599"]])
    print("Prediction for the first record:(lower unemployment)",y5)
    print("Prediction for the second record:(higher unemployment)",y6)
    y7 = model.predict([["55331.69","4.9","2.7","3.2","0","0.149700599"]])
    y8 = model.predict([["55331.69","4.9","82.7","3.2","0","0.149700599"]])
    y9 = model.predict([["55331.69","84.9","2.7","3.2","0","0.149700599"]])
    y10 = model.predict([["55331.69","84.9","82.7","3.2","0","0.149700599"]])
    print("Prediction for the first record:(lower illiteracy and lower unemployment)",y7)
    print("Prediction for the second record:(lower illiteracy and higher unemployment)",y8)
    print("Prediction for the first record:(higher illiteracy and lower unemployment)",y9)
    print("Prediction for the second record:(higher illiteracy and higher unemployment)",y10)


if __name__ == "__main__":
    data = transform.data_transform()
    features, target = prepare_data(data)

    X_train, X_test, y_train, y_test = train_test_split(data[features], data[target], test_size=0.2, random_state=42)
    
    rfr_model = train.train_data(X_train, y_train)
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
        adjusted_r2 = adjusted_r_squared(r_squared=r2_score(y_test,prediction), n=X_test.shape[0],p=X_test.shape[1])
        file.write(f"  Adjusted  R-squared: {adjusted_r2}\n")

    visualize.visualization(features)

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
            adjusted_r2 = adjusted_r_squared(r_squared=r2_score(y_test,predictions[name]), n=X_test.shape[0],p=X_test.shape[1])
            file.write(f"  Adjusted  R-squared: {adjusted_r2}\n")
            file.write("\n")
    experimentation(rfr_model)
    # experimentation(models["Gradient Boosting Regressor"])    

    

    
    
    