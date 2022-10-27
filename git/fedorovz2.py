def datMonth():
    data2 = openFile()
    size = len(data2)
    data1 = ['03', '12', '2002']
    for i in range(0, size, 1):
        n = data2[i].split('-')[0]
        print(n)
        if int(n) < int(data1[0]):
            data1[0] = n
        n = data2[i].split('-')[1]
        if int(n) < int(data1[1]):
            data[1] = n
        print(data1[0], "-", data1[1])

datMonth()