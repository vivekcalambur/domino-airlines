import os
import pandas as pd
import feather
import numpy as np
import pickle
from sklearn.impute import SimpleImputer

path_wd = os.getenv("PATH_WD")
path_input_data = os.getenv("PATH_INPUT_DATA")
path_output_data = os.getenv("PATH_OUTPUT_DATA")
path_output_artifacts = os.getenv("PATH_OUTPUT_ARTIFACTS")
path_airlines = os.path.join(path_input_data, "airlines_small_target_selected.feather")

pd_airlines = feather.read_dataframe(path_airlines)

list_num = [line.rstrip('\n') for line in open(os.path.join(path_input_data, "airlines_impute_num_vars.txt"), "r")]
list_cat = [line.rstrip('\n') for line in open(os.path.join(path_input_data, "airlines_impute_cat_vars.txt"), "r")]

imp_mean = SimpleImputer(missing_values=np.nan, strategy="mean")
np_airlines_num = imp_mean.fit_transform(pd_airlines[list_num])
pd_airlines_num = pd.DataFrame(np_airlines_num)
pd_airlines_num.columns = list_num
print(pd_airlines_num.head())
print(pd_airlines_num.isnull().sum(axis=0))

imp_cat = SimpleImputer(missing_values=np.nan, strategy="constant", fill_value=-1)
np_airlines_cat = imp_cat.fit_transform(pd_airlines[list_cat])
pd_airlines_cat= pd.DataFrame(np_airlines_cat)
pd_airlines_cat.columns = list_cat
print(pd_airlines_cat.head())
print(pd_airlines_cat.isnull().sum(axis=0))

with open(os.path.join(path_output_artifacts, "imp_mean.pkl"), "wb") as f:
	pickle.dump(imp_mean, f)
	f.close()

with open(os.path.join(path_output_artifacts, "imp_cat.pkl"), "wb") as f:
	pickle.dump(imp_cat, f)
	f.close()

feather.write_dataframe(pd_airlines_num, os.path.join(path_output_data, "airlines_small_imp_num.feather"))
feather.write_dataframe(pd_airlines_cat, os.path.join(path_output_data, "airlines_small_imp_cat.feather"))
