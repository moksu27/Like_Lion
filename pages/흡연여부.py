import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns

pd.options.display.max_columns = None


url = "https://raw.githubusercontent.com/moksu27/midproject/main/healthcare-dataset-stroke-data.csv"
df = pd.read_csv(url)

dt2 = df[["id","gender","age","smoking_status","stroke"]]

dt2 = dt2[dt2["age"] >= 55]