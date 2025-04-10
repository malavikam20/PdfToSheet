import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
CREDENTIALS_PATH = os.path.join("credentials", "credentials.json")
TOKEN_PATH = os.path.join("credentials", "token.json")


def authorize_google_sheets():
    creds = None
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, 'r') as token:
            creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(TOKEN_PATH, 'w') as token:
            token.write(creds.to_json())
    return build('sheets', 'v4', credentials=creds)
from google.auth.transport.requests import Request

def read_sheet_data(spreadsheet_id, range_name):
    service = authorize_google_sheets()
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name).execute()
    return result.get('values', [])

def write_to_sheet(spreadsheet_id, range_name, values):
    service = authorize_google_sheets()
    body = {'values': values}
    return service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id, range=range_name,
        valueInputOption='USER_ENTERED', body=body).execute()
