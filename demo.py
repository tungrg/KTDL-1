import csv
listRow=[]
with open('house-prices.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        listRow.append(row)
def caua():
    res=[]
    for key in listRow[0].keys():
        count = 0
        for row in listRow:
            if row[key] == '':
                res.append((key,count))
                count += 1
    res=dict(res)
    return res
caua()
def caub():
    count=0
    for row in listRow:
        for key in listRow[0].keys():
            if row[key] == '':
                count += 1
                break
    return count
caub()
def attributeNumeric():
    num = []
    for key in caua().keys():
        for row in listRow:
            if row[key] != '':
                if row[key].count('.') != 0:
                    num.append(key)
                    break
                else:
                    if row[key].isnumeric():
                        num.append(key)
                        break
    return num
attributeNumeric()
def attributeCategorical():
    attr_str = []
    num = attributeNumeric()
    for key in caua().keys():
        if key not in num:
            attr_str.append(key)
    return attr_str
attributeCategorical()
s = attributeNumeric()
mean =[]
sum = 0
count = 0
for row in listRow:
    if row[s[0]] != '':
        count += 1
        sum += float(row[s[0]])
average = sum / count
average
def calculateMean():
    mean = []
    array= []
    for key in attributeNumeric():
        sum = 0
        count = 0
        for row in listRow:
            if row[key] != '':
                count += 1
                sum += float(row[key])
        average = sum / count
        mean.append((key,average))
    return dict(mean)
calculateMean()
def calculateMedian():
    median=[]
    for key in attributeNumeric():
        array = []
        for row in listRow:
            if row[key] != '':
                array.append(float(row[key]))
        array.sort()
        mid = len(array) // 2
        res = (array[mid] + array[~mid]) / 2
        median.append((key,res))
    return dict(median)
calculateMedian()
def calculateMode():
    mode = []
    for key in attributeCategorical():
        array = []
        for row in listRow:
            if row[key] != '':
                array.append(row[key])
        array.sort()
        L1 = []
        i = 0
        res = []
        while i < len(array):
            L1.append(array.count(array[i]))
            i += 1
        d1 = dict(zip(array, L1))
        for (k,v) in d1.items():
            if v == max(L1):
                res.append(k)
        if len(res) == 0:
            mode.append((key,''))
        else:
            for str in res:
                mode.append((key,str))
    return dict(mode)
calculateMode()
def deleteRow(rate):
    temp_listRow = listRow.copy()
    num_attr = len(listRow[0].keys())
    n = num_attr * rate / 100
    for row in listRow:
        count = 0
        for key in listRow[0].keys():
            if row[key] == '':
                count +=1
            if count > n:
                temp_listRow.remove(row)
                break
    return len(temp_listRow)
deleteRow(10)
def deleteColumn(rate):
    num_attr = len(listRow[0].keys())
    n = num_attr * rate / 100
    temp_listRow = []
    for i in range(len(listRow)):
        b = listRow[i].copy()
        temp_listRow.append(b)
    for key in listRow[0].keys():
        t = 0
        count = 0
        for row in listRow:
            if row[key] == '':
                count +=1
            if count > n:
                print(key)
                temp_listRow[t].pop(key)
                break
        t+=1
    return len(temp_listRow)
deleteColumn(80)