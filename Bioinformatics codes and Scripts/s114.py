import FASTQ
'''import sys
print(sys.path)'''
import os
fileList = os.listdir('/home/ahmed/C4/z-rna-seq/SRR6924568-MB')
fileList.sort()
#print(fileList)
fullPath = []
for i in fileList:
    if i.endswith('.fastq'):
        fullPath.append('/home/ahmed/C4/z-rna-seq/SRR6924568-MB/%s'%(i))
print(fullPath)
FASTQ.qualCont(fileNames=fullPath, quality=30, percentage=95)