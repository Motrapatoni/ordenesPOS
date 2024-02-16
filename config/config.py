import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    PEDIDOSYA_TOKEN = os.getenv('PEDIDOSYA_TOKEN')
    BASE_URL = 'https://partners-pedidosya.deliveryhero.io'
