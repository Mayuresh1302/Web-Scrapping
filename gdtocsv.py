import requests
import csv
import time
import schedule

# Define the Google Sheets ID and desired range (optional)
SPREADSHEET_ID = '1sSrcqlRj1ZrEQjjkaR7fGCcvqIb58CypvzetUe0XeFQ'
RANGE_NAME = 'Sheet1!A1:D'  # Use the name of your sheet, e.g., 'Sheet1'

# 1. Construct the URL for the public Google Sheets CSV export
url = f"https://docs.google.com/spreadsheets/d/1sSrcqlRj1ZrEQjjkaR7fGCcvqIb58CypvzetUe0XeFQ/export?format=csv"

# 2. Fetch the CSV data from the public Google Sheets URL
def fetch_google_sheet_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# 3. Write the fetched data to a CSV file
def save_to_csv(data, filename='google_sheet_data.csv'):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            file.write(data)
        print(f"Data successfully written to {filename}")
    except Exception as e:
        print(f"An error occurred while saving to CSV: {e}")

# Function to fetch and save data
def sync_data():
    sheet_data = fetch_google_sheet_data(url)
    if sheet_data:
        save_to_csv(sheet_data)

# Schedule the function to run every 5 minutes
schedule.every(5).minutes.do(sync_data)

# 4. Main function to fetch and save data
if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1) 
    sheet_data = fetch_google_sheet_data(url)
    if sheet_data:
        save_to_csv(sheet_data)
