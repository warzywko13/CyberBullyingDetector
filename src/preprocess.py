class Preprocess:
    @staticmethod
    def remove_nans(dataset):
        return dataset.dropna()
    
    @staticmethod
    def remove_duplicates(dataset):
        return dataset.drop_duplicates()

    @staticmethod
    def preprocess(dataset):
        df_cleaned = Preprocess.remove_nans(dataset)
        df_cleaned = Preprocess.remove_duplicates(df_cleaned)
        return df_cleaned
