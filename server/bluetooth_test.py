import bluetooth

serverMACAddress = 'B8:27:EB:4C:24:B8'
port = 3
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))

while True:
	text = str.encode('Funciona')
	s.send(text)
s.close()
