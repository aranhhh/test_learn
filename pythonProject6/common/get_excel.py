import xlrd2  #导入excel包
def get_excel_row(row,col):
    excel = xlrd2.open_workbook("../testdata/userdata.xlsx")
    table = excel.sheets()[0]
    # print(table.cell_value(row, col))
    return table.cell_value(row, col)

# if __name__ == '__main__':
#     get_excel_row(0)