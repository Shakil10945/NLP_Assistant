# NLP Assistant

NLP Assistant provides NLP functionalities like sentiment analysis, language translation, and language detection using Google's Generative AI.

## Features

- **Sentiment Analysis:** Determine the sentiment of text.
- **Language Translation:** Translate text to Bengali.
- **Language Detection:** Detect the language of text.

## Directory Structure

NLPAssistant/
├── src/
│ ├── init.py
│ ├── nlp_model.py
│ └── nlp_app.py
└── main.py

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/NLPAssistant.git
    cd NLPAssistant
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Configure API Key:**
    Replace the placeholder in `src/nlp_model.py` with your Google Generative AI API key.

## Usage

Run the application:
```sh
python main.py
