import math

print("Running SinWaveGenerator")

pi = math.pi


def exampleUseOfSin():
    # Remember 1 full cycle is 360 degrees which is 2*Pi.
    # ie. sin(0) = sin(2*Pi)
    # After 2*Pi the function just repeats itself

    print(math.sin(0))
    print(math.sin(1 / 4 * 2 * pi))
    print(math.sin(1 / 2 * 2 * pi))
    print(math.sin(3 / 4 * 2 * pi))


numberOfPrices = 100
numberOfPricesPerSinWave = 20
AveragePrice = 100  # In US Dollars
AmplitudePrice = 1  # In US Dollars

sineWaveFile = open("SineWavePriceData.txt", 'w')


def generateSineWave():
    for t in range(0, numberOfPrices):
        price = "{:.2f}".format(AmplitudePrice * math.sin(t / numberOfPricesPerSinWave * 2 * pi) + AveragePrice)
        # print("Time: ",t, "Price: ",price )
        print(price)
        sineWaveFile.write(price)
        sineWaveFile.write("\n")
    sineWaveFile.close()


# exampleUseOfSin()
generateSineWave()
