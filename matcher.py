from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resume(resume_text, job_texts):
    docs = [resume_text] + job_texts

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf = vectorizer.fit_transform(docs)

    similarities = cosine_similarity(tfidf[0:1], tfidf[1:])
    scores = similarities[0]

    return scores
