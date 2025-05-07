from src.filemanager import FileManager
from src.preprocess import Preprocess
from src.logging_system import logger
from src.parser import parser
from src.train import Train

from src.evaluation import Evaluation

def main() -> None:
    """Execute The main function."""
    logger.info("Start application")
    args = parser()

    file_manager = FileManager()

    if args.preprocessing:
        dataset = file_manager.load_dataset(file_manager.download_model)
        preprocess_dataset = Preprocess.preprocess(dataset)
        file_manager.save_dataset(preprocess_dataset, file_manager.save_preprocessed)

    if args.train:
        dataset = file_manager.load_dataset(file_manager.save_preprocessed)

        Train.execute(dataset, file_manager)

    if args.test:
        evaluation = Evaluation(file_manager.results)
        print(evaluation.predict("Nienawidzę cię"))


if __name__ == "__main__":
    main()