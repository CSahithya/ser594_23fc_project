#### SER594: Exploratory Data Munging and Visualization
#### Crime Rate Analysis (title)
#### Sahithya Cherukuri (author)
#### 10/16/2023 (date)

## Basic Questions
**Datasets**
1. [Population by State in the US](https://www.statista.com/statistics/183497/population-in-the-federal-states-of-the-us/)
2. [Annual Unemployment rate by state in US](https://www.statista.com/statistics/223675/state-unemployment-rate-in-the-us/)
3. [US real per capita GDP by state in US](https://www.statista.com/statistics/248063/per-capita-us-real-gross-domestic-product-gdp-by-state/)
4. [Number of Executions in US by state](https://www.statista.com/statistics/271100/number-of-executions-in-the-us/)
5. [Number of murders involving firearms by state in US](https://www.statista.com/statistics/301603/murder-involving-firearms-us/)
6. [Mass shootings in US by state](https://www.statista.com/statistics/811541/mass-shootings-in-the-us-by-state/)
7. [Gun Law strength in US by state](https://www.statista.com/statistics/1358692/leading-states-gun-law-strength-us/)
8. [US literacy rates by state](https://worldpopulationreview.com/state-rankings/us-literacy-rates-by-state)


**Dataset Author(s):** 
1. By Statista, sourced from US Census Bureau
2. By Statista, sourced from Bureau of Labor Statistics
3. By Statista, sourced from Bureau of Economic Analysis
4. By Statista, sourced from DPIC (death penalty information center)
5. By Statista, sourced from FBI
6. By Statista, sourced from [Mother jones](https://www.motherjones.com/politics/2012/12/mass-shootings-mother-jones-full-data/)
7. By Statista, sourced from [Every Town for Gun Safety](https://everytownresearch.org/rankings/)
8. By World Population Review, sourced from [Barbarabush](https://map.barbarabush.org/state-cards/) and [Reading is Fundamental](https://www.rif.org/why-reading-matters)


**Dataset Construction Date:** 
1. August 30th 2023
2. May 3rd 2023
3. June 1st 2023
4. October 6th 2023
5. October 10th 2023
6. October 6th 2023
7. June 7th 2023
8. June 2023


**Dataset Record Count:**
My datasets collect data of each state in United States of America based on socioeconomic factor or crime related parameter. Hence, all my datasets have a standard 50 record, one for each state. 
Exception is the dataset number 4, where we don't have data from states that denounce a death penalty. 


**Dataset Field Meanings:**
I combined all the above datasets to form 2 datasets: Socioeconomic dataset and Crime dataset.
Field Meanings:
1. Population of each state in the United State given in millions
2. Percentage of unemployment in the working class of labor(16 years and older)
3. Real per capita gdp of each state in the US
(Real GDP per capita takes the GDP of a country, state, or metropolitan area and divides it by the number of people in that area.) 
4. Executions from death penalty in the states that have DPIC. (Execution is just a  measure used to represent the harshness of the punishment given by the state)
5. Number of murders committed with a firearm by state
6. Number of mass murders/shootings committed by state
7. Gun safety score for each state based on 50 key gun safety policies
8. The percentage of the population that is illiterate/with education

**Dataset File Hash(es):** 
1. statistic_id1358692_leading-states-for-gun-law-strength-in-the-us-2023.xlsx : b9ad69ffb20317b49c3e88735796eb29
2. statistic_id183497_population-in-the-states-of-the-us-2022.xlsx : c5d310b4aec5b1440568012a4bbc34a9
3. statistic_id223675_us-annual-unemployment-rate-2022-by-state.xlsx : e3ce6dd1810761f49644b7c42bd86a67
4. statistic_id248063_us-real-per-capita-gdp-2022-by-state.xlsx : 1c225e64196f1cadb1ff4eb11d65d844
5. statistic_id271100_number-of-executions-in-the-united-states-2015-2023.xlsx : 847d459b9cfbbd5ac247785f891c666a
6. statistic_id301603_murders-involving-firearms-in-the-us-2021-by-state.xlsx : 742fbec818eeb78c72ee4dbef17c1507
7. statistic_id811541_mass-shootings-in-the-us-1982-2023-by-state.xlsx : a61ceb36ff8a7c3731f70010a526eee9
8. us.-literacy-rates-by-state-[updated-june-2023].csv : 3f8f233b788bc08e8bc6bbfcc79bd7a7


## Interpretable Records
### Record 1 
**Raw Data:** 
Annual Unemployment Record

| State          | Unemployment |
| --------------- | ------------ |
| alabama         | 2.6          |
| alaska          | 4            |
| arizona         | 3.8          |
| arkansas        | 3.3          |
| california      | 4.2          |
| colorado        | 3            |
| connecticut     | 4.2          |
| delaware        | 4.5          |
| florida         | 2.9          |
| georgia         | 3            |
| hawaii          | 3.5          |
| idaho           | 2.7          |
| illinois        | 4.6          |
| indiana         | 3            |
| iowa            | 2.7          |
| kansas          | 2.7          |
| kentucky        | 3.9          |
| louisiana       | 3.7          |
| maine           | 3            |
| maryland        | 3.2          |
| massachusetts   | 3.8          |
| michigan        | 4.2          |
| minnesota       | 2.7          |
| mississippi     | 3.9          |
| missouri        | 2.5          |
| montana         | 2.6          |
| nebraska        | 2.3          |
| nevada          | 5.4          |
| new hampshire   | 2.5          |
| new jersey      | 3.7          |
| new mexico      | 4            |
| new york        | 4.3          |
| north carolina  | 3.7          |
| north dakota    | 2.1          |
| ohio            | 4            |
| oklahoma        | 3            |
| oregon          | 4.2          |
| pennsylvania    | 4.4          |
| rhode island    | 3.2          |
| south carolina  | 3.2          |
| south dakota    | 2.1          |
| tennessee       | 3.4          |
| texas           | 3.9          |
| utah            | 2.3          |
| vermont         | 2.6          |
| virginia        | 2.9          |
| washington      | 4.2          |
| west virginia   | 3.9          |
| wisconsin       | 2.9          |
| wyoming         | 3.6          |


**Interpretation:** 

This data talks about the unemployment rates over a year in each state of the Unites States of America. It is the number of job seeking individuals that don't have a job(16 years and above). Rationale behind using this data is so that I can correlate the effect of unemployment in each state to the crime rates respectively, understanding effectively the dependency of the factor in resulting crime in a area. 

### Record 2
**Raw Data:** 
Leading States with Gun Law Strength

| State          | Gun Law |
| --------------- | ------- |
| alabama         | 12.5    |
| alaska          | 9       |
| arizona         | 8.5     |
| arkansas        | 4.5     |
| california      | 86.5    |
| colorado        | 58.5    |
| connecticut     | 78.5    |
| delaware        | 60      |
| florida         | 33.5    |
| georgia         | 5       |
| hawaii          | 79.5    |
| idaho           | 5       |
| illinois        | 77      |
| indiana         | 16.5    |
| iowa            | 15.5    |
| kansas          | 9.5     |
| kentucky        | 9       |
| louisiana       | 20.5    |
| maine           | 20.5    |
| maryland        | 72.5    |
| massachusetts   | 78      |
| michigan        | 25.5    |
| minnesota       | 38.5    |
| mississippi     | 3       |
| missouri        | 9       |
| montana         | 5       |
| nebraska        | 31      |
| nevada          | 35      |
| new hampshire   | 9       |
| new jersey      | 79      |
| new mexico      | 39.5    |
| new york        | 81.5    |
| north carolina  | 31      |
| north dakota    | 11.5    |
| ohio            | 13      |
| oklahoma        | 7.5     |
| oregon          | 66.5    |
| pennsylvania    | 40      |
| rhode island    | 57.5    |
| south carolina  | 18      |
| south dakota    | 5.5     |
| tennessee       | 16.5    |
| texas           | 13.5    |
| utah            | 11      |
| vermont         | 32.5    |
| virginia        | 49      |
| washington      | 62.5    |
| west virginia   | 20      |
| wisconsin       | 28      |
| wyoming         | 6.5     |

**Interpretation:** 

The data provided here assesses the strength of gun laws in each state. It's determined by evaluating how well each state follows 50 safety measures related to firearms. This information allows us to examine the relationship between having gun laws in place and the impact on crime rates within each state.

It's important to note that simply having laws regulating firearm usage does not necessarily equate to reduced crime rates. This data enables us to take a closer look at this relationship and draw informed conclusions.

## Background Domain Knowledge

My project centers on a comprehensive analysis of the various factors that influence crime rates, intending to shed light on areas that require attention and improvement. By delving into these factors, we can better understand their impact on crime, potentially providing insights to reduce crime rates in different regions.

To conduct this analysis, I'm utilizing a dataset encompassing various socioeconomic factors within U.S. states. These factors include unemployment rates, Gross Domestic Product (GDP), literacy levels, and the population of each state. Additionally, I'm examining a range of crime-related variables, such as the implementation of safety gun laws, the number of shootings, instances of murder, and executions within these states.

The primary goal of this project is to unveil the relationships and patterns between these diverse data sets. By doing so, we can extract valuable knowledge that may help identify strategies for crime reduction. This research has the potential to offer evidence-based recommendations for targeted improvements in various areas of a state, ultimately contributing to the broader objective of decreasing crime rates and enhancing the well-being of local communities.

In essence, this project aims to bridge the gap between data and actionable insights, providing a solid foundation for informed decision-making and policies to address crime-related challenges.

_References:
_
https://www.apa.org/pi/ses/resources/publications/violence

https://www.pewresearch.org/short-reads/2020/11/20/facts-about-crime-in-the-u-s/

https://www.nobledesktop.com/classes-near-me/blog/data-analytics-in-crime-prediction-and-prevention

## Data Transformation
### Transformation 1
**Description:**
I transformed the data from the number of executions to display a sum of executions instead of by the year for a better analysis of data. I added all the executions over the years and combined it into one column. Aggregation of data. 

**Soundness Justification:**
By adding all the data I am not introducing any anomalies to the data, it is just a better way to display and work with the data. I am not changing any values but just making one column for various columns of data representing the same detail. 

### Transformation 1
**Description:**
I filtered the literacy dataset to only consider the percent of illiterate population filtering out the extra column representing the number of 4th graders below basic education.  

**Soundness Justification:**
By only considering the percentage of population, I am using a factor that can be correlated to the existing dataset and that can semantically fit in with the other factors. Using 4th graders with basic education can be useful but it doesn't represent the crime causing population and thus is not necessary. 

## Visualization
### Visual 1
**Analysis:** 
Population vs Unemployment
- Unemployment is the rate of job seeking individuals without a job.
- Unemployment factor only includes the population of 16 and above.
- From the scatter plot, we can infer that the percentage of job seeking people are more in the less populated states comparatively which does contribute to a lesser value but there is also close to 4% unemployment in most populated states which is a matter of concern. 

### Visual 2
**Analysis:** 
Population vs Illiterate
- Illiterate is given as a percentage of adult population that is not educated.
- Most of the states have illiteracy lying between 13% to 25%. 
- From the scatter plot, we can infer that the highest populated states has high illiteracy (almost 19 million) and this contributes to be more than half illiteracy in the country (other states each has population less than 23million).

### Visual 3
**Analysis:** 
Illiterate vs GDP
- Illiterate is given as a percentage of adult population that is not educated.
- GDP here is the real per capita gdp (gdp of state by the number of people in the area) 
- From the scatter plot, we can infer that illiteracy doesn't have a huge impact on gdp. Although, since the gdp is already taken as the gdp per capita, the relation might not represent the actual gdp of the state to literacy. 

### Visual 4
**Analysis:** 
Gun Laws vs Shootings
- Gun laws is the strength of safety protocol a state follows(based on 50 gun laws)
- Shootings are the number of shooting that took place in each state. 
- From the scatter plot, it is surprising that the states with higher strength of gun laws still contribute to have the most shootings. Although the one data point, is California, which can be reasoned with its high population rates. But then, there are other countries with high gun_law strength that have high shootings. This plot portrays that shootings are occurring even with string gun laws in place.

### Visual 5
**Analysis:** 
Executions vs Murders
- Executions is the number of people executed in a state
- Murders is the number of murders committed in a state 
- From the scatter plot, it shows that the murders are comparatively more in states with less executions. But there are also states with high murders even with execution in place. Does having harsh punishments in place reduce murders? Not by a lot. 

### Visual 6
**Analysis:** 
Gun Law Histogram
- A histogram representing the number of states(frequency) with a particular gun law strength. The histogram shows that more states have less gun safety rules(strength). With only very few states having above 50% gun safety rules. 

There are 2 extra sample plots that have scatter plot relations with all the data present in my dataset. 