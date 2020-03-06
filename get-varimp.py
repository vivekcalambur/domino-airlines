# Some comment
import os
import pandas as pd
import feather
import numpy as np
import pickle

path_wd = os.getenv("PATH_WD")
path_input_artifacts = os.getenv("PATH_INPUT_ARTIFACTS")
path_output_artifacts = os.getenv("PATH_OUTPUT_ARTIFACTS")

with open(os.path.join(path_input_artifacts, "model_rf_varimp.pkl"), "rb") as f:
	model = pickle.load(f)
	f.close()

with open(os.path.join(path_output_artifacts, "model_rf_varimp.txt"), "w") as f:
	f.writelines("%s\n" % x for x in model.feature_importances_)
	f.close()
