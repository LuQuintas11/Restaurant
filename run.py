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
SHEET = GSPREAD_CLIENT.open('Menu-')
VEGAN_DATA = SHEET.worksheet("Vegan")
VEGAN= VEGAN_DATA.get_all_values()

data=[]
def order_menu(worksheet, data):
    data_order= input(f"What is your order: '1'.{worksheet[1]}, '2'.{worksheet[2]}, '3'.{worksheet[3]}")
    if data_order=='1':
        data.append(worksheet[1])
    

def update_worksheet(data):
    SHEET.worksheet("orders").append_row(data)       




def get_name_data():

    """
    Get order input from user
    """
    data_name= input("What is your name:")
    data.append(data_name)
    print(f"Hello {data_name}. We are ready to take your order!")
    while True:
        data_menu = input(f"choose a number: '1.Vegan'. Or choose option '2' to finish your order")
        if data_menu=='1':
            print(f"{VEGAN}")
            order_menu(VEGAN, data)
        elif data_menu=='2':
            update_worksheet(data)
            break
  
    
get_name_data()

