import pandas as pd
import numpy as np

dataset_info = pd.read_csv("dataset_Facebook.csv", sep = ';', low_memory = False)

dataset_info.agg([np.mean, np.max, np.min, np.median]).to_csv("dataset_analysis", sep = "\t", encoding = "utf-8")
dataset_info.groupby(["Type"]).agg([np.mean, np.max, np.min, np.median]).to_csv("dataset_analysis_divided", sep = "\t", encoding = "utf-8")

print(dataset_info["Total Interactions"].mode())
print(dataset_info.groupby(["Type"]).apply(lambda x: x.mode()))