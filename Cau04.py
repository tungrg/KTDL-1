def deleteRow(listRow, rate): #hàm xóa dòng với ngưỡng
    temp_listRow = listRow.copy()
    #lấy số lượng các cột
    num_attr = len(listRow[0].keys())
    # chuyển từ % tỉ lệ ra số thuộc tính bị thiếu
    n = num_attr * float(rate) / 100
    #duyệt từng dòng
    for row in listRow:
        count = 0
        #duyệt từng thuộc tính trong dòng đó
        for key in listRow[0].keys():
            if row[key] == '':
                #đếm số lượng thuộc tính thiếu của dòng
                count += 1
            #nếu số lượng thuộc tính thiếu nhiều hơn ngưỡng thì xóa dòng
            if count > n:
                temp_listRow.remove(row)
                break
    #trả về tập dữ liệu sau khi xóa dòng
    return temp_listRow