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

#Com subfiguras
def plot_histogram(dataset, color_list=None, title='Histogram of Variables', xlabel='Values', ylabel='Frequency',
                   alpha=0.7):
    numeric_cols = dataset.select_dtypes(include=['float64', 'int64']).columns
    num_cols = len(numeric_cols)

    if color_list is None:
        color_list = ['blue', 'orange', 'green', 'red', 'purple', 'brown']

    # Define grid size (2 columns)
    rows = (num_cols + 1) // 2

    fig, axes = plt.subplots(rows, 2, figsize=(12, rows * 4))
    axes = axes.flatten()  # Flatten axes for easy iteration

    for i, column in enumerate(numeric_cols):
        axes[i].hist(dataset[column], color=color_list[i % len(color_list)], edgecolor='black', alpha=alpha)
        axes[i].set_title(f'{column} Histogram')
        axes[i].set_xlabel(xlabel)
        axes[i].set_ylabel(ylabel)
        axes[i].grid(True)

    # Remove empty subplots if the number of variables is odd
    if num_cols % 2 != 0:
        fig.delaxes(axes[-1])

    plt.tight_layout()
    plt.suptitle(title, fontsize=16, y=1.02)
    plt.show()

#Com os plots a sobreporem-se
def plot_histogram_sob(dataset, color_list=None, title='Histogram of Variables', xlabel='Values', ylabel='Frequency',
                   alpha=0.7):
    plt.figure(figsize=(10, 7))

    if color_list is None:
        color_list = ['blue', 'orange', 'green', 'red', 'purple', 'brown']

    numeric_cols = dataset.select_dtypes(include=['float64', 'int64']).columns

    for i, column in enumerate(numeric_cols):
        plt.hist(dataset[column], color=color_list[i % len(color_list)], edgecolor='black', alpha=alpha, label=column)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.legend()
    plt.show()

#Apenas para uma variável específica
def plot_histogram1(dataset, variable_name, color='blue', title=None, xlabel=None, ylabel=None):
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

