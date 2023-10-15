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



def csv_file(filename):
    data = pd.read_csv(filename)
    data['state'] = data['state'].str.lower()
    data = data.rename(columns={'PopulationWithLowLiteracy':'value'})
    return data


def combine_data(states, gdp, literature, population, unemployment):
    data = {}
    data['states'] = states
    gdp_data = []
    lit_data = []
    pop_data = []
    unemp_data =[]
    for i in states:
        index = gdp[gdp['state'] == i].index[0]
        gdp_data.append(gdp['value'][index])
        index = literature[literature['state'] == i].index[0]
        lit_data.append(literature['value'][index])
        index = population[population['state'] == i].index[0]
        pop_data.append(population['value'][index])
        index = unemployment[unemployment['state'] == i].index[0]
        unemp_data.append(unemployment['value'][index])
    
    data['gdp'] = gdp_data
    data['literature'] = lit_data
    data['unemployment'] = unemp_data
    data['population'] = pop_data
    df = pd.DataFrame(data)
    # print(df)
    return df

if __name__ == "__main__":
    filename_gdp = "data_original\statistic_id248063_us-real-per-capita-gdp-2022-by-state.xlsx"
    filename_population = "data_original\statistic_id183497_population-in-the-states-of-the-us-2022.xlsx"
    filename_literacy = r"data_original\\us.-literacy-rates-by-state-[updated-june-2023].csv"
    filename_unemployment = "data_original\statistic_id223675_us-annual-unemployment-rate-2022-by-state.xlsx"
    data_gdp = statista_file(filename_gdp, 1)
    data_population = statista_file(filename_population, 1)
    data_unemployment = statista_file(filename_unemployment, 1)
    data_literature = csv_file(filename_literacy)
    
    all_states = [state.name.lower() for state in us.states.STATES]

    data_combined = combine_data(all_states, data_gdp, data_literature, data_population, data_unemployment)

    data_combined.to_excel('data_processed\data.xlsx', sheet_name='Sheet1', index=False)