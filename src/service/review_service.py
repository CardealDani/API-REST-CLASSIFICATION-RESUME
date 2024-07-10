import re
import spacy
import fitz 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import joblib
import numpy as np
import os
from dotenv import load_dotenv
from service.classMaping import class_mapping
from service.classMaping import class_mapping_seniority
from model.review_model import ReviewResponse
# nltk.download('stopwords')
# nltk.download('punkt')
nlp = spacy.load("en_core_web_lg")

load_dotenv()
model = joblib.load(os.getenv('model_class')) 
vectorizer = joblib.load(os.getenv('vectorizer_class'))
model_seniority = joblib.load(os.getenv('model_seniority'))
vectorizer_seniority = joblib.load(os.getenv('vectorizer_seniority'))



class ReviewService:
    @classmethod
    def get_review(self,id_curriculum:int,file:bytes):
        probabilities_area, seniority = self.predict_formation(file,model,vectorizer,model_seniority,vectorizer_seniority)
        top_probs = self.top_probabilities(probabilities_area)
        response = ReviewResponse(id_curriculum=id_curriculum,occupation_area=str(top_probs[0]),top_probabilities=top_probs, seniority=str(seniority))
        return response


    @classmethod
    def extract_text_from_pdf(self,file:bytes):
        doc = fitz.open(stream=file, filetype="pdf")
        text = ""
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()
        return text

    @classmethod
    def clean_text(self,text):
        text = text.lower()
        text = re.sub(r'http\S+', '', text)  
        text = re.sub(r'@\w+', '', text)  
        text = re.sub(r'\d+', '', text)  
        text = re.sub(r'\W+', ' ', text)  
        text = re.sub(r'\s+', ' ', text).strip()  
        return text

    @classmethod
    def lemmatize_tokens(self,tokens):
        doc = nlp(" ".join(tokens))
        return [token.lemma_ for token in doc]

    @classmethod
    def preprocess_text(self,text):
        text = self.clean_text(text)
        tokens = word_tokenize(text)
        stop_words = set(stopwords.words('english'))
        tokens = [word for word in tokens if word not in stop_words]
        tokens = self.lemmatize_tokens(tokens)
        return " ".join(tokens)
    
    @classmethod
    def predict_formation(self,file, model_occupation, vectorizer_occupation, model_seniority, vectorizer_seniority):
        text = self.extract_text_from_pdf(file)
        processed_text = self.preprocess_text(text)

        area_vectorized = vectorizer_occupation.transform([processed_text])
        probabilities_area = model_occupation.predict_proba(area_vectorized)

        seniority_vectorized = vectorizer_seniority.transform([processed_text])
        seniority_predict = model_seniority.predict(seniority_vectorized)
        seniority = [key for key, value in class_mapping_seniority.items() if value == seniority_predict]
        return probabilities_area, seniority[0]

    @classmethod
    def top_probabilities(self,probabilities):
        top_indices = np.argsort(probabilities[0])[::-1][:3]
        result = []
        for idx in top_indices:
            class_name = [key for key, value in class_mapping.items() if value == idx][0]
            prob_percent = probabilities[0][idx] * 100
            result.append(f"{class_name}: {prob_percent:.2f}%") 
        return result
    
