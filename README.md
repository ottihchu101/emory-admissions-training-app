# Emory Admissions Training App

This is a web-based training quiz designed for new hires in Emory University's Office of Undergraduate Admission (OUA). It transforms frequently asked questions and key policy information into an interactive quiz format to help student assistants and new staff members learn the essentials quickly and effectively.

## 🌟 Features

- Interactive multiple-choice quiz with real OUA questions
- Two quiz modes:
  - **Training Mode**: Get feedback after each question
  - **Test Mode**: Review answers only after completing the quiz
- Category tags for each question (e.g., Financial Aid, I-20s, Applications)
- Score tracking and end-of-quiz performance feedback
- Emory branding with support for dark theme (Streamlit settings dependent)
- Designed for self-guided onboarding and staff refreshers

## 📁 File Structure

```
emory-admissions-training-app/
├── quiz_app.py                          # Main Streamlit application
├── questions.csv                        # Editable quiz question bank
├── requirements.txt                    # Python dependencies for deployment
├── assets/
│   └── emory_logo.png                  # Emory shield or logo
├── .streamlit/
│   └── config.toml                     # Optional Streamlit dark theme config
└── venv/                                # Local virtual environment (should not be pushed to GitHub)
```

> 💡 Make sure to **exclude the `venv/` folder** from GitHub by adding it to `.gitignore`:
```
venv/
```

## 🚀 How to Run

1. Clone the repo:
```bash
git clone https://github.com/YOUR_USERNAME/emory-admissions-training-app.git
cd emory-admissions-training-app
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate   # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Launch the app:
```bash
streamlit run quiz_app.py
```

## 🌐 Live Demo (if deployed)

> Coming soon: [https://your-username.streamlit.app](https://your-username.streamlit.app)

## 📝 How to Update the Questions

To change the quiz questions:
- Open `questions.csv`
- Ensure headers remain the same:
  ```
  question,option1,option2,option3,option4,answer,category
  ```
- Save and push changes back to the repository

Streamlit Cloud will automatically update the live app with the new questions.

## 👤 Author

Chukwudi (Chuchu) Ottih  
Emory University — Summer 2025 Project  
