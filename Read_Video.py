import cv2


#Cpture our video
vid= cv2.VideoCapture(0)


if (vid.isOpened() == False):
    print("Unable to capture feed")


width=int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)
height=int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)
fps=int(vid.get(cv2.CAP_PROP_FPS))
print(fps)


out= cv2.VideoWriter("Boxing.mp4", cv2.VideoWriter_fourcc(*'DIVx'), 30 , (width, height))

while(True):

    ret, frame = vid.read()
    cv2.imshow("Web Cam", frame)
    out.write(frame)

    if cv2.waitKey(25)== 32:
        break

vid.release()
out.release()

cv2.destroyAllWindows()