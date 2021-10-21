import FileReader

print("Running FileReaderExample.py")

stockPriceArray = FileReader.fileRead("../tools/SineWavePriceData.txt")

for stockPrice in stockPriceArray:
    print(stockPrice)

