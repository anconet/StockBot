print("FileReader")

def exampleWritingAndReadingAFile():
    testFile = open('TestData.txt', 'w')

    testFile.write("100\n")
    testFile.write("200\n")
    testFile.write("300\n")
    testFile.close()

    testFile = open('TestData.txt')

    testFileLine = testFile.readline()
    #print(testFileLine)

    stockValuesArray = []

    while testFileLine != '':
        stockValuesArray.append(testFileLine)
        print(testFileLine,end='')
        testFileLine = testFile.readline()

    print("-----------")

    for x in stockValuesArray:
        print(x)

def fileRead(fileName):
    stockPriceFile = open(fileName)
    stockPriceFileLine = stockPriceFile.readline()
    stockPriceArray = []

    while stockPriceFileLine != '':
        stockPriceArray.append(stockPriceFileLine.replace("\n",""))
        stockPriceFileLine = stockPriceFile.readline()

    return stockPriceArray

#exampleWritingAndReadingAFile()
