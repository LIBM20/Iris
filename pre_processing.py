import numpy as np
import pandas as pd
from dataset_utils import remove_duplicated_lines, plot_histogram

dataset = pd.read_csv("./data/iris.data", header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
print(dataset)

dataset = remove_duplicated_lines(dataset)

dataset.info()

plot_histogram(dataset, 'sepal_length')

print(dataset.describe(include='all'))

import os
#Se a pasta não existir é criada
if not os.path.exists('./pre_processed'):
    os.mkdir('./pre_processed')

dataset.to_csv('./pre_processed/iris.csv')



