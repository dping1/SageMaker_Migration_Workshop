# The SageMaker container will pass hyperparamter and other environment variable in the form of command line parameters to the train script

import argparse
import os

# Parser function for getting command line arguments
def parse_args():
    parser = argparse.ArgumentParser()

    # hyperparameters sent by the client are passed as command-line arguments to the script.   
    # Change the lines below to add hyperpamaters that work with your algorithm
    parser.add_argument('--epochs', type=int, default=1)
    parser.add_argument('--learning_rate', type=float, default=0.01)
    
    # Data, model, and output directories.  Do not change this.
    parser.add_argument('--model-dir', type=str, default=os.environ['SM_MODEL_DIR'])
    parser.add_argument('--train', type=str, default=os.environ['SM_CHANNEL_TRAIN'])
    parser.add_argument('--validation', type=str, default=os.environ['SM_CHANNEL_VALIDATION'])
    parser.add_argument('--test', type=str, default=os.environ['SM_CHANNEL_TEST'])
    
    return parser.parse_known_args()