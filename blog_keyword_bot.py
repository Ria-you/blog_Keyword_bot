
import streamlit as st
import re
from collections import Counter

st.set_page_config(page_title="블로그 키워드 추천기", layout="centered")

st.title("📌 블로그 키워드 & 해시태그 자동 추천기")
st.write("블로그 초안을 붙여넣으면 주요 키워드와 해시태그를 추천해드립니다.")

text = st.text_area("📝 블로그 본문 입력", height=300, placeholder="여기에 본문 내용을 붙여넣어주세요...")

STOPWORDS = ['합니다', '있습니다', '경기', '중계', '시청', '보기', '이번', '있다', '있는']

def extract_keywords(text, top_n=10):
    words = re.findall(r'[가-힣]{2,}', text)
    words = [w for w in words if w not in STOPWORDS]
    return Counter(words).most_common(top_n)

if st.button("🔍 키워드 추출하기"):
    if not text.strip():
        st.warning("본문을 먼저 입력해주세요.")
    else:
        keywords = extract_keywords(text)
        hashtags = ['#' + word for word, _ in keywords]

        st.subheader("📌 주요 키워드")
        for word, count in keywords:
            st.markdown(f"- **{word}** ({count}회)")

        st.subheader("📣 추천 해시태그")
        st.code(" ".join(hashtags), language='markdown')
