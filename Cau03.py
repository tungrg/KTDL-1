import Cau01
def attributeNumeric(listRow):
    num = []
    #tận dụng câu 1 để lấy các cột bị thiếu dữ liệu
    for key in Cau01.cau01(listRow).keys():
        #Duyệt từng dòng trong cột bị thiếu
        for row in listRow:
            #Nếu dòng đó có dữ liệu
            if row[key] != '':
                #kiểm có dấu chấm trong dữ liệu đó không (tức là xem thử có phải số thực không)
                if row[key].count('.') != 0:
                    #thêm cột đó vào ds cột bị thiếu dữ liệu numberic và break để xét cột tiếp theo
                    num.append(key)
                    break
                else:
                    #nếu không có dấu chấm thì dùng method isnumeric của python để kiểm tra xem có phải numeric hay không
                    if row[key].isnumeric():
                        #thêm cột đó vào ds cột bị thiếu dữ liệu numberic và break để xét cột tiếp theo
                        num.append(key)
                        break
    #Trả về danh sách cột thuộc kiểu numeric bị thiếu dữ liệu
    return num
def attributeCategorical(listRow):
    attr_str = []
    #lưu các cột  kiểu numeric bị thiếu dữ liệu
    num = attributeNumeric(listRow)
    #Xét trong các cột bị thiếu dữ liệu
    for key in Cau01.cau01(listRow).keys():
        #nếu cột đang xét mà không phải là cột kiểu numeric thì nó là cột kiểu categorical
        if key not in num:
            #thêm cột đó vào danh sách các cột kiểu categorical
            attr_str.append(key)
    #trả về danh sách các cột thuộc kiểu categorical bị thiếu
    return attr_str
def calculateMean(listRow): #hàm tính mean và điền các giá trị vào cột
    #Cập nhật các dữ liệu bị thiếu kiểu categorical
    listRow = calculateMode(listRow)
    mean = []
    array= []
    #xét các cột kiểu numeric mà bị thiếu dữ liệu
    for key in attributeNumeric(listRow):
        sum = 0
        count = 0
        #xét các dòng không bị thiếu dữ liệu để tính mean
        for row in listRow:
            if row[key] != '':
                count += 1
                sum += float(row[key])
        average = sum / count
        #thêm mean của cột đó vào 1 biến nhớ
        mean.append((key, average))
    #chuyển biến thành kiểu dictionary
    mean = dict(mean)
    #cập nhật các giá trị bị thiếu bằng mean của của thuộc tính
    for key in listRow[0].keys():
        if key in mean.keys():
            for row in listRow:
                if row[key] == '':
                    row[key] = mean[key]
    #trả về listRow mới đã được điền đầy đủ các thuộc tính thiếu bằng mean và mode
    return listRow
def calculateMedian(listRow):#hàm tính median và điền các giá trị vào cột
    #Cập nhật các dữ liệu bị thiếu kiểu categorical
    listRow = calculateMode(listRow)
    median = []
    #xét các cột kiểu numeric mà bị thiếu dữ liệu
    for key in attributeNumeric(listRow):
        array = []
        #xét các dòng không bị thiếu dữ liệu để tính mediaan
        for row in listRow:
            if row[key] != '':
                array.append(float(row[key]))
        array.sort()
        n = len(array)
        if n % 2 == 0:
            median1 = array[n//2]
            median2 = array[n//2 - 1]
            res = (median1 + median2)/2
        else:
            res = array[n//2]
            #thêm median của cột đó vào 1 biến nhớ
        median.append((key, res))
    median = dict(median)
    #cập nhật các giá trị bị thiếu bằng median của của thuộc tính
    for key in listRow[0].keys():
        if key in median.keys():
            for row in listRow:
                if row[key] == '':
                    row[key] = median[key]
    #trả về listRow mới đã được điền đầy đủ các thuộc tính thiếu bằng median và mode
    return listRow
def calculateMode(listRow):#hàm tính mode
    mode = []
    #Xét các cột kiểu categorical bị thiếu dữ liệu
    for key in attributeCategorical(listRow):
        array = []
        #với mỗi cột thì reset lại biến nhớ
        #xét các dòng không bị thiếu dữ liệu để tính mediaan
        for row in listRow:
            if row[key] != '':
                #nếu dòng không rỗng thì thêm nó vào biến nhớ array
                array.append(row[key])
        #sort lại list array
        array.sort()
        L1 = []
        i = 0
        res = []
        while i < len(array):
            #dùng L1 để lưu lại đếm số lần giá trị của dữ liệu trong array
            L1.append(array.count(array[i]))
            i += 1
        # chuyển array và L1 thành dictionary với key là giá trị của array còn values là số lần xuất hiện
        d1 = dict(zip(array, L1))
        for (k, v) in d1.items():
            if v == max(L1):
                #nếu key đó có value lớn nhất thì thêm giá trị đã đề cập đó vào res
                res.append(k)
        if len(res) == 0:
            #nếu cột đó là rỗng, thì giá trị của cột đó là '' không có gì
            mode.append((key, ''))
        else:
            #nếu không thì thêm giá trị của thuộc tính xuất hiện nhiều nhất cùng tên cột đó vào mode
            for str in res:
                mode.append((key, str))
    #chuyển kiểu dữ liệu về dictionary
    mode = dict(mode)
    #cập nhật lại các thuộc tính categorical thiếu dữ liệu theo mode
    for key in listRow[0].keys():
        if key in mode.keys():
            for row in listRow:
                if row[key] == '':
                    row[key] = mode[key]
    #trả về listRow mới đã cập nhật lại các thuộc tính categorical thiếu dữ liệu theo mode
    return listRow