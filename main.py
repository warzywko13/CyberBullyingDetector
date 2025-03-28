from src import (
    parser,
    logger,
    Manager,
    FilePath,
    Preprocess
)

def main() -> None:
    """Execute The main function."""
    logger.info("Start application")
    args = parser()

    if args.preprocessing:
        dataset = Manager.load_dataset_from_path(FilePath.download_model)
        preprocess_dataset = Preprocess.preprocess(dataset)
        Manager.save_dataset(preprocess_dataset, FilePath.save_preprocessed)

    logger.info("Finish application")

if __name__ == "__main__":
    main()