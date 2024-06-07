import time

tI = time.time(); #print(tI)
tT = time.localtime(); #print(tT)
asC = time.asctime(); #print(asC)

strF = time.strftime('%d %A %B %Y %I:%M:%S %p', tT); #print(strF)

strP = time.strptime('18 Thursday May 2023 11:32:21 PM', 
                     '%d %A %B %Y %I:%M:%S %p'); #print(strP)
