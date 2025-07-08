# As the stage concept is deprecated from the mlflow, we have to provide the tags 
# register model using aliases instead of deprecated stages
# pip install --upgrade mlflow>=2.9

import json
import mlflow
import logging
import os
import dagshub
import warnings

from src.logger import logging

warnings.simplefilter("ignore", UserWarning)
warnings.filterwarnings("ignore")

from dotenv import load_dotenv 

load_dotenv("./.env")

# --------------------- Dasgshub Mlflow Setup --------------------------- 
mlflow.set_tracking_uri(os.getenv("MLFLOW_DAGSHUB_TRACKING_URI"))
dagshub.init(
    repo_owner=os.getenv("REPO_OWNER"),
    repo_name=os.getenv("REPO_NAME"),
    mlflow=True
)
# --------------------- Dasgshub Mlflow Setup Done --------------------------- 

def load_model_info(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as file:
            model_info = json.load(file)
        logging.debug('Model info loaded from %s', file_path)
        return model_info
    except Exception as e:
        logging.error('Error loading model info: %s', e)
        raise

def register_model_with_alias(model_name: str, alias: str, model_info: dict):
    try:
        model_uri = f"runs:/{model_info['run_id']}/{model_info['model_path']}"
        model_version = mlflow.register_model(model_uri, model_name)
        client = mlflow.tracking.MlflowClient()
        client.set_registered_model_alias(
            name=model_name,
            alias=alias,
            version=model_version.version
        )
        logging.debug(f'Model {model_name} version {model_version.version} registered with alias "{alias}".')
    except Exception as e:
        logging.error('Error during model registration with alias: %s', e)
        raise


def main():
    try:
        model_info = load_model_info('reports/experiment_info.json')
        model_name = "my_model"
        alias_name = "staging"  # or "production" as needed
        register_model_with_alias(model_name, alias_name, model_info)
    except Exception as e:
        logging.error('Registration process failed: %s', e)
        print(f"Error: {e}")

if __name__ == '__main__':
    main()