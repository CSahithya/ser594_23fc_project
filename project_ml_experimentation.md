#### SER594: Experimentation
#### Criminal Activity Prediction (title)
#### Sahithya Cherukuri (author)
#### 11/20/2023 (date)


## Explainable Records
### Record 1
**Raw Data:** 
Input features: [['gdp', 'illiterate', 'unemployment', 'population', 'executions', 'gun_law'],["60012.985","14.3","3.75","1.085","0","0.494011976"]]
Predicted: [0.00730769]
Actual: 0.019230769

_Explanation:_
GDP (60012.985): A relatively high GDP, which could be associated with better economic conditions and potentially lower crime rates.
Illiteracy Rate (14.3): Moderate illiteracy rate, which might have a moderate impact on crime rates.
Unemployment (3.75): A moderate unemployment rate, which can contribute to crime but isn't exceptionally high.
Population (1.085 million): A smaller population, which might lead to fewer opportunities for crime occurrences.
Executions (0): No executions, indicating either a low rate of severe crimes or a judicial system that does not use capital punishment.
Gun Law Strength (0.494011976): Moderate gun law strength, suggesting a balanced approach to firearm regulation.

**Prediction Explanation:**
The prediction of a low crime_rate (0.00730769) seems reasonable given the relatively high GDP and moderate levels of unemployment and illiteracy. The moderate gun law strength, combined with no executions, could be seen as indicative of a stable socio-economic environment with fewer severe crimes.

### Record 2
**Raw Data:**
Input features: [['gdp', 'illiterate', 'unemployment', 'population', 'executions', 'gun_law'],["55331.69","14.9","2.7","3.2","0","0.149700599"]]
Predicted: [0.04038462]
Actual: 0.038461538

_Explanation:_
GDP (55331.69): Slightly lower than the first record but still reasonable, indicating decent economic conditions.
Illiteracy Rate (14.9): Similar to the first record, a moderate illiteracy rate.
Unemployment (2.7): Lower than in the first record, which is generally positive for lower crime rates.
Population (3.2 million): Larger population, which could lead to a higher incidence of crime due to the larger number of individuals.
Executions (0): As with the first record, no executions.
Gun Law Strength (0.149700599): Lower gun law strength, suggesting less strict firearm regulation, which could potentially correlate with higher crime rates.

**Prediction Explanation:**
The higher crime_rate (0.04038462) in this prediction could be attributed to the larger population and the lower strength of gun laws, despite the lower unemployment rate and similar GDP and illiteracy rates compared to the first record. The larger population size and more lenient gun laws might be influencing factors leading to a higher prediction of the crime rate.

## Interesting Features
### Feature A
**Feature: *gun_law***
 The strength and nature of gun laws can have a profound impact on crime rates. Regions with stricter gun control laws might experience fewer instances of gun-related crimes due to restricted access to firearms. Conversely, areas with more lenient gun laws could see higher rates of such crimes. This relationship is a focal point in many socio-political discussions and research studies related to crime and public safety.

**Justification:** 
A higher gun_law strength value (indicating stricter gun laws) might correlate with a lower crime_rate, assuming stricter gun control effectively reduces crime incidents. This feature can be pivotal in understanding how regulatory measures influence overall crime rates.

### Feature B
**Feature: *illiterate***
Education and literacy levels are often linked to crime rates in sociological research. Higher illiteracy rates can be associated with lower socio-economic conditions, which might lead to higher crime rates due to factors like unemployment, poverty, and lack of opportunities. Understanding the relationship between education levels and crime rates can offer insights into long-term crime prevention strategies.

**Justification:**
A higher illiteracy rate might lead to an increase in the crime rate. This feature helps in understanding the socio-economic dimensions of crime, particularly how educational factors play a role in shaping crime trends in a society.

## Experiments 
### Varying A (Illiteracy Rate)
**Prediction Trend Seen:** 
When varying the illiteracy rate alone (keeping other factors constant), the model's predictions did not align with the initial hypothesis. Surprisingly, a higher illiteracy rate resulted in a slightly lower crime_rate. This could indicate that the impact of illiteracy on crime rates is not linear or is influenced by interactions with other socio-economic factors in the model.

### Varying B (Unemployment Rate)
**Prediction Trend Seen:**
Changing the unemployment rate while keeping other factors constant showed a more expected trend. A higher unemployment rate led to a higher crime_rate. This aligns with the general understanding that increased unemployment can contribute to higher crime rates, likely due to economic stress and lack of opportunities.

### Varying A and B together
**Prediction Trend Seen:**
When both illiteracy and unemployment rates were varied together, the highest crime_rate was observed with lower illiteracy and higher unemployment. This suggests that the unemployment rate might have a more substantial and direct impact on the crime rate than the illiteracy rate. The combination of higher illiteracy and higher unemployment did not result in the highest crime rate , indicating a complex interaction between these two features.


### Varying A and B inversely
**Prediction Trend Seen:**
In scenarios where illiteracy and unemployment rates were varied inversely (one increasing while the other decreasing), the lowest crime_rate was predicted for higher illiteracy and lower unemployment. This indicates that the model might be weighing the unemployment rate more heavily than the illiteracy rate in predicting crime rates. The inverse relationship does not follow a simple additive pattern, suggesting complex interdependencies between these socio-economic factors.

Sample output from the file
Prediction for the first record:(lower illiteracy) [0.04038462] </br>
Prediction for the second record:(higher illiteracy) [0.03346154]</br>

Prediction for the first record:(lower unemployment) [0.04038462]</br>
Prediction for the second record:(higher unemployment) [0.05634615]</br>

Prediction for the first record:(lower illiteracy and lower unemployment) [0.04461538]</br>
Prediction for the second record:(lower illiteracy and higher unemployment) [0.05865385]</br>
Prediction for the first record:(higher illiteracy and lower unemployment) [0.03346154]</br>
Prediction for the second record:(higher illiteracy and higher unemployment) [0.05]</br>


Author's note:
In the analysis, I have employed the term "crime_rate" instead of "murders" to enhance the contextual relevance of the study. This adjustment aims to encompass a more comprehensive understanding of crime in the region.