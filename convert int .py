import xlrd
loc ="E:\saurabh\project\\saurabha_bunary.xlsx"
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
sheet.cell_value(0,0)
r = sheet.nrows
for i in range(r):
    for j in range(sheet.ncols):
        print(int(str(int(sheet.cell_value(i,j))),2))
    print() 
