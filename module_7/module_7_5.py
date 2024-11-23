import datetime
import os.path

directory='../'
fullpath = os.path.abspath(directory)



for root,dirs,files in os.walk(fullpath):
    for f in files:
        if f[0]=='.':
            continue
        filepath=root+os.path.sep+f
        stat=os.stat(filepath)
        filetime= datetime.datetime.fromtimestamp(stat.st_mtime)
        filesize= stat.st_size
        parentdir=os.path.basename(os.path.dirname(filepath))
        print(f"{f}, путь: {filepath},  время: {filetime:%d-%m-%Y %H-%M}, размер: {filesize//1000}kб,  Род.дир: {parentdir}|")



#идея для харда -- вывести в консоли в виде дерева как в експлорере))))