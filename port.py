import serial
import time
import threading
import binascii
class SerialPort:
    message = ''
    def __init__(self, port, buand):
        super(SerialPort, self).__init__()
        self.port = serial.Serial(port, buand)
        self.port.close()
        if not self.port.isOpen():
            self.port.open()
    def port_open(self):
        if not self.port.isOpen():
            self.port.open()    #打开串口
            if self.port.isOpen():
                return 0        #成功打开
            else :
                return -1       #打开失败
        else :
           return 1             #已经打开
    def port_close(self):
        self.port.close()
        if not self.port.isOpen():
            return 0            #关闭成功
        else:
            return -1               #关闭失败
    def send_data(self):
        data = input("输入要发送的数据")
        self.port.write(binascii.a2b_hex(data.strip()))    #发送数据
        #self.port.write(data.strip().decode('hex'))
    def read_data(self):          #接收数据
        while True:
            #print(1)    
            #self.message = self.port.read()  #接收数据
            #print(self.port.read().decode('utf-8'))
            #print(str(binascii.b2a_hex(self.message)))
            #self.message =binascii.b2a_hex(self.message)
            #hex = self.message.encode('utf-8')
            #str_bin = binascii.unhexlify(hex)
            #print(str_bin.decode('utf-8'))
            n = self.port.inWaiting()#获取接收到的数据长度
            if n: 
              #读取数据并将数据存入data
             data = self.port.read(n)
             #输出接收到的数据
             print(data.hex())
             data = data.hex()
             return data
             #data = data[0,2]+" "+data[3,5]+" "+data[5,7]+" "+data[8,10]+" "+data[11,13]+" "
             #显示data的类型，便于如果出错时检查错误
             #print(type(data))
 
serialPort = "COM5"  # 串口
baudRate = 9600  # 波特率
 
if __name__ == '__main__':
    mSerial = SerialPort(serialPort, baudRate)
    t1 = threading.Thread(target=mSerial.read_data)
    t1.start()
    while True:
      time.sleep(1)
      mSerial.send_data()
        