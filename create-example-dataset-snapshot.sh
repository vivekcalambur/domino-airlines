#!/bin/bash
if [ -z "${1}" ]
then
  echo -e "Need to specify a dataset: create-example-dataset-snapshot.sh DATASET_NAME"
else
  cp $DOMINO_WORKING_DIR/example_data/* $HOME/datasets/output/$1
  cp $DOMINO_WORKING_DIR/domino.yaml $HOME/files/$DOMINO_PROJECT_NAME/
fi
