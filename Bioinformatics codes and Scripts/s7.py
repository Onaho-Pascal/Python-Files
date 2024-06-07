# Receive a number from the user
#vaR = input('Enter a number: '); print(type(vaR))

# Read a nuber from a file
#oF = open('exampleFile.txt', 'r'); rF = oF.read(); print(type(rF))

# integer to float 
iTf = float(1); print(iTf, type(iTf))
# float to integer
fTi = int(23.5); print(fTi, type(fTi))
# complex
comP = complex(iTf, fTi); print(comP, type(comP))
print(comP.real, comP.imag)

# integer or float to string

iTs = str(12); print(iTs, type(iTs))
fTs = str(23.6); print(fTs, type(fTs))
sTi = int('1'); print(sTi, type(sTi))
sTf = float('1.5'); print(sTf, type(sTf))
