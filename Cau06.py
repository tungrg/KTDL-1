def DeleteDuplicateRows(listRow):
    #tạo 1 set để chứa các dòng không bị trùng
    seen = set()
    #tạo 1 biến để lưu lại tập dữ liệu mới
    new_l = []
    #duyệt từng dòng
    for d in listRow:
        #tạo biến t mang kiểu dữ liệu tuple của dòng đó
        t = tuple(d.items())
        #nếu t chưa từng xuất hiện trong set thì add t vào set và thêm dòng đó vào tập dữ liệu mới
        if t not in seen:
            seen.add(t)
            new_l.append(d)
    #trả về tập dữ liệu mới sau khi đã loại bỏ các dòng trùng lắp
    return new_l