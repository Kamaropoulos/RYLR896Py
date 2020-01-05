# import serial

class RYLR896():
    ser = None
    def __init__(self, tty=None, baudrate=None):
        # self.ser = serial.Serial(tty, baudrate, timeout=1)
        # TODO: Set IPR
        pass

    def Test(self):
        pass

    def Reset(self):
        pass

    def Send(self, message, address=None):
        if address is None:
            # Broadcast
            pass
        else:
            # Send to address
            pass

    def Receive(self):
        pass

    def SleepMode(self):
        pass

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

    def __ReadFromLoRa(self):
        pass

    def __SetIPR(self, IPR):
        pass

