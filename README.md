# 🤖 AI Resume Matcher & Job Analyzer

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/HridayBhadouria/ai-resume-matcher/graphs/commit-activity)

A powerful CLI-based system that leverages **Natural Language Processing (NLP)** and **Machine Learning** to match resumes against multiple job descriptions. It provides deep insights into candidate suitability and identifies critical skill gaps.

---

## 🚀 Key Features

-   **Multi-Format Support**: Parse resumes in both `.pdf` and `.txt` formats seamlessly using `PyPDF2`.
-   **Advanced NLP Preprocessing**: Clean and normalize text using `NLTK`, removing noise and stop words for better matching accuracy.
-   **Intelligent Skill Extraction**: Automatically identifies key technical skills from both the resume and job descriptions.
-   **AI-Powered Matching**: Uses **TF-IDF Vectorization** and **Cosine Similarity** to calculate precise match scores between the candidate and the role.
-   **Actionable Insights**: 
    -   Detailed percentage-based match scores.
    -   Lists existing common skills.
    -   **Skill Gap Analysis**: Highlights missing keywords required for the job.
-   **Bulk Job Processing**: Match a single resume against a whole folder of job descriptions in one go.

---

## 🛠️ Tech Stack

-   **Language**: [Python](https://www.python.org/)
-   **Machine Learning**: [scikit-learn](https://scikit-learn.org/) (TF-IDF, Cosine Similarity)
-   **NLP**: [NLTK](https://www.nltk.org/)
-   **PDF Parsing**: [PyPDF2](https://pypdf2.readthedocs.io/)

---

## 📦 Installation & Setup

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/HridayBhadouria/ai-resume-matcher.git
    cd ai-resume-matcher
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Download NLTK Data**:
    The system will automatically download necessary NLTK data (like stopwords) on the first run.

---

## 🖥️ Usage

Run the analyzer via the command line by providing your resume path and the folder containing job descriptions:

```bash
python main.py path/to/your_resume.pdf path/to/jobs_folder/
```

### 📄 Example Output

```text
MATCH RESULTS

Job: Senior_Software_Engineer.txt
Match Score: 85.5%
Your Skills: ['python', 'git', 'sql', 'aws', 'docker']
Job Skills: ['python', 'git', 'sql', 'aws', 'docker', 'kubernetes', 'terraform']
Missing Skills: ['kubernetes', 'terraform']
--------------------------------------------------
```

---

## 📂 Project Structure

```text
ai-resume-matcher/
├── main.py              # Application entry point
├── matcher.py           # ML Matching logic (TF-IDF)
├── skill_extractor.py   # Keyword matching & skill lists
├── text_utils.py        # NLP cleaning & preprocessing
├── requirements.txt     # Project dependencies
└── jobs/                # Directory for target job descriptions (.txt)
```

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

---
*Developed with ❤️ by [Hriday Bhadouria](https://github.com/HridayBhadouria)*
