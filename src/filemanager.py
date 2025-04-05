import os
import pandas as pd
from src.logging_system import logger

class FileManager:
    def __init__(self):
        self.current_path = os.getcwd()

        # dictionaries
        self.data_path = os.path.join(self.current_path, "data")
        self.datasets = os.path.join(self.data_path, "datasets")
        self.preprocess = os.path.join(self.data_path, "preprocess")
        self.results = os.path.join(self.data_path, "results")
        self.graph = os.path.join(self.data_path, "graph")

        # files
        self.download_model = os.path.join(self.datasets, "BAN-PL.csv")
        self.save_preprocessed = os.path.join(self.preprocess, 'Preprocess.csv')
        self.model_save = os.path.join(self.results, "model.safetensors")
        # self.cout_labels = os.path.join(self.graph, "cout_labels.png")
        self.classyfication_report = os.path.join(self.graph, "classification_report.txt")

        self.create_directories()


    def create_directories(self):
        directories = [
            self.data_path,
            self.datasets,
            self.preprocess,
            self.results,
            self.graph
        ]

        for directory in directories:
            if not os.path.exists(directory):
                os.makedirs(directory)

    @staticmethod
    def save_dataset(dataset, path: str):
        logger.info(f"Saving dataset to path: {path}...")
        dataset.to_csv(path, index=False)
        logger.info("Dataset successfully saved")

    @staticmethod
    def load_dataset(path: str):
        logger.info(f"Start loading the dataset from the path: {path}...")
        df = pd.read_csv(path)
        logger.info("Dataset successfully loaded")
        return df