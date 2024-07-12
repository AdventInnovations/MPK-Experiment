from sensor import Sensor
import time
import os
import matplotlib.pyplot as plt



class Experiment:
    def __init__(self):
        
        self.fileName = "test1"
        self.filePath = f"{os.path.dirname(__file__)}/{self.fileName}"
        self.currentTime = 0.0
        self.startTime = 0.0

   
    def StoreData(self, name):
        files = os.listdir(f"{os.path.dirname(__file__)}/data/diode")
        if len(files) != 0:
            if not os.path.exists(f"{os.path.dirname(__file__)}/recordedData/{name}"):
                os.system(f"mkdir -p {os.path.dirname(__file__)}/recordedData/{name}")
            folder = os.listdir(f"{os.path.dirname(__file__)}/recordedData/{name}")
            os.system(f"mkdir -p {os.path.dirname(__file__)}/recordedData/{name}/trial{len(folder)}/diode")
            time.sleep(1)
            os.system(f"cp -r {os.path.dirname(__file__)}/data/diode/* {os.path.dirname(__file__)}/recordedData/{name}/trial{len(folder)}/diode")
            os.system(f"mkdir -p {os.path.dirname(__file__)}/recordedData/{name}/trial{len(folder)}/transistor")
            time.sleep(1)
            os.system(f"cp -r {os.path.dirname(__file__)}/data/transistor/* {os.path.dirname(__file__)}/recordedData/{name}/trial{len(folder)}/transistor")
        
   
    def recordLight(self, light, file, timer, rate, sensor):
        if sensor == "diode":
            
            light(True)
            with open(f"{os.path.dirname(__file__)}/data/diode/{file}", "w") as f:
                self.startTime = time.time()
                self.ser.StartRecordingDiode()
                while (self.currentTime - self.startTime) < timer:            
                    f.write(self.ser.readSerial())
                    time.sleep(rate)
                    self.currentTime = time.time()
            self.ser.stopRecording()
            light(False)
        elif sensor == "transistor":
             
            light(True)
            with open(f"{os.path.dirname(__file__)}/data/transistor/{file}", "w") as f:
                self.startTime = time.time()
                self.ser.StartRecordingTransistor()
                while (self.currentTime - self.startTime) < timer:            
                    f.write(self.ser.readSerial())
                    time.sleep(rate)
                    self.currentTime = time.time()
            self.ser.stopRecording()
            light(False)
        
    def startExperiment(self, timeBetween, rate, name):
        
        self.ser = Sensor("/dev/ttyACM0", 115200, 1)
        self.ser.setAllOff()
        time.sleep(1)
        
        self.recordLight(self.ser.setBlue, "blue.txt", timeBetween, rate, "diode")
        self.recordLight(self.ser.setGreen, "green.txt", timeBetween, rate, "diode")
        self.recordLight(self.ser.setRed, "red.txt", timeBetween, rate, "diode")
        self.recordLight(self.ser.setBlueRGB, "rgb_blue.txt", timeBetween, rate, "diode")
        self.recordLight(self.ser.setGreenRGB, "rgb_green.txt", timeBetween, rate, "diode")
        self.recordLight(self.ser.setRedRGB, "rgb_red.txt", timeBetween, rate, "diode")
        
        self.recordLight(self.ser.setBlue, "blue.txt", timeBetween, rate, "transistor")
        self.recordLight(self.ser.setGreen, "green.txt", timeBetween, rate, "transistor")
        self.recordLight(self.ser.setRed, "red.txt", timeBetween, rate, "transistor")
        self.recordLight(self.ser.setBlueRGB, "rgb_blue.txt", timeBetween, rate, "transistor")
        self.recordLight(self.ser.setGreenRGB, "rgb_green.txt", timeBetween, rate, "transistor")
        self.recordLight(self.ser.setRedRGB, "rgb_red.txt", timeBetween, rate, "transistor")
        
        self.StoreData(name)
        
    def plotData(self, sensor):
        data = {}
       
        files = os.listdir(f"{os.path.dirname(__file__)}/data/{sensor}")
        for i in files:
            with open(f"{os.path.dirname(__file__)}/data/{sensor}/{i}", "r") as f:
               
                data[i] = f.read().replace('\n', " ").split(" ")[0:-1]
        
        X = []
        Y = []
        fileCount = 0
        plt.figure()
        for i in data.keys():
            point = 0
           
            for j in data[i]:
                if j != '':
                    X.append(point)
                    Y.append(int(j))
                    point += 1
            plt.plot(X,Y, label=f"{files[fileCount][0:-4]}")
            plt.title(sensor)
            X = []
            Y = []
            fileCount += 1
        
        plt.legend()
        
        

if __name__ == "__main__":
    ex = Experiment()
    for i in range(3):
        print("Start Experiment")
        ex.startExperiment(20, 0.1, "P_8Ml")
        print("Stop Experiment")
   
    # ex.plotData("diode")
    # ex.plotData("transistor")
    
    # plt.show()
 
