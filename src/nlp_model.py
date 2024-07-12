import google.generativeai as genai
import logging

class NLPModel:
    def get_model(self):
        try:
            genai.configure(api_key="##########")  # Enter your Gemini API key
            model = genai.GenerativeModel("gemini-pro")
            return model
        except Exception as e:
            logging.error("Error configuring the model: %s", e)
            raise
