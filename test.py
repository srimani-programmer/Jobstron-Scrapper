import xlwt
def write_excel():
    filename = "python_excel_test.xls"
    excel_file = xlwt.Workbook()
    sheet = excel_file.add_sheet('2016')
    row = 0
    col = 0
    ctype = 'string'
    value = 'Rocky1'
    xf = 0
    for i in range(6):
        value = input()
        sheet.write(row, col, value)
        row += 1

    '''
    sheet2 = excel_file.add_sheet('2017')
    row = 0
    col = 0
    ctype = 'string'
    value = 'Rocky122'
    xf = 0
    sheet2.write(row, col, value)
    '''
    excel_file.save(filename) 

write_excel()
