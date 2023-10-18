import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def stat_summary(data, crime_data, filename):
    data_info = {}
    crime_info = {}
    data_keys = ['gdp','literate','population','unemployment']
    crime_keys = ['gun_law','shootings','executions','murders']
    for x in data_keys:
        data_info[x] = {'Min':data[x].min(), 'Max':data[x].max(), 'Median':data[x].median().round(3)}
    for x in crime_keys:
        crime_info[x] = {'Min':crime_data[x].min(), 'Max':crime_data[x].max(), 'Median':crime_data[x].median().round(3)}
    with open(filename, 'w') as file:
        file.write("For socioeconomic factors\n")
        for x in data_keys:
            file.write(x.upper()+"\n")
            file.write("Minimum Value: " + str(data_info[x]['Min']) + "\n"+"Maximum Value: " + str(data_info[x]['Max']) + "\n")
            file.write("Median Value: "+ str(data_info[x]['Median']) + "\n")

        file.write("\n\nFor crime data\n")
        for x in crime_keys:
            file.write(x.upper()+"\n")
            file.write("Minimum Value: " + str(crime_info[x]['Min']) + "\n"+"Maximum Value: " + str(crime_info[x]['Max']) + "\n")
            file.write("Median Value: "+ str(crime_info[x]['Median']) + "\n")


def correlation_matrix(data, crime_data,filename):
    data_correlation_matrix = data[['gdp', 'literate', 'population', 'unemployment']].corr()
    crime_correlation_matrix = crime_data[['gun_law','shootings','executions','murders']].corr()
    with open(filename, 'w') as file:
        file.write("Socioeconomic Factors Correlation\n")
        file.write(str(data_correlation_matrix))
        file.write("\n\nCrime data Correlation\n")
        file.write(str(crime_correlation_matrix))
    # print(data_correlation_matrix)
    # print(crime_correlation_matrix)


def scatter_helper(data, crime_data):
    x_labels = ['Population', 'Population', 'Population', 'Literate','Literate', 'GDP']
    y_labels = ['Literate', 'GDP', 'Unemployment', 'GDP', 'Unemployment', 'Unemployment']
    fig_name= "Project\Git\ser594_23fc_project\\visuals\\SocioEconomicFactors.png" 
    scatter_plot(data, x_labels, y_labels, fig_name)

    x_labels = ['Gun_Law', 'Gun_Law', 'Gun_Law', 'Shootings','Shootings', 'Executions']
    y_labels = ['Shootings', 'Executions', 'Murders', 'Executions', 'Murders', 'Murders']
    fig_name= "Project\Git\ser594_23fc_project\\visuals\\CrimeDataPlot.png" 
    scatter_plot(crime_data, x_labels, y_labels, fig_name)


def scatter_plot(data, x_labels, y_labels, fig_name):
    fig, ax = plt.subplots(2, 3, figsize=(12, 8))

    # Scatter plot data
    for i in range(6):
        ax[i // 3, i % 3].scatter(data[x_labels[i].lower()], data[y_labels[i].lower()], alpha=0.5, color='b', marker='o')
        ax[i // 3, i % 3].set_xlabel(x_labels[i])
        ax[i // 3, i % 3].set_ylabel(y_labels[i])
        ax[i // 3, i % 3].grid(True, linestyle='--', alpha=0.7)
   
    fig.savefig(fig_name) 

    plt.suptitle('Scatter Plots', fontsize=16)
    plt.tight_layout()

    plt.show()

 
 
def visualize_correlation(correlation_matrix):
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.show()



def visualization():
    filename = "data_processed\data.xlsx"
    crime_file = "data_processed\crime_data.xlsx"
    summary_file = "data_processed\summary.txt"
    correlation_file = "data_processed\correlations.txt"
    data = pd.read_excel(filename)
    crime_data = pd.read_excel(crime_file)
    stat_summary(data, crime_data, summary_file)
    correlation_matrix(data, crime_data, correlation_file)
    # visualize_correlation(correlation_matrix)
    scatter_helper(data,crime_data)