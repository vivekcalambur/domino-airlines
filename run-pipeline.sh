#!/bin/bash
if [ -z "$1" ]
then
  RUNTIME_ENV="local"
else
  RUNTIME_ENV=$1
fi


source utils.sh

if [ $RUNTIME_ENV == "local" ]
then
  source config/set-local-env-vars.sh
elif [ $RUNTIME_ENV == "domino-workspace-ex" ]
then 
  source config/set-domino-workspace-ex-env-vars.sh
elif [ $RUNTIME_ENV == "domino-workspace-ex-dataset" ]
then 
  source config/set-domino-workspace-ex-dataset-env-vars.sh
elif [ $RUNTIME_ENV == "domino-job-ex" ]
then 
  source config/set-domino-job-ex-env-vars.sh
elif [ $RUNTIME_ENV == "domino-job-ex-dataset" ]
then 
  source config/set-domino-job-ex-dataset-env-vars.sh
else
  source config/set-local-env-vars.sh
fi

print_proj_env_vars 
echo -e "INPUT_DATA: $INPUT_DATA"
print_run_pipeline_stage "Create Target" create-target.py
print_run_pipeline_stage "Select Features" select-features.py
print_run_pipeline_stage "Impute Missing" impute-missing.py
print_run_pipeline_stage "Encode Categoricals" encode-categoricals.py
print_run_pipeline_stage "Train Reference Variable Importance Model" train-ref-varimp-model.py
print_run_pipeline_stage "Get Variable Importance" get-varimp.py

clean_env_vars
