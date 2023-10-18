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
4. Executions from death penalty in the states that have DPIC
5. Number of murders committed with a firearm by state
6. Number of mass murders/shootings committed by state
7. Gun safety score for each state based on 50 key gun safety policies
8. The percentage of the population that is literate/with education

**Dataset File Hash(es):** TODO
<!-- >>> with open(".\data_original\statistic_id248063_us-real-per-capita-gdp-2022-by-state.xlsx", "rb") as file:
...     while True:
...             data = file.read(8192)
...             if not data:
...                     break
...             md5.update(data)
...     print(md5.hexdigest())
...
1c225e64196f1cadb1ff4eb11d65d844 -->


## Interpretable Records
### Record 1
**Raw Data:** TODO

**Interpretation:** TODO

### Record 2
**Raw Data:** TODO

**Interpretation:** TODO

## Background Domain Knowledge
TODO

## Data Transformation
### Transformation N
**Description:** TODO

**Soundness Justification:** TODO

(duplicate above as many times as needed; remove this line when done)


## Visualization
### Visual N
**Analysis:** TODO

(duplicate above as many times as needed; remove this line when done)