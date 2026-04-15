import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
data = pd.read_csv("dataset/resumes.csv")

# Convert text into vectors
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(data['skills'])


def get_suggestions(user_input):
    # Convert user input to vector
    user_vec = vectorizer.transform([user_input])
    
    # Calculate similarity
    similarity = cosine_similarity(user_vec, X)
    index = similarity.argmax()
    
    # Get role and full resume text
    role = data.iloc[index]['role']
    full_text = data.iloc[index]['skills']
    
    # 🔥 Clean resume text (extract only words)
    words = re.findall(r'\b[a-zA-Z]+\b', full_text.lower())
    
    # Remove small/unnecessary words
    words = [word for word in words if len(word) > 3]
    
    # Unique skills (limit to 15)
    suggested_skills = list(set(words))[:15]
    
    # 🔥 Clean user input
    user_words = re.findall(r'\b[a-zA-Z]+\b', user_input.lower())
    user_words = [word for word in user_words if len(word) > 3]
    user_words = set(user_words)
    
    # 🔥 Find missing skills
    missing_skills = set(suggested_skills) - user_words
    
    return role, suggested_skills, list(missing_skills)
