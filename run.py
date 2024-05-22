import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('contact_book')

def get_contact_info():
    """
    REQUEST CONTACT INFORMATION INPUT FROM USER 
    """
    print('-------------------------------')
    print('---------CONTACT BOOK----------')
    print('-------------------------------')
    question_str= input('Please choose an option:(Add, Search, Delete, Display All):\n')

    print(f'The data provided is {question_str}')

get_contact_info()