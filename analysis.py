import os
import matplotlib.pyplot as plt
import numpy as np


def getData(name):
    data = {"diode": {}, "transistor": {}}
    
    
    for i in os.listdir(f"{os.path.dirname(__file__)}/recordedData/{name}"):
        data["transistor"][i] = {}
        data["diode"][i] = {}
        for j in os.listdir(f"{os.path.dirname(__file__)}/recordedData/{name}/{i}/diode/"):
            with open(f"{os.path.dirname(__file__)}/recordedData/{name}/{i}/diode/{j}") as f:
                data["diode"][i][j[0:-4]] = list(int(i.replace("\n", "")) for i in f.readlines() if i.replace("\n", "") != '' and int(i.replace('\n', '')) < 200)
        for j in os.listdir(f"{os.path.dirname(__file__)}/recordedData/{name}/{i}/transistor/"):
            with open(f"{os.path.dirname(__file__)}/recordedData/{name}/{i}/transistor/{j}") as f:
                data["transistor"][i][j[0:-4]] = list(int(i.replace("\n", "")) for i in f.readlines() if i.replace("\n", "") != '' and int(i.replace('\n', '')) < 200)
        

    return [name, data] 


def plotTogether(d1, d2, sensor, trial, color):
    
    
    X0 = [i for i in range(0, len(d1[1][sensor][trial][color]))]
    X1 = [i for i in range(0, len(d2[1][sensor][trial][color]))]
    
    Y0 = [i for i in d1[1][sensor][trial][color]]
    Y1 = [i for i in d2[1][sensor][trial][color]]
    
    return X0, X1, Y0, Y1
    # plt.plot(X0, Y0, label=f"{d1[0]}:{color}")
    # plt.plot(X1, Y1, label=f"{d2[0]}:{color}")
    # plt.legend()
    # plt.show() 
    
def plotAll(d1, d2, sensor, trial):
    
    def createPlot(axs, color, axis):
        
        axs[axis[0], axis[1]].plot(X0, Y0, label=f"{d1[0]}")
        axs[axis[0], axis[1]].plot(X1, Y1, label=f"{d2[0]}")
        axs[axis[0], axis[1]].set_title(f"{trial} : {color}")
        axs[axis[0], axis[1]].legend()
        
        return axs
        
    fig, axs = plt.subplots(2,3)
    X0, X1, Y0, Y1 = plotTogether(d1, d2, sensor, trial, "red")
    createPlot(axs, "red", [0,0])
    X0, X1, Y0, Y1 = plotTogether(d1, d2, sensor, trial, "blue")
    createPlot(axs, "blue", [0,1])
    X0, X1, Y0, Y1 = plotTogether(d1, d2, sensor, trial, "green")
    createPlot(axs, "green", [0,2])
    X0, X1, Y0, Y1 = plotTogether(d1, d2, sensor, trial, "rgb_red")
    createPlot(axs, "rgb_red", [1,0])
    X0, X1, Y0, Y1 = plotTogether(d1, d2, sensor, trial, "rgb_blue")
    createPlot(axs, "rgb_blue", [1,1])
    X0, X1, Y0, Y1 = plotTogether(d1, d2, sensor, trial, "rgb_green")
    createPlot(axs, "rgb_green", [1,2])
    plt.show()


if __name__ == "__main__":
    
    base = getData("base")
    
    
    plotAll(base, getData("N_2Ml"), "diode", "trial1")
    