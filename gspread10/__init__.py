# Google Sheets Features.
# Open a spreadsheet by title, key or url.
# Read, write, and format cell ranges.
# Sharing and access control.
# Batching updates.

# oauth2client library will help us to get the client credientials a to read the data of specific Spread Sheet.

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

def getjsonGspreadData(json_file, gspread_file):
    # use creds to create a client to interact with the Google Drive API
    scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(json_file, scope)
    client = gspread.authorize(creds)   
    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.

    sheet = client.open(gspread_file).sheet1

    # Extract and print all of the values
    list_of_gspread = sheet.get_all_records()
    # return list_of_gspread
    data = pd.DataFrame.from_dict(list_of_gspread)
    return data

# print(getjsonGspreadData("D:\\project videos\\Google sheets\\client_secret.json", "Greendeck Assignment"))   
