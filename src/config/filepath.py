import os

class FilePath:
    current_path = os.getcwd()

    # dictionaries
    data_path = os.path.join(current_path, "data")
    datasets = os.path.join(data_path, "datasets")
    models = os.path.join(data_path, "models")
    preprocess = os.path.join(data_path, "preprocess")


    # files
    download_model = os.path.join(datasets, "BAN-PL.csv")
    save_preprocessed = os.path.join(preprocess, 'Preprocess.csv')