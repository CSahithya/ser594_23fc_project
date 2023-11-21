import pandas as pd
import itertools
from sklearn.preprocessing import MinMaxScaler


def add_data_points(data_file, crime_file):
    # Assuming merged_data is your DataFrame with state data
    # and input_columns are the columns you want to average
    data_df = pd.read_excel(data_file)
    crime_df = pd.read_excel(crime_file)
    merged_data = pd.merge(data_df, crime_df, on="states")
    input_columns = merged_data.columns

    state_pairs = list(itertools.combinations(merged_data['states'], 2))

    border_data = pd.DataFrame()

    for pair in state_pairs:
        state1_data = merged_data[merged_data['states'] == pair[0]]
        state2_data = merged_data[merged_data['states'] == pair[1]]

        avg_data = { i: (state1_data[i].values[0] + state2_data[i].values[0])/2 if i != 'states' else f"{pair[0]}_{pair[1]}_border" for i in input_columns}
  
        border_entry = pd.DataFrame([avg_data])
        border_data = pd.concat([border_data, border_entry], ignore_index=True)
    
    expanded_dataset = pd.concat([merged_data, border_data], ignore_index=True)

    # print(expanded_dataset.head())
    return expanded_dataset


def data_transform():
# if __name__ == "__main__":
    data_file = "data_processed\data.xlsx"
    crime_file = "data_processed\crime_data.xlsx"
    result_file = 'data_processed\dataset.xlsx'

    result_data = add_data_points(data_file,crime_file)
    data = generate_target_value(result_data)
    data.to_excel(result_file, sheet_name="Sheet1", index=False)
    return data

def generate_target_value(data):
    scaler = MinMaxScaler()
    data[['murders', 'executions', 'gun_law']] = scaler.fit_transform(data[['murders', 'executions', 'gun_law']])
    data['crime_rate_factor'] = data[['murders', 'executions', 'gun_law']].mean(axis=1)
    return data
