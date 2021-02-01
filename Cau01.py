
def cau01(listRow):
    res = []
    #tạo biến nhớ tạm để lưu kết quả
    #duyệt từng cột
    for key in listRow[0].keys():
        #reset biến đếm với từng cột
        count = 0
        #duyệt từng dòng trong cột đó
        for row in listRow:
            if row[key] == '':
                res.append((key, count))
                count += 1
    #chuyển biến từ list về lại dictionary ban đầu
    res = dict(res)
    return res