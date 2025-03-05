import pandas as pd
from dataset_utils import remove_duplicated_lines

dataset = pd.read_csv("./data/iris.data", header=None)
print(dataset)

dataset = remove_duplicated_lines(dataset)

import os
#Se a pasta não existir é criada
if not os.path.exists('./pre_processed'):
    os.mkdir('./pre_processed')

dataset.to_csv('./pre_processed/iris.csv')