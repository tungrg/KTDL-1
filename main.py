import sys
import csv
import Cau01
import Cau02
import Cau03
import Cau04
import Cau05
import Cau06
import Cau07
import Cau08
#doc file csv
def readFile(inputFile):
    #tạo biến để lưu dữ liệu đọc được
    listRow = []
    
    with open(inputFile) as csvfile:
        #Hàm csv.DictReader đọc file csv rồi lưu vào 1 biến, biến này mang kiểu dữ liệu dictionary
        reader = csv.DictReader(csvfile)
        for row in reader:
            #chuyển sang lưu dạng list
            listRow.append(row)
    return listRow
def writeFile(outputFile,listRow):
    with open(outputFile, 'w', newline='') as csvfile:
        #ghi file csv theo kiểu dữ liệu của dictionary
        writer = csv.DictWriter(csvfile, fieldnames = listRow[0].keys())
        #ghi tên các cột trước
        writer.writeheader()
        for row in listRow:
            writer.writerow(row)
if __name__ == '__main__':
    input_file_name = str(sys.argv[1])
    listRow = readFile(input_file_name)
    if str(sys.argv[2]) == "cau01":
        res = Cau01.cau01(listRow)
        for x, y in res.items():
            print(x, '-', y)
    elif str(sys.argv[2]) == "cau02":
        Cau02.cau02(listRow)
    elif str(sys.argv[2]) == "cau03":
        if str(sys.argv[3]) == "mean":
            temp = Cau03.calculateMean(listRow)
            writeFile(str(sys.argv[4]), temp)
        elif str(sys.argv[3]) == "median":
                temp = Cau03.calculateMedian(listRow)
                writeFile(str(sys.argv[4]), temp)
    elif str(sys.argv[2]) == "cau04":
        temp = Cau04.deleteRow(listRow, str(sys.argv[3]))
        writeFile(str(sys.argv[4]), temp)
    elif str(sys.argv[2]) == "cau05":
        temp = Cau05.deleteColumn(listRow, str(sys.argv[3]))
        writeFile(str(sys.argv[4]), temp)
    elif str(sys.argv[2]) == "cau06":
        temp = Cau06.DeleteDuplicateRows(listRow)
        writeFile(str(sys.argv[3]), temp)
    elif str(sys.argv[2]) == "cau07":
        if str(sys.argv[3]) == "Min-Max":
            temp = Cau07.setAttributeByMin_MaxMethod(listRow, sys.argv[4])
            if temp == 0:
                print("This row cann't standardize!.")
            else:
                writeFile(str(sys.argv[5]), temp)
        elif str(sys.argv[3]) == "Z-Score":
            temp = Cau07.setAttributeByZ_ScoreMethod(listRow, sys.argv[4])
            if temp == 0:
                print("This row cann't standardize!.")
            else:
                writeFile(str(sys.argv[5]), temp)
    elif str(sys.argv[2]) == "cau08":
        temp = Cau08.addColumn(listRow, sys.argv[3])
        if temp == 0:
            print("Wrong input expression.")
        else:
            writeFile(str(sys.argv[4]), temp)