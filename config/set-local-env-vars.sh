#!/bin/bash
if [ -z "${INPUT_DATA}" ]
then
  export INPUT_DATA=airlines_10k.csv
fi

export PATH_DATA=$PATH_WD/example_data
export PATH_INPUT_DATA=$PATH_DATA
export PATH_OUTPUT_DATA=$PATH_DATA
export PATH_ARTIFACTS=$PATH_WD/artifacts
export PATH_INPUT_ARTIFACTS=$PATH_ARTIFACTS
export PATH_OUTPUT_ARTIFACTS=$PATH_ARTIFACTS

mkdir -p $PATH_ARTIFACTS
