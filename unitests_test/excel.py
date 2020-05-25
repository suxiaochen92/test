import xlrd

class Excel:
    def __init__(self,name,sheet):
        self.name=name
        self.sheet=sheet
    def on(self):
        sheet=xlrd.open_workbook(self.name).sheet_by_name(self.sheet)
        row=sheet.nrows
        col=sheet.ncols
        cell=sheet.cell_value(1,1)
        table=[]
        for i in range(1,row):
            table.append(sheet.row_values(i))
        return table