import matplotlib.pyplot as plt
import seaborn as sns

import nltk
from nltk import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer
import stopwordsiso as stopwordsiso

from src.filemanager import FileManager

class Graph:
    @staticmethod
    def count_graph(df):
        file_manager = FileManager()

        plt.figure(figsize=(6, 4))
        sns.countplot(data=df, x='label', palette='Set2')
        plt.title("Label Distribution (Toxic vs Neutral)")
        plt.xlabel("Label")
        plt.ylabel("Count")
        plt.savefig(file_manager.cout_labels)

        numerical_columns = ['No_of_Characters', 'No_of_Words', 'No_of_Sentences']
        sns.pairplot(df[numerical_columns + ['label']], hue='label', palette='Set1')

        stop_words = set(stopwordsiso.stopwords('pl'))
        # WordCloud for spam and ham messages
        spam_words = ' '.join(df[df['label'] == 1]['message'])
        ham_words = ' '.join(df[df['label'] == 0]['message'])

        # Remove stopwords for better word cloud generation
        spam_words_cleaned = ' '.join([word for word in spam_words.split() if word.lower() not in stop_words])
        ham_words_cleaned = ' '.join([word for word in ham_words.split() if word.lower() not in stop_words])

        # Plot WordCloud
        plt.figure(figsize=(14, 7))
        plt.subplot(1, 2, 1)
        wordcloud_spam = WordCloud(width=400, height=200, background_color='black').generate(spam_words_cleaned)
        plt.imshow(wordcloud_spam, interpolation='bilinear')
        plt.axis('off')
        plt.title("Spam Messages WordCloud")

        plt.subplot(1, 2, 2)
        wordcloud_ham = WordCloud(width=400, height=200, background_color='white').generate(ham_words_cleaned)
        plt.imshow(wordcloud_ham, interpolation='bilinear')
        plt.axis('off')
        plt.title("Ham Messages WordCloud")

        plt.show()

        # Top spam vs ham words using CountVectorizer
        vectorizer = CountVectorizer(stop_words='polish', max_features=10)

        # Fit and transform on spam and ham messages
        spam_vectorized = vectorizer.fit_transform(df[df['label'] == 1]['message'])
        ham_vectorized = vectorizer.fit_transform(df[df['label'] == 0]['message'])

        # Get the top 10 words for spam and ham
        spam_word_freq = sorted(zip(vectorizer.get_feature_names_out(), spam_vectorized.sum(axis=0).A1), key=lambda x: x[1], reverse=True)
        ham_word_freq = sorted(zip(vectorizer.get_feature_names_out(), ham_vectorized.sum(axis=0).A1), key=lambda x: x[1], reverse=True)

        # Print top words
        print("\nTop spam words:", spam_word_freq[:10])
        print("Top ham words:", ham_word_freq[:10])