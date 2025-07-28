import streamlit as st
import pandas as pd
import random

# Page config
st.set_page_config(page_title="Emory Admissions Training", layout="centered")

# Load questions
df = pd.read_csv("emory-admissions-training-questions.csv")
all_questions = df.to_dict(orient="records")

# Sidebar controls
with st.sidebar:
    st.header("🛠 Settings")
    mode = st.radio("Mode", ["Training Mode", "Test Mode"])
    quiz_length = st.selectbox("Quiz length", [5, 10, 15])


if "previous_quiz_length" not in st.session_state:
    st.session_state.previous_quiz_length = quiz_length

if "previous_mode" not in st.session_state:
    st.session_state.previous_mode = mode

# If quiz settings change, reset session state
if (
    quiz_length != st.session_state.previous_quiz_length
    or mode != st.session_state.previous_mode
):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()


# Header and intro
col1, col2 = st.columns([1, 6])
with col1:
    st.image("emory_logo.png", width=60)
with col2:
    st.title("Emory Admissions Training Assistant")
    st.write(
        "This system is designed for new hires in Emory's Office of Undergraduate Admission. "
        "It aims to help you become confident and well-informed about Emory's key policies and frequently asked questions."
    )

st.markdown("---")

# Session state initialization
if "questions" not in st.session_state:
    st.session_state.questions = random.sample(all_questions, quiz_length)
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.user_answers = []
    st.session_state.finished = False

# Progress bar
progress = (st.session_state.current_q) / quiz_length
st.progress(progress)

# Quiz in progress
if not st.session_state.finished:
    current_q = st.session_state.current_q
    q = st.session_state.questions[current_q]

    st.subheader(f"❓ Question {current_q + 1} of {quiz_length}")
    st.caption(f"Category: {q['category']}")
    st.write(q['question'])

    options = [q['option1'], q['option2'], q['option3'], q['option4']]
    answer = st.radio("Choose your answer:", options, key=f"q{current_q}")

    if st.button("Submit", key=f"submit_{current_q}"):
        selected = answer

        st.session_state.user_answers.append({
            "question": q['question'],
            "selected": selected,
            "correct": q['answer']
        })

        if mode == "Training Mode":
            if selected == q['answer']:
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Incorrect. Correct answer: {q['answer']}")

        if selected == q['answer']:
            st.session_state.score += 1

        if current_q + 1 < quiz_length:
            st.session_state.current_q += 1
            st.rerun()
        else:
            st.session_state.finished = True
            st.rerun()

# Quiz complete
if st.session_state.finished:
    st.balloons()
    st.subheader("🎉 Quiz Complete!")
    st.write(f"**Final Score: {st.session_state.score} / {quiz_length}**")

    pct = st.session_state.score / quiz_length
    if pct >= 0.8:
        st.success("🏆 Excellent! You're ready to take calls.")
    elif pct >= 0.5:
        st.info("🟡 Good effort — review a few areas.")
    else:
        st.warning("🔴 Needs more training — consider revisiting key topics.")

    if mode == "Test Mode":
        st.subheader("📝 Answer Review:")
        for idx, ans in enumerate(st.session_state.user_answers):
            st.write(f"**Q{idx+1}:** {ans['question']}")
            if ans['selected'] == ans['correct']:
                st.success(f"Your answer: {ans['selected']} ✅")
            else:
                st.error(f"Your answer: {ans['selected']} ❌ | Correct: {ans['correct']}")

    if st.button("Restart Quiz"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
