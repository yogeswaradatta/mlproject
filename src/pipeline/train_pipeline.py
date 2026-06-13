import sys

from src.exception import CustomException
from src.logger import logging

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


class TrainPipeline:

    def __init__(self):
        pass

    def run_pipeline(self):

        try:

            logging.info("Training Pipeline Started")

            data_ingestion = DataIngestion()

            train_path, test_path = (
                data_ingestion.initiate_data_ingestion()
            )

            data_transformation = DataTransformation()

            train_arr, test_arr, _ = (
                data_transformation.intiate_data_transformation(
                    train_path,
                    test_path
                )
            )

            model_trainer = ModelTrainer()

            result = model_trainer.intiate_model_trainer(
                train_arr,
                test_arr
            )

            logging.info("Training Pipeline Completed")

            return result

        except Exception as e:
            raise CustomException(e, sys)