import os
import sys
from docx2pdf import convert
import win32console

results = []
resultsBluePrint = []

filePath = __file__.replace(os.path.basename(sys.argv[0]),'')
results += [each for each in os.listdir(filePath) if each.endswith('.docx')]

for file in results:
    
    new_filename = file.replace('docx','pdf')
    convert(filePath+'/'+file, filePath+'/'+new_filename)
    os.replace(filePath+'/'+new_filename, filePath+'/AutoPDF/'+new_filename)