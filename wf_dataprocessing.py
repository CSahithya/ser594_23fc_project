import pandas as pd
import numpy as np
import openpyxl
import us

def statista_file(filename, sheet=1):

    sheet_name = 'Data' 
    workbook = openpyxl.load_workbook(filename, data_only=True)
    sheet = workbook[sheet_name]
    data = sheet.values
    columns = next(data)  
    df = pd.DataFrame(data, columns=columns)
    df.dropna(axis=1, how='all', inplace=True)

    data_rows = df.notna()
    df = df[data_rows]
    if len(df.columns)==3:
        df.columns = ['state','value', 'percent']
        df.drop(columns='percent')
    else:
        df.columns = ['state', 'value']
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    df['state'] = df['state'].str.lower()
    df = df.drop([0,1,2,3])
    df.reset_index(drop=True, inplace=True)
    return df


def process_file(filename):
    sheet_name = 'Data' 
    workbook = openpyxl.load_workbook(filename, data_only=True)
    sheet = workbook[sheet_name]
    data = sheet.values
    columns = next(data)  
    df = pd.DataFrame(data, columns=columns)
    df.dropna(axis=1, how='all', inplace=True)
    data_rows = df.notna()
    df = df[data_rows]
    df = df.drop([0,1,2,3])
    for x in df.columns:
        df[x] = df[x].replace('',0)
    df.columns = ['state','2015', '2016','2017','2018','2019','2020','2021','2022','2023*']
    df['state'] = df['state'].str.lower()
    df['value'] = df['2015'] + df['2016'] + df['2017'] + df['2018']+df['2019']+df['2020']+df['2021']+df['2022']+df['2023*']
    # print(df)
    return df

def csv_file(filename):
    data = pd.read_csv(filename)
    data['state'] = data['state'].str.lower()
    data = data.rename(columns={'PopulationWithLowLiteracy':'value'})
    return data


def combine_param_data(states, gdp, illiterate, population, unemployment):
    data = {}
    data['states'] = states
    gdp_data = []
    lit_data = []
    pop_data = []
    unemp_data =[]
    for i in states:
        index = gdp[gdp['state'] == i].index[0]
        gdp_data.append(gdp['value'][index])
        index = illiterate[illiterate['state'] == i].index[0]
        lit_data.append(illiterate['value'][index])
        index = population[population['state'] == i].index[0]
        pop_data.append(population['value'][index])
        index = unemployment[unemployment['state'] == i].index[0]
        unemp_data.append(unemployment['value'][index])
    
    data['gdp'] = gdp_data
    data['illiterate'] = lit_data
    data['unemployment'] = unemp_data
    data['population'] = pop_data
    df = pd.DataFrame(data)
    # print(df)
    return df


def combine_crime_data(states, data_execution, data_shootings, data_gun_law, data_murders):
    data = {}
    data['states'] = states
    executions = []
    shootings = []
    gun_law = []
    murders =[]
    for i in states:
        if (data_execution['state'] == i).any():
            index = data_execution[data_execution['state'] == i].index[0]
            executions.append(data_execution['value'][index])
        else:
            executions.append(0)

        if (data_shootings['state'] == i).any():
            index = data_shootings[data_shootings['state'] == i].index[0]
            shootings.append(data_shootings['value'][index])
        else:
            shootings.append(0)

        if (data_gun_law['state'] == i).any():
            index = data_gun_law[data_gun_law['state'] == i].index[0]
            gun_law.append(data_gun_law['value'][index])
        else:
            gun_law.append(0)

        if (data_shootings['state'] == i).any():
            index = data_shootings[data_shootings['state'] == i].index[0]
            murders.append(data_shootings['value'][index])
        else:
            murders.append(0)

    data['gun_law'] = gun_law
    data['shootings'] = shootings
    data['executions'] = executions
    data['murders'] = murders
    df = pd.DataFrame(data)
    return df

def data_processing():
    gdp_filepath = "data_original\statistic_id248063_us-real-per-capita-gdp-2022-by-state.xlsx"
    population_filepath = "data_original\statistic_id183497_population-in-the-states-of-the-us-2022.xlsx"
    literacy_filepath = r"data_original\\us.-literacy-rates-by-state-[updated-june-2023].csv"
    unemployment_filepath = "data_original\statistic_id223675_us-annual-unemployment-rate-2022-by-state.xlsx"
    data_gdp = statista_file(gdp_filepath, 1)
    data_population = statista_file(population_filepath, 1)
    data_unemployment = statista_file(unemployment_filepath, 1)
    data_illiterate = csv_file(literacy_filepath)
    
    all_states = [state.name.lower() for state in us.states.STATES]

    data_combined = combine_param_data(all_states, data_gdp, data_illiterate, data_population, data_unemployment)

    data_combined.to_excel('data_processed\data.xlsx', sheet_name='Sheet1', index=False)

    shootings_filepath = "data_original\statistic_id811541_mass-shootings-in-the-us-1982-2023-by-state.xlsx"
    gun_law_strength_file = "data_original\statistic_id1358692_leading-states-for-gun-law-strength-in-the-us-2023.xlsx"
    executions_filepath = "data_original\statistic_id271100_number-of-executions-in-the-united-states-2015-2023.xlsx"
    murders_filepath ="data_original\statistic_id301603_murders-involving-firearms-in-the-us-2021-by-state.xlsx"

    data_shootings = statista_file(shootings_filepath)
    data_gun_law = statista_file(gun_law_strength_file)
    data_execution = process_file(executions_filepath)
    data_murders = statista_file(murders_filepath)

    crime_data_combined = combine_crime_data(all_states, data_execution, data_shootings, data_gun_law, data_murders)
    crime_data_combined.to_excel('data_processed\crime_data.xlsx', sheet_name='Sheet1', index=False)
