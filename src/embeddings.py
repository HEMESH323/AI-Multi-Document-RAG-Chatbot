from langchain_community.embeddings import HuggingFaceEmbeddings
from src.utils import logger

class EmbeddingManager:
    """Manages the generation of text embeddings."""
    
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        logger.info(f"Initializing EmbeddingManager with model: {model_name}")
        self.embeddings = HuggingFaceEmbeddings(model_name=model_name)

    def get_embeddings(self):
        """Returns the embeddings object."""
        return self.embeddings
