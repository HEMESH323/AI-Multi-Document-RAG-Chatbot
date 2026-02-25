import logging
import sys
import os

def setup_logging():
    """Sets up logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('app.log')
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logging()

def get_env_variable(var_name: str, default: str = None) -> str:
    """Safely retrieves an environment variable."""
    value = os.getenv(var_name, default)
    if value is None and default is None:
        logger.error(f"Environment variable {var_name} is not set.")
        raise ValueError(f"Missing required environment variable: {var_name}")
    return value
