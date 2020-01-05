import serial

class RYLR896():
    ser = None
    def __init__(self, tty=None, baudrate=None):
        self.ser = serial.Serial(tty, baudrate)
        self.__SetIPR(baudrate)
        pass

    def Test(self):
        self.__WriteToLoRa("AT")
        response = self.__ReadFromLoRa()
        if response == "+OK":
            return True
        else:
            return False

    def Reset(self):
        self.__WriteToLoRa("AT+RESET")
        response = self.__ReadBytesFromLoRa()
        if response == b'+RESET\r\xca\x00\xe0+READY\r\n':
            return True
        else:
            return False

    def Send(self, message, address=None):
        if address is None:
            self.__WriteToLoRa("AT+SEND=0,"+str(len(message))+","+message)
            response = self.__ReadFromLoRa()
            if response == "+OK":
                return True
            else:
                return False
        else:
            self.__WriteToLoRa("AT+SEND="+str(address)+","+str(len(message))+","+message)
            response = self.__ReadFromLoRa()
            if response == "+OK":
                return True
            else:
                return False

    def Receive(self):
        pass

    def SleepMode(self):
        self.__WriteToLoRa("AT+MODE=1")
        response = self.__ReadFromLoRa()
        if response == "+OK":
            return True
        else:
            return False

    def NormalMode(self):
        pass

    def SetRFParams(self, spreadingFactor, bandwidth, codingRate, programmedPreamble):
        pass

    def SetRFParamsLessThan3KM(self):
        pass

    def SetRFParamsMoreThan3KM(self):
        pass

    def SetAddress(self, address):
        pass

    def GetAddress(self):
        pass

    def SetNetworkID(self, networkID):
        pass

    def __WriteToLoRa(self, message):
        self.ser.write(str(message+'\r\n').encode())

    def __ReadBytesFromLoRa(self):
        try:
            responseBytes = self.ser.readline()
            return(responseBytes)
        except Exception as e:
            print(e)

    def __ReadFromLoRa(self):
        try:
            response = self.ser.readline().decode('utf-8')[:-2]
            return(response)
        except Exception as e:
            print(e)

    def __SetIPR(self, IPR):
        self.__WriteToLoRa("AT+IPR="+str(IPR))
        response = self.__ReadFromLoRa()
        if response == "+OK":
            return True
        else:
            return False

