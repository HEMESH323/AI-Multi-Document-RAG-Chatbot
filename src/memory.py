from langchain.memory import ConversationBufferMemory
from src.utils import logger

class MemoryManager:
    """Manages conversational memory."""
    
    def __init__(self):
        logger.info("Initializing MemoryManager...")
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True,
            output_key="answer"
        )

    def get_memory(self):
        """Returns the memory object."""
        return self.memory

    def clear_memory(self):
        """Clears the conversational memory."""
        logger.info("Clearing chat history...")
        self.memory.clear()

