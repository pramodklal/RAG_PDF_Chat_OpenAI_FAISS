from setuptools import find_packages, setup

setup(
    name="RAGChatPDFBOT",
    version="0.0.1",
    author="Pramod",
    author_email="pramodklal@gmail.com",
    packages=find_packages(),
    install_requires=['langchain==0.0.184','PyPDF2==3.0.1','python-dotenv==1.0.0 ','streamlit==1.18.1','openai==0.27.6','faiss-cpu==1.7.4','altair==4','tiktoken==0.4.0','huggingface-hub==0.14.1','InstructorEmbedding==1.0.1','sentence-transformers==2.2.2u']
)