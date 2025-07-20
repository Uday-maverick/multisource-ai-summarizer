# 🌐 LangChain YouTube/Web Summarizer

A powerful Streamlit app that uses **LangChain**, **Groq-hosted LLMs**, and **multi-source loaders** to **summarize content from YouTube videos and web pages**. Supports multilingual summaries and customizable word limits.

---

## 🚀 Features

- 🔗 **Summarize from URL**: Supports YouTube videos and websites.
- 🌍 **Multilingual**: Supports summaries in English, Bengali, Hindi, and more.
- 📏 **Custom Summary Length**: Set a word limit for your summary.
- 🧠 **Powered by Groq LLMs**: Leverages Gemma and Mixtral via LangChain.
- ✅ **Minimal UI**: Built with Streamlit for quick deployment.

---

## 🧰 Tech Stack

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Groq LLMs](https://console.groq.com/)
- [LangChain Document Loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/)
- [UnstructuredURLLoader](https://api.python.langchain.com/en/latest/loaders/langchain_community.document_loaders.UnstructuredURLLoader.html)
- [YoutubeLoader](https://python.langchain.com/docs/modules/data_connection/document_loaders/integrations/youtube)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 📸 Demo

<img width="1920" height="1080" alt="Screenshot (272)" src="https://github.com/user-attachments/assets/f6de644a-041a-462d-bb9f-f00ae1854340" />


---

## 📦 Installation

```bash
git clone https://github.com/udayislam/langchain-url-summarizer.git
cd langchain-url-summarizer
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
pip install -r requirements.txt




🔑 Setup Environment Variables
Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key




🏃‍♂️ Run the App

streamlit run app.py




📝 Usage Guide

1. Paste a YouTube video URL or a web article URL.
2. Select the language for the summary.
3. Set the summary word limit.
4. Click Summarize to view results.




📂 Project Structure

langchain-url-summarizer/
|-- app.py
|-- requirements.txt
|-- .env
|-- README.md


🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.





✨ Acknowledgements

LangChain Docs
Groq Console
YouTube & Web Loader Integrations


### 🧠 Next Steps:
- Place this content in a file named `README.md`.
- Replace demo image placeholder with your own screenshot if you have one.
- Upload the repo to GitHub: `git init → git add . → git commit → git remote add origin → git push`.

Would you like me to write a `LICENSE` file or `requirements.txt` as well?
