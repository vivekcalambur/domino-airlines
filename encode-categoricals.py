import os
import pandas as pd
import feather
import pickle
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

path_wd = os.getenv("PATH_WD")
path_input_data = os.getenv("PATH_INPUT_DATA")
path_output_data = os.getenv("PATH_OUTPUT_DATA")
path_output_artifacts = os.getenv("PATH_OUTPUT_ARTIFACTS")
path_airlines = os.path.join(path_input_data, "airlines_small_target_selected.feather")

pd_airlines = feather.read_dataframe(path_airlines)

list_categoricals = ["UniqueCarrier", "Origin", "Dest"]

def one_hot_encode(pd_data, column, path_output_data=".", path_output_artifacts="."):
    le = LabelEncoder()
    oe = OneHotEncoder(dtype="int64")
    column_le = column+"_le"
    column_oe = column+"_oe"
    le.fit(pd_data[column].values.ravel())
    pd_data[column_le] = le.transform(pd_data[column].values.ravel())
    oe.fit([[x] for x in pd_data[column_le]])
    sp_oe = oe.transform([[x] for x in pd_data[column_le]])

    with open(os.path.join(path_output_artifacts, column_le+".pkl"), "wb") as f:
        pickle.dump(le, f)
        f.close()

    with open(os.path.join(path_output_artifacts, column_oe+".pkl"), "wb") as f:
        pickle.dump(oe, f)
        f.close()

    with open(os.path.join(path_output_data, column_oe+"_sp.pkl"), "wb") as f:
        pickle.dump(sp_oe, f)
        f.close()

for var in list_categoricals:
    one_hot_encode(pd_airlines, var, path_output_data, path_output_artifacts)
    pd_airlines[[var, var+"_le"]].to_csv(os.path.join(path_output_data, var+"_le.csv"), index=False)

feather.write_dataframe(pd_airlines, os.path.join(path_output_data, "airlines_small_target_selected_le.feather"))
