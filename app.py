import streamlit as st
import joblib

st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰",
    layout="centered"
)

# ---------- CSS ----------
st.markdown("""
<style>

/* Background */
.stApp{
    background: linear-gradient(135deg,#74ebd5,#ACB6E5);
}

/* Main container */
.main > div{
    background:white;
    padding:35px;
    border-radius:20px;
    box-shadow:0px 8px 25px rgba(0,0,0,0.25);
}

/* Text Area */
textarea{
    border-radius:12px !important;
    border:2px solid #1976D2 !important;
    font-size:16px !important;
}

/* Button */
.stButton>button{
    width:100%;
    background:linear-gradient(90deg,#1565C0,#42A5F5);
    color:white;
    border:none;
    border-radius:12px;
    height:55px;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:linear-gradient(90deg,#0D47A1,#1976D2);
    color:white;
}

/* Success */
.stSuccess{
    border-radius:10px;
}

/* Error */
.stError{
    border-radius:10px;
}

/* Footer */
.footer{
    text-align:center;
    color:#444;
    margin-top:25px;
    font-size:15px;
}

</style>
""", unsafe_allow_html=True)


# ---------- Load Model ----------
vectorizer = joblib.load("vectorizer.jb")
model = joblib.load("lr_model.jb")

# ---------- Header ----------
st.title("📰 Fake News Detector")

st.write(
    "Enter a news article below to check whether it is **Real** or **Fake** using an AI-powered text classification model."
)

# ---------- Input ----------
news_input = st.text_area(
    "📝 News Article",
    height=220,
    placeholder="Paste the complete news article here..."
)

# ---------- Prediction ----------
if st.button("🔍 Check News"):

    if news_input.strip():

        transform_input = vectorizer.transform([news_input])

        prediction = model.predict(transform_input)

        if prediction[0] == 1:
            st.balloons()
            st.success("✅ Prediction: This news is REAL.")
        else:
            st.error("❌ Prediction: This news is FAKE.")

    else:
        st.warning("⚠ Please enter a news article.")

# ---------- Footer ----------
st.markdown(
    """
<div class="footer">
<hr>
Developed using ❤️ Python | Streamlit | Scikit-learn
</div>
""",
    unsafe_allow_html=True,
)