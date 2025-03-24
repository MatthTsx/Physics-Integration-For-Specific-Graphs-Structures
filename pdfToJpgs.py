from pdf2image import convert_from_path
import os

root = os.getcwd() + "/PdfsForConversion/"
print(root)

fileName = input("Pdf's File name: ")
pages = convert_from_path(root + fileName + ".pdf")


resultDir = root + fileName + "_JPGS/"
if not os.path.exists(resultDir):
    os.makedirs(resultDir)

for i in range(len(pages)):
    pages[i].save(resultDir + fileName + str(i) + ".jpg", 'JPEG')
    print(i)