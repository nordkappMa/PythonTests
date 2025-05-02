import os
import pathlib
path1 = r"E:\BaiduNetdiskDownload"


#print(os.path.exists(path1))
#print(os.listdir(path1))


def list_folders(path):
    var_path=pathlib.Path(path)
    folders=[]
    for dirName in var_path.iterdir():
        if os.path.isdir(dirName):
            if not os.path.basename(dirName).startswith("."):
                folders.append(dirName)
                list_folders(dirName)
    return folders

def list_folders2(path):
    folders=[]
    dirs=os.listdir(path) 
    for each in dirs:
        if not str(each).startswith("."):
            eachPath=os.path.join(path,each)
            if os.path.isdir(eachPath):
                list_folders2(eachPath)
            else:
                folders.append(eachPath)
    return folders


 

l1=list_folders2(path1)
print(l1)
# for dirPath, dirNames,fileNames in os.walk(path1):
#     print(f"当前目录:{dirPath}")
#     print(f"子目录:")
#     for dirName in dirNames:
#         if not dirName.startswith("."):
#             print(f" {dirName}")
#     print(f"文件:")
#     for fileName in fileNames:
#         print(f" {fileName}")
#     print("-"*20)

