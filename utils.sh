#!/bin/bash
print_proj_env_vars() {
	echo "DOMINO_PROJECT_NAME: "$DOMINO_PROJECT_NAME
	echo "DOMINO_STARTING_USERNAME: "$DOMINO_STARTING_USERNAME
	echo "PATH_WD: "$PATH_WD
}

print_env_vars() {
	echo "PATH_INPUT_DATA: "$PATH_INPUT_DATA
	echo "PATH_OUTPUT_DATA: "$PATH_OUTPUT_DATA
	echo "PATH_INPUT_ARTIFACTS: "$PATH_INPUT_ARTIFACTS
	echo "PATH_OUTPUT_ARTIFACTS: "$PATH_OUTPUT_ARTIFACTS
}

print_run_pipeline_stage() {
  TITLE=$1
  COMMAND=$2
  echo -e "\n-----------------------------------------------------"
  echo -e "$TITLE\n"
  echo -e "Environment Variables:"
  print_env_vars
  echo -e "\nRunning $COMMAND ...\n"
  python $COMMAND
}

clean_env_vars() {
  unset INPUT_DATA
  unset PATH_DATA
  unset PATH_INPUT_DATA
  unset PATH_OUTPUT_DATA
  unset PATH_ARTIFACTS
  unset PATH_INPUT_ARTIFACTS
  unset PATH_OUTPUT_ARTIFACTS
}
