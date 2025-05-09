import os
import re
import  sys

def checkEachDir(dirPathF,eachDir):
    fileList=os.listdir(dirPathF)
    for eachFile in fileList:
        eachFilePath=os.path.join(dirPathF, eachFile)
        if os.path.isfile(eachFilePath):
            readEachFile(eachFilePath, eachDir)

def readEachFile(filePathF, eachDir):
    target_list=[]
    fileName=os.path.basename(filePathF)
    f = open(filePathF, "r", encoding="utf-8")
    contentList = f.readlines()
    f.close()
    for each in contentList:
        eachContentList=each.split(",")
        if len(eachContentList) == 4 or len(eachContentList) == 5:
            if not eachContentList[2] in exception_list:
                if len(eachContentList) == 4:
                    if eachContentList[3].startswith("start"):
                        target_list.append(",".join(eachContentList))
                else:
                    if eachContentList[3].startswith("start"):
                        target_list.append(",".join(eachContentList))
    writeFile(fileName, target_list, eachDir)



def writeFile(fileName, targetList, eachDir):
    i = 0
    while i < len(targetList):
        targetList[i] = eachDir + "," + fileName + "," + targetList[i]
        i = i+1
    filePath = r"D:\result.txt"
    f = open(filePath, "a", encoding="utf-8")
    f.writelines(targetList)
    f.close()

if __name__ == '__main__':
    exception_list = ["GS_CMD_FILE_CHECK.bash", "GS_CMD_FILE_DELETE.bash", "GS_CMD_TXT.bash", "GS_CMD_MSGOUT.bash"]
    basePath = os.path.dirname(os.path.abspath(__file__))
    dirList = os.listdir("gdc_log")
    for eachDir in dirList:
        eachDirPath = os.path.join(basePath, "gdc_log", eachDir)
        print(eachDirPath)
        if os.path.isdir(eachDirPath):
            checkEachDir(eachDirPath, eachDir)

# target_list.append(re.findall(r"[a-zA-Z]+\d+",each_content_list[4]))