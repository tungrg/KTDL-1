import  math
import Cau03
import  Cau01
def allNumeric(listRow):
    all_num = []
    #kiem tra cac thuoc tinh tinh co phai la so hay khong
    for key in listRow[0].keys():
        for row in listRow:
            if row[key] != '':
                if row[key].count('.') != 0: #kiem tra gia tri cua thuoc tinh co chua dau "."
                    all_num.append(key)
                    break
                else:
                    if row[key].isnumeric():
                        all_num.append(key)
                        break
    return all_num
def setAttributeByMin_MaxMethod(listRow, chuoi):
    temp = []
    check = 0
    check1 = 0
    for attr in chuoi.split("-"): # truy xuat tung thuoc tinh trong 1 chuoi
        if attr not in allNumeric(listRow):
            check1 += 1
            if check1 <= len(chuoi.split('-')):
                print(attr + " Khong phai la mot thuoc tinh so hoac khong co trong danh sach cac thuoc tinh.")
                if check1 == len(chuoi.split('-')):
                    return 0
        else:
            list1 = []
            #sao chep temp_lisRow tu listRow
            temp_listRow = []
            for row in listRow:
                if row[attr] != '':
                    list1.append(float(row[attr]))
            max1 = max(list1)
            min1 = min(list1)
            t = max1 - min1
            name = attr + " Min-Max" #cot chuyen hoa tuong ung voi thuoc tinh do
            for i in range(len(listRow)):
                b = listRow[i].copy()
                temp_listRow.append(b)
            if check == 0:
                for row in temp_listRow:
                    if row[attr] == '':
                        temp.append({attr: row[attr], name: ''})
                    else:
                        value = (float(row[attr]) - min1) / t #gia tri chuyen doi (x-min)/(max-min)
                        temp.append({attr: row[attr], name: value})
                check += 1
            else:
                count = 0
                for row in temp_listRow:
                    #xuat hoa cac thuoc tinh con lai bat dau tu thuoc tinh thu 2.
                    if row[attr] == '':
                        temp[count][attr] = row[attr]
                        temp[count][name] = ''
                    else:
                        value = (float(row[attr]) - min1) / t
                        temp[count][attr] = row[attr]
                        temp[count][name] = value
                    count += 1
    return temp

def setAttributeByZ_ScoreMethod(listRow, chuoi):
    temp =[]
    check1 = 0
    check = 0
    for attr in chuoi.split("-"):
        if attr not in allNumeric(listRow): #kiem tra attr co phai thuoc tinh so hay khong
            check1 += 1
            if check1 <= len(chuoi.split('-')):
                print(attr + " Khong phai la mot thuoc tinh so hoac khong co trong danh sach cac thuoc tinh.")
                if check1 == len(chuoi.split('-')):
                    return 0
        else:
            temp_listRow = []
            name = attr + " Z-Score" # ten thuoc tinh chuyen doi cua thuoc tinh dang xet
            for i in range(len(listRow)):
                b = listRow[i].copy()
                temp_listRow.append(b)
            if attr in Cau03.attributeNumeric(listRow):
                xich_ma = 0
                n = len(listRow) - Cau01.cau01(listRow)[attr]
                #tinh mean cua thuoc tinh dang xet
                count = 0
                tong = 0
                for row in listRow:
                    if row[attr] != '':
                        count += 1
                        tong += float(row[attr])
                x = tong / count
                for row in temp_listRow:
                    if row[attr] != '':
                        xich_ma += 1/(n-1)*pow((float(row[attr]) - x), 2) #cong thu tinh do lech chuan
                xich_ma = math.sqrt(xich_ma) #cong thu tinh do lech chuan
                if check == 0:
                    for row in temp_listRow:
                        if row[attr] != '':
                            z = (float(row[attr]) - x) / xich_ma # cong thuc tinh z-score
                            temp.append({attr: row[attr], name: z})
                        else:
                            temp.append({attr: row[attr], name: ''})
                    check += 1
                else:
                    count = 0
                    #chuan hoa cac thuoc tinh con lai bawt dau tu thuoc tinh thu 2 co trong chuoi
                    for row in temp_listRow:
                        if row[attr] != '':
                            z = (float(row[attr]) - x) / xich_ma
                            temp[count][attr] = row[attr]
                            temp[count][name] = z
                        else:
                            temp[count][attr] = row[attr]
                            temp[count][name] = ''
                        count += 1
            else:
                xich_ma = 0
                sum = 0
                for row in temp_listRow:
                    sum += float(row[attr])
                average = sum / len(listRow)
                for row in temp_listRow:
                    xich_ma += 1/(len(listRow)-1)*pow((float(row[attr]) - average), 2) #cong thu tinh do lech chuan
                xich_ma = math.sqrt(xich_ma) #cong thu tinh do lech chuan
                if check == 0:
                    for row in temp_listRow:
                        if xich_ma == 0:
                            z = 0
                        else:
                            z = (float(row[attr]) - average) / xich_ma #cong thu tinh z-score
                        temp.append({attr: row[attr], name: z})
                    check += 1
                else:
                    count = 0
                    for row in temp_listRow:
                        if xich_ma == 0:
                            z = 0
                        else:
                            z = (float(row[attr]) - average) / xich_ma #cong thu tinh z-score
                        temp[count][attr] = row[attr]
                        temp[count][name] = z
                        count += 1
    return temp