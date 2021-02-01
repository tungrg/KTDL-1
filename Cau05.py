def deleteColumn(listRow, rate):
    #lấy số lượng các dòng
    num_attr = len(listRow)
    # chuyển từ % ngưỡng tỉ lệ ra số dữ liệu cụ thể của cột
    n = num_attr * float(rate) / 100
    #tạo biến mới lưu lại tập dữ liệu
    temp_listRow = []
    #tạo ra 1 bản copy của dữ liệu ban đầu
    for i in range(len(listRow)):
        b = listRow[i].copy()
        temp_listRow.append(b)
    #duyệt từng cột
    for key in listRow[0].keys():
        t = 0
        #với mỗi cột thì reset biến đếm
        count = 0
        #duyệt từng dòng trong cột
        for row in listRow:
            #nếu ở dòng đó mà cột không có dữ liệu thì tăng biến đếm
            if row[key] == '':
                count += 1
            #nếu lượng dữ liệu thiếu trong cột vượt ngưỡng ban đầu thì xóa cột đó và chuyển sang duyệt cột tiếp theo
            if count > n:
                for index in range(len(listRow)):
                    temp_listRow[index].pop(key)
                break
        t += 1
    #trả vệ tập dữ liệu mới sau khi xóa cột
    return temp_listRow