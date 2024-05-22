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
    print('1. Add Contact')
    print('2. Search Contact')
    print('3. Display All Contacts')
    print('4. Delete Contact')
    print('5. Update Contact')
    print('6. Exit.')
    question_str= input('Please choose an option:')

    print(f'option chosen:{question_str}')

get_contact_info()