import logging
from src.nlp_app import NLPApp

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    try:
        logging.info("Starting NLPApp")
        obj = NLPApp()
    except Exception as e:
        logging.error("Error starting NLPApp: %s", e)
