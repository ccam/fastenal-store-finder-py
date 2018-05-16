# NOTE:
# write script to pull table from site and then paste into google sheets. then beable to pull from that.


import gspread
from oauth2client.service_account import ServiceAccountCredentials


def main():
    search()
    # display()


def search():
    # menu:
    menu = input(
        'How would you like to search? (1) 5 Letter, (2) City, (3) State: ')

    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'client_secret.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    sheet = client.open("fastenalStores-5-14-18").sheet1

    if menu == '1':  # 5code
        query = input('Enter search term: ')
        try:
            cell = sheet.find(query.upper())
            results = sheet.row_values(cell.row)
            print('''
        4 letter: %s 
        5 letter: %s
        Addresss: %s %s, %s %s %s
        Phone: %s
        Email: %s@stores.fastenal.com
        ''' % (results[0], results[1], results[2], results[3], results[4], results[5], results[6], results[7], results[1]))
        except Exception:
            print('not found, try again!')

    elif menu == '2':  # City
        query = input('Enter search term: ')
        try:
            cell = sheet.findall(query.capitalize())
            for c in cell:
                results = sheet.row_values(c.row)
                print('''
                    4 letter: %s 
                    5 letter: %s
                    Addresss: %s %s, %s %s %s
                    Phone: %s
                    Email: %s@stores.fastenal.com
                    ''' % (results[0], results[1], results[2], results[3], results[4], results[5], results[6], results[7], results[1]))
        except Exception:
            print('Not found, try again!')

    elif menu == '3':  # State
        query = input('Enter search term: ')
        try:
            cell = sheet.findall(query.upper())
            for c in cell:
                results = sheet.row_values(c.row)
                print('''
          4 letter: %s 
          5 letter: %s
          Addresss: %s %s, %s %s %s
          Phone: %s
          Email: %s@stores.fastenal.com
          ''' % (results[0], results[1], results[2], results[3], results[4], results[5], results[6], results[7], results[1]))
        except Exception:
            print('Not found, try again!')

    else:
        print('Wrong input! Try again!')


main()
