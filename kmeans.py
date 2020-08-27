import random
import matplotlib.pyplot as plt
import math


class Means:

    def __init__(self, x_Means, y_Means, meansColor):
        self.x_means = x_Means
        self.y_means = y_Means
        self.meansColor = meansColor


# GET- the x value of the mean
def get_xMeans(self):
    return self.x_means


# GET- the y value of the mean
def get_yMeans(self):
    return self.y_means

def get_meansColor(self):
    return self.meansColor

def set_XMeans(self, x):
    self.x_means = x


def set_Ymeans(self, y):
    self.y_means = y


class Datenpunkt:

    def __init__(self, x, y, datenpunkt_color):
        self.x = x
        self.y = y
        self.datenpunkt_color = datenpunkt_color


def get_y(self):
    return self.y


def get_x(self):
    return self.x


def get_datenpunkt_Color(self):
    return self.datenpunkt_color


def set_DatenPunktColor(self, color):
    self.datenpunkt_color = color


def calculateEukDist(datapoint_x, datapoint_y, means_x, means_y):

    euklidianDistance = math.sqrt((datapoint_x - means_x)**2 + (datapoint_y - means_y)**2)
    return euklidianDistance

####### Boilerplate Code #######

liste1 = []
liste2 = []

for i in range(25):
    x = random.randrange(0, 15)
    y = random.randrange(0, 15)
    temp = Datenpunkt(x, y, "Null")
    liste1.append(temp)

for i in range(25):
    x = random.randrange(25, 35)
    y = random.randrange(25, 35)
    temp = Datenpunkt(x, y, "Null")
    liste2.append(temp)

listOfDatapoints = liste1 + liste2

# Visualizing
output_Liste_X_Values = []
output_Liste_Y_Values = []

for i in range(25):
    output_Liste_X_Values.append(get_x(listOfDatapoints[i]))
    output_Liste_Y_Values.append(get_y(listOfDatapoints[i]))

output_Liste_X_Values1 = []
output_Liste_Y_Values1 = []


for i in range(25, 50):
    output_Liste_X_Values1.append(get_x(listOfDatapoints[i]))
    output_Liste_Y_Values1.append(get_y(listOfDatapoints[i]))

plt.scatter(output_Liste_X_Values, output_Liste_Y_Values, color='k')
plt.scatter(output_Liste_X_Values1, output_Liste_Y_Values1, color='k')
plt.show()



####### 1. Initialize Means #######

listOfMeans = []

FirstMean = Means(random.randrange(0, 15), random.randrange(0, 15), "r")
SecondMean = Means(random.randrange(25, 35), random.randrange(25, 35), "b")

listOfMeans.append(FirstMean)
listOfMeans.append(SecondMean)

####### 2. Calculate Distance #######


def calculatelocalMin():
    aggregatedTDM = 0
    for i in range(0, len(listOfDatapoints)):
        DistOfFirstMean = calculateEukDist(get_x(listOfDatapoints[i]), get_y(listOfDatapoints[i]), get_xMeans(listOfMeans[0]), get_yMeans(listOfMeans[0]))
        DistOfSecondMean = calculateEukDist(get_x(listOfDatapoints[i]), get_y(listOfDatapoints[i]), get_xMeans(listOfMeans[1]), get_yMeans(listOfMeans[1]))
        if DistOfFirstMean < DistOfSecondMean:
            aggregatedTDM = aggregatedTDM + DistOfFirstMean
        else:
            aggregatedTDM = aggregatedTDM + DistOfSecondMean
    return aggregatedTDM


def assignBelonging():
    for i in range(0, len(listOfDatapoints)):
        red = "r"
        blue = "b"
        DistOfFirstMean = calculateEukDist(get_x(listOfDatapoints[i]), get_y(listOfDatapoints[i]), get_xMeans(listOfMeans[0]), get_yMeans(listOfMeans[0]))
        DistOfSecondMean = calculateEukDist(get_x(listOfDatapoints[i]), get_y(listOfDatapoints[i]), get_xMeans(listOfMeans[1]), get_yMeans(listOfMeans[1]))
        if DistOfFirstMean < DistOfSecondMean:
            set_DatenPunktColor(listOfDatapoints[i], red)
        else:
            set_DatenPunktColor(listOfDatapoints[i], blue)


def update(Mean):
    color = get_meansColor(Mean)
    sumX = 0
    sumY = 0
    counter = 0
    for i in range(0, len(listOfDatapoints)):
        temp = get_datenpunkt_Color(listOfDatapoints[i])
        if temp == color:
            sumX = sumX + get_x(listOfDatapoints[i])
            sumY = sumY + get_y(listOfDatapoints[i])
            counter = counter + 1
    updatedX = sumX/counter
    updatedY = sumY/counter
    set_XMeans(Mean, updatedX)
    set_Ymeans(Mean, updatedY)


# Visualizes the results as a scatter plot
def showFinalResult():
    redCluster = []
    blueCluster = []
    for i in range(0, len(listOfDatapoints)):
        color = get_datenpunkt_Color(listOfDatapoints[i])
        if color == "r":
            redCluster.append(listOfDatapoints[i])
        else:
            blueCluster.append(listOfDatapoints[i])
    redClusterX = []
    redClusterY = []
    blueClusterX = []
    blueClusterY = []
    for i in range(0, len(redCluster)):
        redClusterX.append(get_x(redCluster[i]))
        redClusterY.append(get_y(redCluster[i]))
    for i in range(0, len(blueCluster)):
        blueClusterX.append(get_x(blueCluster[i]))
        blueClusterY.append(get_y(blueCluster[i]))
    plt.scatter(redClusterX, redClusterY, color='r')
    plt.scatter(blueClusterX, blueClusterY, color='b')
    firstMeanX = []
    firstMeanY = []
    secondMeanX = []
    secondMeanY = []
    firstMeanX.append(get_xMeans(listOfMeans[0]))
    firstMeanY.append(get_xMeans(listOfMeans[0]))
    secondMeanX.append(get_xMeans(listOfMeans[1]))
    secondMeanY.append(get_yMeans(listOfMeans[1]))
    plt.scatter(firstMeanX, firstMeanY, color='r', marker="^")
    plt.scatter(secondMeanX, secondMeanY, color='b', marker="s")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Theory of Machine Learning -- Kmeans-Example')
    plt.show()

# Main-Function
prevTDM = 0
while True:
    assignBelonging()
    currentTDM = calculatelocalMin()
    print("currentTDM: " + str(currentTDM) + " prevDTM: " + str(prevTDM))
    if currentTDM < prevTDM:
        showFinalResult()
        break
    prevTDM = currentTDM
    update(listOfMeans[0])
    update(listOfMeans[1])