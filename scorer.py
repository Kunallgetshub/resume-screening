from sklearn.metrics.pairwise import cosine_similarity
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

def keyword_score(resume_text, jd_text):
    jd_words = set(jd_text.lower().split()) - stop_words
    resume_words = set(resume_text.lower().split())
    if not jd_words:
        return 0
    return len(jd_words & resume_words) / len(jd_words)

def combined_score(resume_embed, jd_embed, resume_text, jd_text):
    semantic = cosine_similarity([resume_embed], [jd_embed])[0][0]
    keyword = keyword_score(resume_text, jd_text)
    return round(0.6 * float(semantic) + 0.4 * keyword, 4)

def rank_candidates(candidates):
    return sorted(candidates, key=lambda x: x["score"], reverse=True)