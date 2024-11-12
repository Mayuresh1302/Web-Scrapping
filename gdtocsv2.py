import os
import pickle
import pandas as pd
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Define the required scope for reading Google Sheets
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of the Google Sheet to fetch data from
SPREADSHEET_ID = '1sSrcqlRj1ZrEQjjkaR7fGCcvqIb58CypvzetUe0XeFQ'  # Replace with your Google Sheets ID
RANGE_NAME = 'Sheet1!A1:Z1000'  # Modify the range as required (e.g., 'Sheet1!A1:D10')

# Authenticate and initialize Google Sheets API
def authenticate_google_sheets():
    creds = None
    # The token.pickle file stores the user's access and refresh tokens, and is created automatically when the
    # authorization flow completes for the first time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no valid credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret_977018422022-agoelbm3q4lrj7sn7m42nggqfbq7h988.apps.googleusercontent.com.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

# Retrieve data from the specified Google Sheet
def get_sheet_data(creds):
    try:
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()

        # Call the Sheets API to get the data
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
        else:
            return values
    except HttpError as err:
        print(f"An error occurred: {err}")
        return None

# Convert the sheet data to a CSV
def save_to_csv(data):
    if data:
        # Convert the list of rows to a pandas DataFrame and save it to a CSV file
        df = pd.DataFrame(data[1:], columns=data[0])  # The first row is the header
        df.to_csv('google_sheet_data.csv', index=False)
        print("Data saved to 'google_sheet_data.csv'")
    else:
        print("No data to save.")

# Main function to authenticate and process the sheet data
def main():
    creds = authenticate_google_sheets()
    sheet_data = get_sheet_data(creds)
    save_to_csv(sheet_data)

if __name__ == '__main__':
    main()
