import os

def getFullPath(file):
    put = os.getcwd()
    path = str(put) + '\\' + file
    return path

file =img/good.jpg
p1 = getFullPath("img\error.jpg")
print(p1)
