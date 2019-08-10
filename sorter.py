#make a new directory for all files and will cut paste the file in respective extension
#name folder
import glob, os
import shutil 
#a=['.txt',".zip"]
#print(a[0])
os.chdir("d:/downloads")#ur working directort where all types of extension file reside
for file in glob.glob("*.*"):
    print(file)
    import os.path
    extension = os.path.splitext(file)[1]
   
    
    newpath = r'd:\downloads'
    n_p=newpath+'/'+extension
    if not os.path.exists(n_p):
        os.makedirs(n_p)
    shutil.move(file,n_p)

