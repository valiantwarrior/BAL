from openpyxl import load_workbook


# Define Class(or DataStructur) that containing Excel data with function(using OpenPyXl)

# For example,
# Training per week
# Author
# Weight unit
# Contents of Cell

# use "test"  sheet

 
#지정 경로에 있는 엑셀 파일 읽어오기
load_wb = load_workbook("test.xlsx", data_only=True)
#특정 시트 사용하기
load_ws = load_wb['Schedules']
 
#스케쥴 이름 및 기본 정보 
print('Schedule Name:'+load_ws['E5'].value+"\n")
print('Author:'+load_ws['S5'].value)
print('Training per week:'+str(load_ws['S6'].value))
print('Weight unit:'+load_ws['S7'].value+"\n")

#Lifting Category Table
multiple_cells = load_ws['R9':'U17']
for row in multiple_cells:
    print("")
    for cell in row:
        if cell.value==None:
         break
        else:
         print(cell.value,end='\t\t')

#Assistance Exercies table
multiple_cells = load_ws['R19':'S25']
for row in multiple_cells:
    print("")
    for cell in row:
        if cell.value==None:
         break
        else:
         print(cell.value,end='\t\t')

#Main Schedule table        
multiple_cells = load_ws['B9':'P117']
for row in multiple_cells:
    print("")
    for cell in row:
       print(cell.value,end='\t')
