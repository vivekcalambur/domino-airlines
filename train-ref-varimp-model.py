import os
import pandas as pd
import feather
import numpy as np
import pickle

path_wd = os.getenv("PATH_WD")
path_input_data = os.getenv("PATH_INPUT_DATA")
path_output_artifacts = os.getenv("PATH_OUTPUT_ARTIFACTS")
path_airlines = os.path.join(path_input_data, "airlines_small_target_selected_le.feather")
path_airlines_imp_num = os.path.join(path_input_data, "airlines_small_imp_num.feather")
path_airlines_imp_cat = os.path.join(path_input_data, "airlines_small_imp_cat.feather")

pd_airlines = feather.read_dataframe(path_airlines)
pd_airlines_imp_num = feather.read_dataframe(path_airlines_imp_num)
pd_airlines_imp_cat = feather.read_dataframe(path_airlines_imp_cat)

print(pd_airlines.isnull().sum(axis=0))

list_num = [line.rstrip('\n') for line in open(os.path.join(path_input_data, "airlines_impute_num_vars.txt"), "r")]
list_cat = [line.rstrip('\n') for line in open(os.path.join(path_input_data, "airlines_impute_cat_vars.txt"), "r")]
list_oe_vars = ["UniqueCarrier", "Origin", "Dest"]

pd_airlines.drop(list_num+list_cat, axis=1, inplace=True)
pd_airlines = pd.concat([pd_airlines, pd_airlines_imp_num, pd_airlines_imp_cat], axis=1)

print(pd_airlines.isnull().sum(axis=0))

dict_oe = {}
for var in list_oe_vars:
	with open(os.path.join(path_input_data, var+"_oe_sp.pkl"), "rb") as f:
		sp_oe = pickle.load(f)
		f.close()
	dict_oe[var] = pd.DataFrame.sparse.from_spmatrix(sp_oe)
	dict_oe[var].columns = [var+"_oe_"+str(x) for x in dict_oe[var].columns]
	pd_airlines.drop([var, var+"_le"], axis=1, inplace=True)
	pd_airlines = pd.concat([pd_airlines, dict_oe[var]], axis=1)

target = "IsDelayed"

pd_features = pd_airlines.drop(target, axis=1)
pd_target = pd_airlines[[target]]

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(max_depth=5, random_state=0, n_estimators=3)
model.fit(pd_features, pd_target)

with open(os.path.join(path_output_artifacts, "model_rf_varimp.pkl"), "wb") as f:
	pickle.dump(model, f)
	f.close()
