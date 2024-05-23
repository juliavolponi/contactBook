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
        option= input('Please choose an option: ')

        if option == '1':
          name = input('Enter name: ')
          number = input('Enter number (only numbers): ')
          add_contact(name, number)
        elif option == '2':
         name = input('Enter name to search: ')
         search_contact(name)
        elif option == '3':
          display_all_contacts()
        elif option == '4':
         name = input('Enter name to delete: ')
         delete_contact(name)
        elif option == '5':
          name = input('Enter name to update: ')
          new_number = input('Enter new number: ')
          update_contact(name, new_number)
        elif option == '6':
          print('Exiting contact book ')
          break
        else:
          print("Invalid option. Please try again.")

# Function to add contact
def add_contact(name, number):
    """
    FUNCTION TO ADD CONTACT TO CONTACT BOOK
    """
    try:
        number = int(number)  # Ensure number is an integer
    except ValueError:
        print("Invalid number. Please enter a valid integer.")
        return

    lower_name = name.lower()  # Convert name to lowercase
    data = [name, lower_name, number]
    contacts_worksheet = SHEET.worksheet('contact')
    contacts_worksheet.append_row(data)
    print(f"Contact '{name}' added successfully!")

# Function to search contact
def search_contact(name):
    """
    FUNCTION TO SEARCH CONTACT IN CONTACT BOOK
    """
    contacts_worksheet = SHEET.worksheet('contact')
    try:
        all_records = contacts_worksheet.get_all_records()
        lower_name = name.lower()
        found_contacts = []
        for record in all_records:
            if lower_name in record.get('LowerName', '').lower():
                found_contacts.append(record)
        
        if found_contacts:
            for contact in found_contacts:
                print(f"Contact found: Name: {contact['Name']}, Number: {contact['Number']}")
        else:
            print(f"Contact '{name}' not found.")
    except gspread.exceptions.GSpreadException as e:
        print(f"An error occurred: {e}")

# Function to display all contacts
def display_all_contacts():
    """
    FUNCTION TO DISPLAY ALL CONTACTS
    """
    contacts_worksheet = SHEET.worksheet('contact')
    all_contacts = contacts_worksheet.get_all_records()
    for contact in all_contacts:
        print(f"Name: {contact['Name']}, Number: {contact['Number']}")

# Function to delete contact
def delete_contact(name):
    """
    FUNCTION TO DELETE A CONTACT BY NAME
    """
    contacts_worksheet = SHEET.worksheet('contact')
    try:
        all_records = contacts_worksheet.get_all_records()
        lower_name = name.lower()
        for idx, record in enumerate(all_records, start=2):  # start=2 to account for header row
            if lower_name in record.get('LowerName', ''):
                # Confirmation prompt
                confirm = input(f"Are you sure you want to delete the contact '{record['Name']}'? (yes/no): ")
                if confirm.lower() == 'yes':
                    contacts_worksheet.delete_rows(idx)
                    print(f"Contact '{record['Name']}' deleted successfully.")
                else:
                    print("Deletion cancelled.")
                return
        print(f"Contact '{name}' not found.")
    except gspread.exceptions.GSpreadException as e:
        print(f"An error occurred: {e}")


get_contact_info()

