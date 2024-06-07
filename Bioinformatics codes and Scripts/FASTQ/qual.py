def qualCont(fileNames, quality, percentage):
    locK = 0
    quality = quality + 33
    for fileName in fileNames:
        counT = 0
        tCount = 0
        hqIDs = []
        with open(fileName, 'r') as openFile:
            for indLine, linE in enumerate(openFile):
                '''if indLine == 100:
                    break
                else:
                    pass
                    #print(linE.replace('\n', ''))'''
                if linE.startswith('@'):
                    fastqID = '%s\n'%(linE.split(' ')[0][1:])
                if locK == 1:
                    tCount += 1
                    #print(indLine+1, linE.replace('\n', ''))
                    qualNuc = []
                    for nuC in linE.replace('\n', ''):
                        #print(nuC, ord(nuC), ord(nuC)-33)
                        if ord(nuC) >= quality:
                            qualNuc.append(nuC)
                    #print(qualNuc, len(qualNuc), len(linE))
                    peR = (len(qualNuc)/len(linE.replace('\n', '')))*100
                    #print(peR)
                    if peR >= percentage:
                        counT += 1
                        hqIDs.append(fastqID)
                if linE.startswith('+'):
                    locK = 1
                else:
                    locK = 0
        #return tCount, counT
        with open('{filE}-qual.txt'.format(filE=openFile.name), 'w') as writE:
            writE.write('Total Number of Reads: {total}\nReads with {percent}% High-quality Bases: {HQ}'.format(total=tCount, HQ=counT, percent=percentage))
        with open('{filE}-HQ_IDS.txt'.format(filE=openFile.name), 'w') as writE2:
            writE2.writelines(hqIDs)

if __name__ == '__main__':
    fileNames = []
    qualCont(fileNames, 20, 80)