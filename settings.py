from dotenv import load_dotenv
from os import environ

load_dotenv()

valid_email = environ.get('USERNAME')
valid_password = environ.get('PASSWORD')
