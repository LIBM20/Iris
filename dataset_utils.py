import pandas as pd
from pandas import DataFrame

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