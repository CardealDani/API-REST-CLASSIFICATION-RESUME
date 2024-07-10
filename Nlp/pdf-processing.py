import pandas as pd
import re
import spacy
import fitz 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import joblib
import numpy as np
from jupyter_notebook.classMap import class_mapping
# nltk.download('stopwords')
# nltk.download('punkt')

nlp = spacy.load("en_core_web_lg")
model = joblib.load('/Nlp/model-class.pkl')
vectorizer = joblib.load('/Nlp/vectorizer-class.pkl')



def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', '', text)  
    text = re.sub(r'@\w+', '', text)  
    text = re.sub(r'\d+', '', text)  
    text = re.sub(r'\W+', ' ', text)  
    text = re.sub(r'\s+', ' ', text).strip()  
    return text


def lemmatize_tokens(tokens):
    doc = nlp(" ".join(tokens))
    return [token.lemma_ for token in doc]


def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text


def preprocess_text(text):
    text = clean_text(text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    tokens = lemmatize_tokens(tokens)
    return " ".join(tokens)

def predict_formation(pdf_path, model, vectorizer):
    text = extract_text_from_pdf(pdf_path)
    processed_text = preprocess_text(text)
    X = vectorizer.transform([processed_text])
    prediction = model.predict(X)
    probabilities = model.predict_proba(X)
    return prediction,probabilities


def top_probabilities(probabilities):
    top_indices = np.argsort(probabilities[0])[::-1][:5]
    result = []
    for idx in top_indices:
        class_name = [key for key, value in class_mapping.items() if value == idx][0]
        prob_percent = probabilities[0][idx] * 100
        result.append(f"{class_name}: {prob_percent:.2f}%") 
    return result



    

pdf_path = 'path_file.pdf'
result,probabilities = predict_formation(pdf_path,model,vectorizer)
top_probabilities(probabilities)