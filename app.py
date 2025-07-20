import os
import validators
import streamlit as st
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse, parse_qs

from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader

# Optional fix for YoutubeLoader import error
try:
    from langchain_community.document_loaders import YoutubeLoader
except ImportError:
    YoutubeLoader = None

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# UI setup
st.set_page_config(page_title="🧠 LangChain Summarizer", layout="centered")
st.title("🧠 LangChain Summarizer")
st.markdown("Summarize **YouTube** or **Web URLs** using Groq-hosted LLMs")

with st.sidebar:
    st.header("🔐 Settings")
    st.write(f"API Key Loaded: {'✅ Yes' if groq_api_key else '❌ No'}")
    if not groq_api_key:
        groq_api_key = st.text_input("Enter your Groq API Key", type="password")
    model = st.selectbox("LLM Model", ["gemma2-9b-it"])

# Input fields
url = st.text_input("🔗 Enter YouTube or Website URL")
col1, col2 = st.columns(2)
with col1:
    language = st.selectbox("🌐 Language", ["English", "Hindi", "Bengali", "Spanish"])
with col2:
    word_limit = st.selectbox("✂️ Word Limit", [100, 300, 500], index=1)

# Prompt Template
template = """You are a helpful assistant. Please summarize the content in about {word_limit} words.
Use {language} language and correct script.

Content:
{text}
"""
prompt = PromptTemplate(template=template, input_variables=["text", "word_limit", "language"])

def sanitize_youtube_url(url):
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)
    video_id = qs.get("v", [None])[0]
    return f"https://www.youtube.com/watch?v={video_id}" if video_id else url

def fetch_web_text(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers, timeout=10, verify=True)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    return "\n\n".join(p.get_text() for p in soup.find_all("p"))

def fetch_youtube_transcript(url):
    if not YoutubeLoader:
        raise ImportError("YoutubeLoader is not available.")
    loader = YoutubeLoader.from_youtube_url(url, add_video_info=False)
    docs = loader.load()
    return "\n\n".join(doc.page_content for doc in docs)

if st.button("📝 Summarize Now"):
    if not groq_api_key or not validators.url(url):
        st.error("❗ Please check API key and valid URL.")
        st.stop()
    
    try:
        with st.spinner("Fetching content..."):
            if "youtube.com" in url or "youtu.be" in url:
                sanitized_url = sanitize_youtube_url(url)
                text = fetch_youtube_transcript(sanitized_url)
            else:
                text = fetch_web_text(url)

            if not text.strip():
                st.error("❗ No readable content found.")
                st.stop()

            llm = ChatGroq(groq_api_key=groq_api_key, model=model)
            chain = LLMChain(prompt=prompt, llm=llm)
            result = chain.run(text=text, word_limit=word_limit, language=language)
            st.success("✅ Summary:")
            st.text_area("📄 Output", result, height=300)

    except Exception as e:
        st.error(f"🚨 Error: {str(e)}")

