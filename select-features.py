import os
import pandas as pd
import feather
import numpy as np
import pickle

path_wd = os.getenv("PATH_WD")
path_input_data = os.getenv("PATH_INPUT_DATA")
path_output_data = os.getenv("PATH_OUTPUT_DATA")
path_airlines = os.path.join(path_input_data, "airlines_small_target.feather")

pd_airlines = feather.read_dataframe(path_airlines)

print("Starting Shape: " + str(pd_airlines.shape))
print("Columns: " + str(pd_airlines.columns))

list_drop= [line.rstrip('\n') for line in open(os.path.join(path_input_data, "airlines_leakage_vars.txt"), "r")]
pd_airlines.drop(list_drop, axis=1, inplace=True)

print("Starting Shape: " + str(pd_airlines.shape))
print("Columns: " + str(pd_airlines.columns))

feather.write_dataframe(pd_airlines, os.path.join(path_output_data, "airlines_small_target_selected.feather"))
