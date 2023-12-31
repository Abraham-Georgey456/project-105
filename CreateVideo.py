import os
import cv2

path = "E:/Coding/Project-105/Images/"

Images = []

for i in os.listdir(path):
    name, ext = os.path.splitext(i)
    
    if ext in [".gif",".jpg", ".png", ".jpeg",".jfif"]:
        file_name = path+"/"+i
        print(file_name)
        Images.append(file_name)
        count = len(Images)
        
        
frame = cv2.imread(Images[0])
w,h,l = frame.shape
size = (w,h)
print(size)

out = cv2.VideoWriter("Project.avi", cv2.VideoWriter_fourcc(*'DIVX'),1.0,size)

for i in range(0,count-1):
    frame = cv2.imread(Images[i])
    out.write(frame)
    cv2.imshow("frame2",frame)


print("Done")

cv2.waitKey(0)
out.release()

