import os, ast
import pandas as pd

dataset = os.environ["INPUT_DATASET"]
target = os.environ["INPUT_TARGET"]

dataset_path = "https://raw.githubusercontent.com/" + os.environ["GITHUB_REPOSITORY"] + "/master/" + os.environ["INPUT_DATASET"] + '.csv'
data = pd.read_csv(dataset_path)
data.head()

if type(target) is float:
    from pycaret.regression import *
else:
    from pycaret.classification import *

exp1 = setup(data, target = target, session_id=123, silent=True, html=False, log_experiment=True, experiment_name='exp_github')

c = compare_models()

save_model(c, 'model')

logs_exp_github = get_logs(save=True)