from src.graph import Graph

import nltk
from nltk import word_tokenize,sent_tokenize
import spacy.cli

import re

spacy.cli.download("pl_core_news_sm")
nlp = spacy.load("pl_core_news_sm")

nltk.download('stopwords', 'polish')
nltk.download('punkt')

class Preprocess:
    @staticmethod
    def remove_duplicates(df):
        return df.drop_duplicates()

    @staticmethod
    def preprocess_text(text):
        text = str(text).replace("\n", " ")
        text = str(text).replace("\n", " ")
        text = str(text).replace("{USERNAME}:", "")
        text = str(text).replace("{USERNAME}", "")
        text = str(text).replace("{URL}", "")
        text = str(text).replace("{EMAIL}", "")
        text = str(text).replace("pseudonym", "")
        text = str(text).replace("surname", "")
        text = text.lower()
        text = re.sub(r'[^a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ0-9\s]', '', text)

        doc = nlp(text)
        lemmas = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
        return ' '.join(lemmas)
    
    @staticmethod
    def remove_outliers_iqr(df, column):
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    
    @staticmethod
    def rename_columns(df):
        df = df[['Text', 'Class']]
        df.columns = ['message', 'label']
        return df
    
    @staticmethod 
    def create_extra_columns(df):
        df['No_of_Characters'] = df['message'].apply(len)
        df['No_of_Words'] = df.apply(lambda row: word_tokenize(row['message']), axis=1).apply(len)
        df['No_of_Sentences'] = df.apply(lambda row: sent_tokenize(row['message']), axis=1).apply(len)
        return df

    @staticmethod
    def preprocess(df):
        df = Preprocess.rename_columns(df)
        df = Preprocess.create_extra_columns(df)

        df = Preprocess.remove_duplicates(df)
        df = Preprocess.remove_outliers_iqr(df, "No_of_Characters")
        df = Preprocess.remove_outliers_iqr(df, "No_of_Words")

        df['clean_message'] = df['message'].apply(Preprocess.preprocess_text)

        df = df.dropna(subset=['clean_message'])
        df['clean_message'] = df['clean_message'].astype(str)
        df = df[df['clean_message'].str.strip() != '']

        return df
