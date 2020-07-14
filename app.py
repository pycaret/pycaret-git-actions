import os, ast
import pandas as pd

dataset_path = "https://raw.githubusercontent.com/" + os.environ["GITHUB_REPOSITORY"] +"/master/dataset.csv"
data = pd.read_csv(dataset_path)
data.head()

target = ast.literal_eval(os.environ["INPUT_MYINPUT"])

from pycaret.classification import *
clf1 = setup(data, target =  target, session_id=123, silent=True, html=False, log_experiment=True, experiment_name='exp1')

c = compare_models()

save_model(c, 'model')

logs_exp1 = get_logs(save=True)