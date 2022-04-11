# Ver. 0.3 11/4/22
#
# Python 3 program to solve UCDdle
# from script file, answer can be retrieved in base64 encoded format
# steps:
#	1. Download/ read script from website (running into error when reading Error: 403 Forbidden)
#	2. Read answer in base64 (issue being encoded form can be n in length)
#	3. Decode base64
#	4. Return ans



import base64, urllib.request, urllib


lines = []

url = "https://ucddle.tk/script.js"

with open("script.txt", "r") as f:
	data = f.readlines(330)




dataExtract = data[7]


#print(dataExtract[26]) # index of dataExtract[26] = "

with open("encodedAns.txt", "w") as f:
	
	i = 27
	while dataExtract[i] != chr(34):
		f.write(dataExtract[i])
		i += 1

with open("encodedAns.txt", "r") as f:
	encoded = f.read()
	decoded = base64.b64decode(encoded)
	print(decoded)

