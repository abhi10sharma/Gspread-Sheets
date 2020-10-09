
# GSPREAD10

![Sheets to Python](https://twilio-cms-prod.s3.amazonaws.com/original_images/python-and-sheets.png)

# Introduction

This is an python package which helps us to read the data of google spread sheets from your google drive and then you can manipulate the data using [pandas](https://pypi.org/project/pandas/) and plot graph using [matplotlib](https://pypi.org/project/matplotlib/)
***

## Features

1. Easy to use
2. Easy to understand
3. Very helpful for reading the data from Google Sheets

# Inside the Package

Before installing this package there is one important thing which you have to do first. You have to enable your Google Drive API and Google Sheets API from [Google APIs Console](console.developers.google.com).

## Steps to enable [Google Drive API](https://www.google.com/intl/en_in/drive/)

1. Go to the Google APIs Console.
2. Create a new project.
3. Click Enable API. Search for and enable the Google Drive API.
4. Create credentials for a Web Server to access Application Data.
5. Name the service account and grant it a Project Role of Editor.
6. Download the [JSON](https://www.json.org/json-en.html) file.
7. Give any specfic name of your [JSON](https://www.json.org/json-en.html) file
8. Then Search [Google Sheets API](https://developers.google.com/sheets/api) and then click on enable.
9. Open your [JSON](https://www.json.org/json-en.html) file and copy the client_email.
10. Open your [GOOgLE SPREADSHEETS](https://www.google.com/sheets/about/) and click on share button on the right top.
11. Paste your client_email and then click on send button.


# Code Description

## Library Used

I have used the [gspread](https://pypi.org/project/gspread/) and [oauth2client](https://pypi.org/project/oauth2client/) service to authorize and make API calls to Google Cloud Services.

### Importing Library

```python
pip install gspread oauth2client
```

### Features of **`gspread`** library

1. Google Sheets API v4.
2. Open a spreadsheet by title, key or url.
3. Read, write, and format cell ranges.
4. Sharing and access control.
5. Batching updates.

### About **`oauth2client`**

This library will help us to get the client credientials a to read the data of specific Spread Sheet.
***

# LET'S GET STARTED

# How to Install

```python
 pip install gspread10
```

The name of this package is "gspread10" and you can use this package to read the data from [GOODLE SPREADSHEETS](https://www.google.com/sheets/about/) in [JSON](https://www.json.org/json-en.html) format and then using [pandas](https://pypi.org/project/pandas/) you can manipulate the data in table using [DataFrames](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) and for Data Visualization you can use [Matplotlib](https://pypi.org/project/matplotlib/).

## Function to read the data

To read the data from c you have to use `getjsonGspreadData(json_file, gspread_file)` function and inside the function you have to give the path of your [JSON](https://www.json.org/json-en.html) file and the name of your [GOODLE SPREADSHEETS](https://www.google.com/sheets/about/).
For example:- I want to read the data from [Greendeck](https://www.greendeck.co/) Assignment file. So Here How it should be written.

``` Python
getjsonGspreadData("your_JSON_Path", "Greendeck Assignment")
```

# Code for Reading the file from [GOOGLE SPREADSHEETS](https://www.google.com/sheets/about/)

```Python
# Google Sheets Features.
# Open a spreadsheet by title, key or url.
# Read, write, and format cell ranges.
# Sharing and access control.
# Batching updates.

# oauth2client library will help us to get the client credentials a to read the data of specific Spread Sheet.

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

```

I went throung several websites to get the idea of 'How to read data from Google Spread Sheet'. So finally I got this website --> [medium.com](https://medium.com/analytics-vidhya/how-to-read-and-write-data-to-google-spreadsheet-using-python-ebf54d51a72c). You can go through this website.

# License

This package is distributed under the [MIT license](https://opensource.org/licenses/MIT).

# Download

[https://pypi.org/project/gspread10/0.0.1/](https://pypi.org/project/gspread10/0.0.1/)
