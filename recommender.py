import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("movies_data.csv")

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

df['cleaned'] = df['Storyline'].apply(clean_text)

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['cleaned'])

def recommend_movies(user_input, top_n=5):
    user_input = clean_text(user_input)
    user_vector = vectorizer.transform([user_input])
    similarity_scores = cosine_similarity(user_vector, tfidf_matrix).flatten()
    top_indices = similarity_scores.argsort()[-top_n:][::-1]

    results = df.iloc[top_indices][['Movie Name', 'Storyline']].copy()
    results['Similarity Score'] = similarity_scores[top_indices]
    return results.reset_index(drop=True)