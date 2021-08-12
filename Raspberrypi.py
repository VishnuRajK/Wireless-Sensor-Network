import time
import serial
import re
import urllib2
#Setting the serial data
ser = serial.Serial(
        port='/dev/ttyAMA0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)
counter=0
ser.flushInput()
# Providing the details of cloud space used
url1='https://api.thingspeak.com/update?api_key= *ID*=0'
# Reading data from each node 
while 1:
        data_string=ser.readline()
        data_num= re.findall('\d+(?:\.\d+)?',data_string)
 
        NID=data_num[1]
        if NID=="1":
                Temperature1=data_num[2]
        elif NID=="2":
                Temperature2=data_num[2]
        elif NID=="3":
                Temperature3=data_num[2]
        elif NID=="4":
                Temperature4=data_num[2]
        counter=counter+1
        print data_num
        if counter>=4:

#Uploading the data input to corresponding field in the cloud space               
               upload1=urllib2.urlopen(url1+Temperature1+"&field2=0"+Temperature2+"&field3=0"+Temperature3+"&field4=0"+Temperature4)
               upload1.read()
               upload1.close()
               counter=0
