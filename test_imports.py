try:
    import streamlit
    import langchain
    import langchain_google_genai
    import faiss
    import sentence_transformers
    import pypdf
    from dotenv import load_dotenv
    print("All imports successful!")
except ImportError as e:
    print(f"Import failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
