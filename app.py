from flask import Flask, request, render_template
from bert_model import get_embedding
from scorer import combined_score, rank_candidates
import fitz
import docx
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        doc = fitz.open(file_path)
        return " ".join(page.get_text() for page in doc)
    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        return " ".join(p.text for p in doc.paragraphs)
    return ""

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    jd = ""
    if request.method == "POST":
        jd = request.form.get("jd", "")
        jd_embed = get_embedding(jd)
        files = request.files.getlist("resumes")
        for file in files:
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)
            text = extract_text(path)
            embed = get_embedding(text)
            score = combined_score(embed, jd_embed, text, jd)
            results.append({"name": file.filename, "score": score})
        results = rank_candidates(results)
    return render_template("index.html", results=results, jd=jd)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))