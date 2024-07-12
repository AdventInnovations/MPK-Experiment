import serial


class Sensor:
    def __init__(self, port, baudrate, timeout):
        self.ser = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
        self.cmd = ""
        self.output = ""
    
    def setBlue(self, state):
        if state:
            self.ser.write(b"set blue 1 ")
        else:
            self.ser.write(b"set blue 0 ")
    
    def setGreen(self, state):
        if state:
            self.ser.write(b"set green 1 ")
        else:
           self.ser.write(b"set green 0 ")
            
    def setRed(self, state):
        if state:
            self.ser.write(b"set red 1 ")
        else:
           self.ser.write(b"set red 0 ")
            
    def setBlueRGB(self, state):
        if state:
            self.ser.write(b"set rgb_blue 255 ")
        else:
            self.ser.write(b"set rgb_blue 0 ")
    
    def setGreenRGB(self, state):
        if state:
            self.ser.write(b"set rgb_green 255 ")
        else:
            self.ser.write(b"set rgb_green 0 ")
            
    def setRedRGB(self, state):
        if state:
            self.ser.write(b"set rgb_red 255 ")
        else:
            self.ser.write(b"set rgb_red 0 ")
            
    def StartRecordingDiode(self):
        self.ser.write(b"start_diode ")
    
    def StartRecordingTransistor(self):
        self.ser.write(b"start_transistor ")
        
    def stopRecording(self):
        self.ser.write(b"stop ")
        
    def readSerial(self):
        return self.ser.readline().decode()
    
    
    
            
        
