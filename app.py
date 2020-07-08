import os, ast
import pandas as pd

dataset_path = "https://raw.githubusercontent.com/" + os.environ["GITHUB_REPOSITORY"] +"/master/dataset.csv"
data = pd.read_csv(dataset_path)
data.head()

from pycaret.classification import *
clf1 = setup(data, target = 'Purchase', session_id=123, silent=True, html=False)

pd.set_option("display.max_columns", 999)

c = compare_models()

save_model(c, 'model')
