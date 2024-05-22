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

# Main function to create contact book
def get_contact_info():
    """
    REQUEST CONTACT INFORMATION INPUT FROM USER 
    """
while True:

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

    if choice == '1':
        name = input('Enter name: ')
        number = input('Enter number: ')
        add_contact(name, number)
    elif choice == '2':
       name = input('Enter name to search: ')
       search_contact(name)
    elif choice == '3':
        display_all_contacts()
    elif choice == '4':
       name = input('Enter name to delete: ')
       delete_contact(name)
    elif choice == '5':
        name = input('Enter name to update: ')
        new_number = input('Enter new number: ')
        update_contact(name, new_number)

