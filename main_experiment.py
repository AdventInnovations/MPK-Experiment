from sensor import Sensor
import time
import os


class Experiment:
    def __init__(self):
        
        self.fileName = "test1"
        self.filePath = f"{os.path.dirname(__file__)}/{self.fileName}"
        self.currentTime = 0.0
        self.startTime = 0.0

        self.ser = Sensor("/dev/ttyACM0", 115200, 1)


    def recordLight(self, light, file, timer, rate):
        light(True)
        with open(f"{os.path.dirname(__file__)}/{file}", "w") as f:
            self.startTime = time.time()
            self.ser.StartRecording()
            while (self.currentTime - self.startTime) < timer:            
                f.write(self.ser.readSerial())
                time.sleep(rate)
                self.currentTime = time.time()
        self.ser.stopRecording()
        light(False)
        
    def startExperiment(self, timeBetween, rate):
        
        self.recordLight(self.ser.setBlue, "blue.txt", timeBetween, rate)
        self.recordLight(self.ser.setGreen, "green.txt", timeBetween, rate)
        self.recordLight(self.ser.setRed, "red.txt", timeBetween, rate)
        self.recordLight(self.ser.setBlueRGB, "rgb_blue.txt", timeBetween, rate)
        self.recordLight(self.ser.setGreenRGB, "rgb_green.txt", timeBetween, rate)
        self.recordLight(self.ser.setRedRGB, "rgb_red.txt", timeBetween, rate)
                

if __name__ == "__main__":
    ex = Experiment()
    print("Start Experiment")
    ex.startExperiment(10, 1)
    print("Stop Experiment")

