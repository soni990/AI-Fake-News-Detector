#app.py main interface 
import streamlit as st
from analyzer import analyze_article 
from utils import extract_from_url

st.title("🔍 AI Fake News Detector") 
st.subheader("Paste an article or enter a URL")

input_type = st.radio(
    "Input type", 
    ["Paste text", "Enter URL"]
) 

if input_type == "Paste text":
    article_text = st.text_area("Paste article here", height=200) 

else:
    url = st.text_input("Enter article URL")
    article_text = extract_from_url(url) if url else ""

if st.button("Analyse Article") and article_text:
    with st.spinner("Analysing..."):
        result = analyze_article(article_text)

# Show trust score

    score = result["trust_score"]
    st.metric("Trust Score", f"{score}/100")

    #color-coded verdict
    if score >= 70:
        st.success("✅ Likely credible")
    elif score >= 40:
        st.warning("⚠️ Needs verification")
    else:
        st.error("❌ Likely misleading")
    
    st.subheader("Why ?")
    st.write(result["explanation"])

    st.subheader("Red Flags found:")
    for flag in result["red_flags"]:
        st.write(f"- {flag}")