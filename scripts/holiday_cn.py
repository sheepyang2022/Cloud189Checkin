import os
from datetime import datetime

if __name__ == "__main__":
    # 创建文件夹
    if not os.path.exists("today"):
        os.mkdir("today")
    # 今天日期写入文件
    timeNow = datetime.now()
    print("timeNow=" + str(timeNow))
    fp = open("today/time.txt", "w+", encoding='utf-8')     
    fp.write(str(timeNow))
    fp.close()
