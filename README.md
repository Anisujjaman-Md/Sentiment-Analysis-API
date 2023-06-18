# Sentiment Analysis API (FastAPI)

The Sentiment Analysis API is a backend service that provides sentiment analysis on text input. It exposes a RESTful API endpoint implemented using the FastAPI web framework.

## Requirements

- Python 3.10+
- FastAPI
- setfit

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/Anisujjaman-Md/Sentiment-Analysis-API.git
   
2. Navigate to the project directory:

    ```shell
   cd Sentiment-Analysis-API
   
3. Create a virtual environment and activate it:

    ```shell
    python3 -m venv venv
    source venv/bin/activate  # for Linux/Mac
    venv\Scripts\activate  # for Windows

4. Install the dependencies:

    ```shell
    pip install -r requirements.txt
   
## Usage

1. Start the server:

    The API will be accessible at http://localhost:8000

    ```shell
    uvicorn main:app --reload

2. Send a POST request to http://localhost:8000/analyze with the following payload. Replace "Text to be analyzed" with the actual text you want to analyze.

    ```json
   {"text": "Text to be analyzed"}

3. The API will respond with the sentiment analysis result:
    
    ```json
   {"sentiment": "positive/negative/neutral"}