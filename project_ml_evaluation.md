#### SER594: Machine Learning Evaluation
#### Criminal Activity Prediction (title)
#### Sahithya Cherukuri (author)
#### 11/20/2023 (date)

## Evaluation Metrics
### Metric 1
**Mean Squared Error**
 MSE calculates the average of the squares of the errors—that is, the average squared difference between the estimated values and the actual value.

**Choice Justification:** MSE is effective in highlighting larger errors as it squares the error before averaging them, thus amplifying the impact of outliers or large errors. This is particularly useful in scenarios where avoiding large prediction errors is critical.

**Interpretation:** A lower MSE value indicates better model performance. However, as MSE is in squared units, it might not always be intuitive. It's especially useful for comparing different models or model configurations.

### Metric 2
**Mean Absolute Error (MAE)**
MAE measures the average magnitude of the errors in a set of predictions, without considering their direction. It's the average over the test sample of the absolute differences between prediction and actual observation.

**Choice Justification:** MAE is robust to outliers and provides a straightforward indication of average error. It is particularly useful when you want a clear, direct interpretation of the model's prediction accuracy.

**Interpretation:** A lower MAE value indicates better accuracy. It represents the average error in the same units as the predicted variable, making it intuitively easier to understand.

### Metric 3
**R-squared (Coefficient of Determination)**
R-squared represents the proportion of the variance for the dependent variable that's explained by the independent variables in a regression model.

**Choice Justification:** R-squared is a statistical measure that represents the proportion of the variance for a dependent variable that's explained by an independent variable or variables in a regression model. It is a measure of how well the observed outcomes are replicated by the model.

**Interpretation:** An R-squared value closer to 1 indicates that the model explains a large portion of the variance in the response variable. However, a high R-squared doesn't necessarily imply a good model fit, especially if the model is overfitted.

### Metric 4
**Adjusted R-squared**
Adjusted R-squared is a modified version of R-squared that has been adjusted for the number of predictors in the model. It increases only if the new term improves the model more than would be expected by chance.


**Choice Justification:** Adjusted R-squared is preferred over R-squared for models with multiple predictors, as it adjusts for the number of predictors in the model. It prevents the misleading interpretation of the model's goodness of fit when unnecessary predictors are included.

**Interpretation:** A higher Adjusted R-squared indicates that the model fits the data well. It is more reliable than R-squared for models with a large number of predictors, as it only increases if the new predictor improves the model more than would be expected by chance.


## Initial Model
### Random Forest Regressor
**Construction:** The Random Forest Regressor is an ensemble learning method that operates by constructing a multitude of decision trees at training time. It is known for its robustness and is less likely to overfit compared to simpler models.

**Evaluation:** The model shows a high R-squared value, indicating good performance, with relatively low MSE and MAE, suggesting accurate predictions.

## Alternative Models
### Linear Regression (Alternative Model 1)
**Construction:** Linear Regression is a basic yet powerful regression technique. It assumes a linear relationship between the input variables and the target.

**Evaluation:** While performing reasonably well, the Linear Regression model falls short compared to the Random Forest in terms of all metrics, indicating less accuracy and fit.

### Gradient Boosting Regressor (Alternative Model 2)
**Construction:** Gradient Boosting Regressor is an ensemble technique like Random Forest but uses boosting methods. It builds the model in a stage-wise fashion and generalizes them by allowing optimization of an arbitrary differentiable loss function.

**Evaluation:** This model outperforms the initial Random Forest model in all metrics, indicating higher accuracy and better fit.

### Support Vector Regressor (Alternative Model 3)
**Construction:** Support Vector Regressor (SVR) uses the same principles as the SVM for classification, with a few modifications to make it suitable for regression. SVR provides a flexible decision boundary.

**Evaluation:** SVR performs significantly worse than the other models, with much higher errors and very low R-squared values, indicating poor model fit and accuracy.

## Visualization
### Visual 1 - Feature Importance Map
**Analysis:**
The visualization suggests the following insights for each feature relative to their importance in predicting murders/deaths from crime:

_Population:_ Highly influential in predicting crime-related deaths, indicating that larger populations might be associated with higher numbers of such incidents.

_Executions:_ Considered an important predictor, possibly reflecting a response to crime severity that correlates with the murder rate.

_Gun Law:_ Has a moderate influence, suggesting that the strictness or leniency of gun laws might have some relationship with crime-related deaths.

_Illiterate:_ Shows low importance due the extremely high population impact, indicating that literacy rates may not be a strong standalone predictor but it is a peaceful and important aspect to be considered.

_GDP:_ Exhibits comparatively low importance, suggesting that economic output by itself is not a primary driver of crime-related deaths but it is one of the influential aspects.

_Unemployment:_ Ranked low in importance, implying that unemployment rates may not be directly predictive of crime-related deaths, or their effects are captured by other, more influential features.

_Author's Note:_ I believe due to the very high population influence, the other factors are rated as less influential, but it is very evident that, higher population usually records more cases. So, apart from that, I strongly think gun_law and literacy rate should be the primary focus here. 


## Best Model

**Model: Gradient Boosting Regressor** 
Among the alternative models, the Gradient Boosting Regressor emerges as the best performing model. It has the lowest MSE and a very high R-squared value, indicating both high accuracy and an excellent fit to the data. While the Random Forest model also shows good performance, the Gradient Boosting Regressor edges it out slightly in terms of overall evaluation metrics.