import pandas as pd
from dataset_utils import remove_duplicated_lines

dataset = pd.read_csv("./data/iris.data", header=None)
print(dataset)

dataset = remove_duplicated_lines(dataset)