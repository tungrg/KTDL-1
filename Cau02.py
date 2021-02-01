def cau02(listRow):
    count=0
    #Duyệt từng dòng
    for row in listRow:
        #xét từng giá trị của cột trong dòng đó
        for key in listRow[0].keys():
            if row[key] == '':
                count += 1
                break
    #In ra số dòng bị thiếu dữ liệu
    print(count)
    return count