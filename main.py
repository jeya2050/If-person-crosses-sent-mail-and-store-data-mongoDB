import torch
import pymongo
from pymongo import MongoClient
import cv2
import smtplib
import time

times=0
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
num=1
video=cv2.VideoCapture(0)

def mail_sent():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("jeyagobi00@gmail.com", "hkdpjvdoctdkzkjl")
    message = "some person cross in the frame"
    s.sendmail("jeyagoi00@gmail.com", "jeyaraman@kssmart.co", message)
    s.quit()
    return("mail sent")
    
def store_on_db():
    cluster=MongoClient("mongodb+srv://jeya:jeya123@cluster0.3qe9mq7.mongodb.net/?retryWrites=true&w=majority")
    db=cluster["new"]
    collection=db["python"]
    post={"s.no": num,"class":"person" ,"time" : current_time}
    collection.insert_one(post)
    print("save on database")
    
while True:
    current_time = time.strftime("%H:%M:%S")
    _,frame=video.read()
    results = model(frame)
    df=results.pandas().xyxy[0]
    print(df)
    for ind in df.index:
        x1,y1=int(df["xmin"][ind]),int(df["ymin"][ind])
        x2,y2=int(df["xmax"][ind]),int(df["ymax"][ind])
        label=df["name"][ind]
        cv2.rectangle(frame,(x1,y1),(x2,y2),(255,255,0),3)
        cv2.putText(frame,label,(x1,y1+5),cv2.FONT_HERSHEY_PLAIN,2,(255,255,0),2)
   
        if label == "person" and times==0:
           m= mail_sent()
           print(m)
           times+=1
           s=store_on_db()
           print(s)
           num+=1
        if label =="person":
            times+=1
            print(times)
        if times==50:
            times=0
    cv2.imshow("video",frame)
    q=cv2.waitKey(10)

    if q == ord("q"):
        break