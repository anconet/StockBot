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
    while testFileLine != '':
        print(testFileLine,end='')
        testFileLine = testFile.readline()

exampleWritingAndReadingAFile()