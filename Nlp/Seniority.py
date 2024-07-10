import pandas as pd
import re
import spacy
import os
import joblib
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import logging
from sklearn.feature_extraction.text import CountVectorizer
import xgboost as xgb

# Download NLTK resources
# nltk.download('stopwords')
# nltk.download('punkt')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

nlp = spacy.load("en_core_web_lg")


def clean_text(text):
    text = text.lower()  
    text = re.sub(r'\d+', '', text)  
    text = re.sub(r'\W+', ' ', text)  
    text = re.sub(r'\s+', ' ', text) 
    return text

def lemmatize_tokens(tokens, model):
    doc = model(" ".join(tokens))
    return [token.lemma_ for token in doc]

logging.info("Reading dataset.csv")
df = pd.read_csv('Nlp/jupyter_notebook/BIG_DATASET.csv', delimiter=';')


if not os.path.exists('Nlp/preprocessed_text.csv'):
    stop_words = set(stopwords.words('english'))
    logging.info("Cleaning and preprocessing text")
    df['text'] = df['text'].apply(clean_text)

    logging.info("tokenizing")
    df['tokens'] = df['text'].apply(word_tokenize)

    logging.info("Removing StopWords")
    df['tokens'] = df['tokens'].apply(lambda x: [word for word in x if word not in stop_words])
    
    logging.info("lemantizing")
    df['tokens'] = df['tokens'].apply(lambda x: lemmatize_tokens(x, nlp))
    df = df.dropna(subset=['tokens'])
    logging.info("token-lambda")
    df['tokens'] = df['tokens'].apply(lambda x: ' '.join(x))
    df.to_csv('preprocessed_text.csv', index=False)
    logging.info("Preprocessed text saved to preprocessed_text.csv")
else:
    logging.info("Preprocessed text already exists, skipping preprocessing step")
    df = pd.read_csv('Nlp/preprocessed_text.csv')
    df = df.dropna(subset=['tokens'])

def train(df):
    X_train, X_test, y_train, y_test = train_test_split(df['tokens'], df['seniority_number'], test_size=0.25, stratify=df['seniority_number'], random_state=None)
    vectorizer = CountVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    model = xgb.XGBClassifier()
    model.fit(X_train_vec, y_train)
    y_pred = model.predict(X_test_vec)
    accuracy = accuracy_score(y_test, y_pred)
    return model, vectorizer, accuracy

logging.info("Training and exporting model and vector")
model, vectorizer, accuracy_model = train(df)
logging.info("Model accuracy: {:.2f}".format(accuracy_model))

joblib.dump(model, 'model_seniority.pkl')
joblib.dump(vectorizer, 'vectorizer_seniority.pkl')
