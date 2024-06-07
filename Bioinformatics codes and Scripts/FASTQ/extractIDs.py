def extIDs(fileName, iDs):
    locK = 0
    locK2 = 0
    lockForFile = 0
    with open(fileName, 'r') as openFile:
        reC = ''
        for indLine, linE in enumerate(openFile):
            '''if indLine == 12:
                break
            else:
                pass
                #print(linE.replace('\n', ''))'''
            if linE.startswith('@'):
                locK2 = 0
                fastqID = linE.split(' ')[0][1:]
                if fastqID in iDs:
                    locK = 1
                else:
                    locK = 0
            if locK == 1:
                locK2 += 1
                reC += linE
            if locK2 == 4:
                if lockForFile == 0:
                    with open('{filE}-extractIDs.fastq'.format(filE=openFile.name), 'w') as writE:
                        writE.write(reC)
                        lockForFile = 1
                else:
                    with open('{filE}-extractIDs.fastq'.format(filE=openFile.name), 'a') as writE:
                        writE.write(reC)
                reC = ''

if __name__ == '__main__':
    fileName = ''
    iDsList = []
    extIDs(fileName, iDsList)