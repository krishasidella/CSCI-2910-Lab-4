from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env
api_key = os.getenv('API_KEY')  # Access your API key
