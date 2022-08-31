import Adafruit_DHT as dht
#import sys
from urllib.request import urlopen
from time import sleep
DHT_SENSOR = dht.DHT11
DHT_PIN = 4
#Enter Your API key
myAPI = "XEIU8767B7E5RSS6" 
baseURL = 'https://api.thingspeak.com/update?api_key=%s'%myAPI
#-----------------------------------
def DHT_data():
	humi,temp = dht.read_retry(DHT_SENSOR,DHT_PIN)
	return humi, temp
#------------------------------------
while True:
	humi, temp = DHT_data()
	print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temp, humi))
	if isinstance(humi,float) and isinstance(temp,float):
		humi = '%.2f' % humi
		tem = '%.2f' % temp
	#print(tem,humi)
	#send the data to thingspeak
		conn = urlopen(baseURL+'&field1=%s&field2=%s' % (temp, humi))
		print(conn.read)
	#closing the connection
		conn.close()
	else:
		print('Error')
	sleep(0.5)
