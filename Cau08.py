import Cau03
import Cau07


def XuLyChuoi(listRow, chuoi):  # ham xu ly chuoi bieu thuc nhap vao
    # tach chuỗi biểu thức thành list, với mỗi biến và 1 phép toán là 1 phần tử của list
    temp = ['+', '-', '*', '/']
    a = []
    b = ''
    count = 0
    # tach chuoi thanh mang cac thuoc tinh va dau rieng biet
    for i in chuoi:
        if i not in temp:
            b = b + i
        else:
            a.append(b)
            a.append(i)
            b = ''
        count += 1
        if count == len(chuoi):
            a.append(b)

    # kiem tra cac thuoc tinh co ton tai trong file  house-prices.csv va cac thuoc tinh co phai so khongg
    x = Cau07.allNumeric(listRow)
    for key in a:
        if key not in temp:
            if key not in x:
                return 0
    return a


def addColumn(listRow, chuoi):
    # tao mang temp_listRow sao chep du lieu tu listRow
    temp_listRow = []
    for i in range(len(listRow)):
        b = listRow[i].copy()
        temp_listRow.append(b)
    # xử lý chuỗi, lưu vào list x
    x = XuLyChuoi(listRow, chuoi)
    temp = []
    count = 0
    if x == 0:
        return 0
    else:
        # xét từng dòng
        for row in temp_listRow:
            sum = []
            check = 0
            # ham anh xa cac thuoc tinh trong 1 dong lieu thanh cac gia tri tuong ung
            for i in range(len(x)):
                if x[i] == '+' or x[i] == '-' or x[i] == '*' or x[i] == '/':
                    sum.append(x[i])
                else:
                    # kiểm tra giá trị tại cột đó có rỗng hay không, nếu có thì kết quả bên cột mới là rỗng
                    if row[x[i]] == '':
                        check = 1
                        temp_listRow[count][chuoi] = ''
                        break
                    else:
                        sum.append(row[x[i]])
            # nếu ở tất cả các cột đều có giá trị thì tính giá trị cho cột mới
            if check == 0:
                # ham tinh toan gia tri cua bieu thuc so hoc
                t = eval(''.join(sum))
                # them thuoc tinh vao trong listRow
                temp_listRow[count][chuoi] = t
            count += 1
        # trả về list tập dữ liệu mới 1 cột đã thêm vào
        return temp_listRow
