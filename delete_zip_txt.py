#for sending all .zi[ and .txt file in "d/downloads" directory to recycle bin
import shutil
from send2trash import send2trash
import glob, os
total, used, free = shutil.disk_usage("d:/")

print("Total: %d GB" % (total // (2**30)))
print("Used: %d GB" % (used // (2**30)))
print("Free: %d GB" % (free // (2**30)))

used_1=used//(2**30)
print(used_1)
 # print(type(used_1))
if used_1>10:
    print("excess..deleting txt files")
    #import glob, os
    os.chdir("d:/downloads")#replace your directory where u hve all ur zip n txt files.
    for file in glob.glob("*.zip"):
        #print(file)
        #from send2trash import send2trash
        send2trash(file)
    for file in glob.glob("*.txt"):
        #print(file)
        #from send2trash import send2trash
        send2trash(file)
