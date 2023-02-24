import openpyxl
import xlrd

path = str("../data/WUP2018-F13-Capital_Cities.xls")
try:
    wb = xlrd.open_workbook(path.strip())
    ws = wb.sheet_by_index(0)

    print(f"{wb.nsheets}")
    print(f"{wb.sheet_names()}")

    for sheet in wb.sheets():
        print(sheet)

    #for row in range(2, max_row+1):
except Exception as e:
    print(e)

