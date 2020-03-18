# Making a change here
# Vivek was here
# Vivek < Saahil
import os
import pandas as pd
import numpy as np
import feather

# Preston was here
# Neena was here

path_wd = os.getenv("PATH_WD")
path_input_data = os.getenv("PATH_INPUT_DATA")
input_data = os.getenv("INPUT_DATA")
path_output_data = os.getenv("PATH_OUTPUT_DATA")
path_airlines = os.path.join(path_input_data, input_data)

pd_airlines = pd.read_csv(path_airlines)

print("Starting Shape: " + str(pd_airlines.shape))
print(pd_airlines.isnull().sum(axis = 0))

conditions = [
    (pd_airlines["ArrDelay"] > 0),
    (pd_airlines["ArrDelay"] <= 0)]
choices = [True, False]

pd_airlines["IsDelayed"] = np.select(conditions, choices, default=np.NaN)
pd_airlines.dropna(how='all', subset=["IsDelayed"], inplace=True)

print("\n")
print("Ending Shape: " + str(pd_airlines.shape))
print(pd_airlines.isnull().sum(axis = 0))

feather.write_dataframe(pd_airlines, os.path.join(path_output_data, "airlines_small_target.feather"))
