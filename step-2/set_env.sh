export SM_OUTPUT_DATA_DIR=./opt/ml/output/
echo $SM_OUTPUT_DATA_DIR
export SM_MODEL_DIR=./opt/ml/model
echo $SM_MODEL_DIR
export SM_CHANNEL_TRAIN=./opt/ml/input/data/training
echo $SM_CHANNEL_TRAIN
export SM_CHANNEL_VALIDATION=./opt/ml/input/data/testing
echo $SM_CHANNEL_TESTING