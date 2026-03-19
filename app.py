import streamlit as st
from model import predict_news

# Page config
st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #1f77b4;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #555;
        }
        .box {
            background-color: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Title section
st.markdown('<div class="title">📰 Fake News Detection</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Analyze whether a news article is Fake or Real using AI</div>', unsafe_allow_html=True)

st.write("")

# Input box inside styled container
with st.container():
    st.markdown('<div class="box">', unsafe_allow_html=True)

    news_input = st.text_area("✍️ Enter News Text:", height=200)

    st.markdown("</div>", unsafe_allow_html=True)

# Fixed threshold
THRESHOLD = 0.8

st.write("")

# Centered button
col1, col2, col3 = st.columns([1,2,1])
with col2:
    predict_btn = st.button("🔍 Analyze News")

# Prediction logic
if predict_btn:
    if news_input.strip() == "":
        st.warning("⚠️ Please enter some news text.")
    else:
        result, fake_prob, real_prob = predict_news(news_input, THRESHOLD)

        st.write("")

        # Result section
        with st.container():
            st.markdown('<div class="box">', unsafe_allow_html=True)

            st.subheader("📊 Prediction Result")

            if result.lower() == "fake":
                st.error("🚫 This news is likely FAKE")
            else:
                st.success("✅ This news is likely REAL")

            st.markdown("---")

            st.subheader("📈 Confidence Scores")

            st.write(f"Fake Probability: {fake_prob*100:.2f}%")
            st.progress(float(fake_prob))

            st.write(f"Real Probability: {real_prob*100:.2f}%")
            st.progress(float(real_prob))

            st.markdown("</div>", unsafe_allow_html=True)