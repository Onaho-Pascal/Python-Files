def fastq2fasta(fileNames):
    locK = 0
    for fileName in fileNames:
        lockForFile = 0
        with open(fileName, 'r') as openFile:
            for indLine, linE in enumerate(openFile):
                reC = ''
                '''if indLine == 12:
                    break
                else:
                    pass
                    #print(linE.replace('\n', ''))'''
                if locK == 1:
                    reC += linE#.replace('\n', '')
                if linE.startswith('@'):
                    reC += linE.replace('@', '>')
                    locK = 1
                else:
                    locK = 0
                #print(reC)
                if reC:
                    if lockForFile == 0:
                        with open('{filE}-fastq2fasta.fasta'.format(filE=openFile.name), 'w') as writE:
                            writE.write(reC)
                            lockForFile = 1
                    else:
                        with open('{filE}-fastq2fasta.fasta'.format(filE=openFile.name), 'a') as writE:
                            writE.write(reC)

if __name__ == '__main__':
    fileNames = []
    fastq2fasta(fileNames)