import pickle
import re

# Load files
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Clean function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text

# Prediction function
def predict_news(text, threshold=0.8):
    vec = vectorizer.transform([text])
    
    prob = model.predict_proba(vec)[0]
    real_prob = prob[0]
    fake_prob = prob[1]

    if fake_prob > threshold:
        result = "🚨 Fake News"
    else:
        result = "✅ Real News"

    return result, fake_prob, real_prob