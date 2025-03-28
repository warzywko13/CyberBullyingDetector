import os

import pandas as pd

from src.logs import logger

class Manager:

    @staticmethod
    def load_dataset_from_path(path: str):
        logger.info(f"Start loading the dataset from the path: {path}...")
        dataset = pd.read_csv(path)
        logger.info("Dataset successfully loaded")
        return dataset
    
    @staticmethod
    def save_dataset(dataset, path: str):
        logger.info(f"Saving dataset to path: {path}...")
        dataset.to_csv(path, index=False)
        logger.info("Dataset successfully saved")