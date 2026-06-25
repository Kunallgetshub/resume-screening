# AI Resume Screening System

An AI-powered Resume Screening System built using **Python, Flask, and BERT** that evaluates resumes by comparing them with a job description and generates a relevance score.

---

## Features

- Upload resumes in PDF format
- Extract text from resumes
- Enter a custom job description
- Calculate similarity score using BERT embeddings
- Display resume matching percentage
- Simple and user-friendly web interface

---

## Tech Stack

- Python
- Flask
- Sentence Transformers (BERT)
- HTML
- CSS
- JavaScript
- PDF Text Extraction

---

## Project Structure

```
resume-screening/
│
├── app.py                 # Flask application
├── bert_model.py          # BERT embedding model
├── scorer.py              # Resume scoring logic
├── requirements.txt       # Project dependencies
├── templates/
│   └── index.html
├── uploads/               # Uploaded resumes (ignored by Git)
├── .gitignore
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Kunallgetshub/resume-screening.git
```

### 2. Navigate to the project

```bash
cd resume-screening
```

### 3. Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

---

## Usage

1. Open the application in your browser.

```
http://127.0.0.1:5000
```

2. Enter the job description.

3. Upload a resume (PDF).

4. Click **Screen Resume**.

5. View the similarity score.

---

## How It Works

1. User uploads a resume.
2. Resume text is extracted.
3. User enters a job description.
4. Both texts are converted into BERT embeddings.
5. Cosine similarity is calculated.
6. Matching percentage is displayed.

---

## Future Improvements

- Resume ranking for multiple candidates
- Skill extraction
- Experience detection
- ATS compatibility score
- Resume recommendations
- Support for DOCX resumes
- Recruiter dashboard
- Database integration

---

## Author

**Kunal Sharma**

GitHub: https://github.com/Kunallgetshub

---
