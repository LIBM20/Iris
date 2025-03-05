import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

#Remover linhas duplicadas
def remove_duplicated_lines(dataset):
    initial_rows = len(dataset)
    dataset = dataset.drop_duplicates()
    rows = len(dataset)
    removed = initial_rows - rows
    if(removed > 0):
        print(f'Removed {removed} duplicated samples (rows)')
    print(f'Found {rows} samples (rows)')
    return dataset


def plot_histogram(dataset, variable_name, color='blue', title=None, xlabel=None, ylabel=None):
    data = dataset[variable_name]  # Select only the column by its name

    if title is None:
        title = f'{variable_name} histogram'
    if xlabel is None:
        xlabel = variable_name
    if ylabel is None:
        ylabel = 'Frequency'

    plt.figure(figsize=(8, 6))
    plt.hist(data, color=color, edgecolor='black', alpha=0.7)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

