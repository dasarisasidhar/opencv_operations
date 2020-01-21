import numpy as np
import datetime
import cv2

cap = cv2.VideoCapture(0)

def access_camera():
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        #show frame-by-frame
        cv2.imshow('frame',frame)
        # if q is pressed break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    """
    For example, I can check the frame width and height by cap.get(3) and cap.get(4).
    It gives me 640x480 by default. But I want to modify it to 320x240.
    Just use ret = cap.set(3,320) and ret = cap.set(4,240).
   """
def mouse_events():
    #to find all events
    #events = [i for i in dir(cv2) if "EVENT" in i]
    #print(events)
    pass

def click_event(event, x, y, flags, params):
    if(events == cv2.EVENT_LBUTTONDOWN):
        # do the operation required
        pass

#mouse_events()   

def save_video():
    #declare fourcc type
    temp = np.empty([1])
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # cv2.CAP_PROP_FRAME_WIDTH default vale is 3
    # CAP_PROP_FRAME_HEIGHT default value is 5
    #set height and width manually  
    #width = cap.set(3, 1020)
    #height = cap.set(4, 720)

    #details to save --> name of the file, fourcc, no of frames, width and height of frame to save
    out = cv2.VideoWriter('output.avi',fourcc, 20.0, (width, height))
    #to save video
    while(cap.isOpened()):
        ret, frame = cap.read()
        # ret is true if frame is avaliable else it is false
        # frame is the matrix containing the value of data
        if ret==True:
            font = cv2.FONT_HERSHEY_SIMPLEX
            datetime_ = str(datetime.datetime.now())
            #get the time and display in top left corner
            frame = cv2.putText(frame, datetime_, (10,50), font, 1, (255,255,255), 1, cv2.LINE_AA)
            #write the out data to file with 20 frames for second 
            #if(frame.all() != temp.all()):
            out.write(frame)
            #display thhe same out file
            cv2.imshow('frame',frame)
             #temp = frame
            # q is to quite     
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()


save_video()

def drawing_shapes():
    """
    Learn to draw different geometric shapes with OpenCV
    You will learn these functions : cv2.line(), cv2.circle(), 
    cv2.rectangle(), cv2.ellipse(), cv2.putText() etc.
    """
    
    # Create a black image
    img = np.zeros((512,512,3), np.uint8)
    cv2.namedWindow('image')

    # Draw a diagonal blue line with thickness of 5 px
    img1 = cv2.line(img,(0,0),(511,511),(255,0,0),5)

    img2 = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

    img3 = cv2.circle(img,(447,63), 63, (0,0,255), -1)

    img4 = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

    pts_for_polygon = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
    pts_for_polygon = pts_for_polygon.reshape((-1,1,2))
    img5 = cv2.polylines(img,[pts_for_polygon],True,(0,255,255))

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

#drawing_shapes()
def nothing(x):
    pass

def maniputaion():
    img = np.zeros((300,512,3), np.uint8)
    cv2.imshow('img',gray)

    # create trackbars for color change
    cv2.createTrackbar('R','image',0,255,nothing)
    cv2.createTrackbar('G','image',0,255,nothing)
    cv2.createTrackbar('B','image',0,255,nothing)

    # create switch for ON/OFF functionality
    switch = '0 : OFF \n1 : ON'
    cv2.createTrackbar(switch, 'image',0,1,nothing)

    while(1):
        cv2.imshow('image',img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        # get current positions of four trackbars
        r = cv2.getTrackbarPos('R','image')
        g = cv2.getTrackbarPos('G','image')
        b = cv2.getTrackbarPos('B','image')
        s = cv2.getTrackbarPos(switch,'image')

        if s == 0:
            img[:] = 0
        else:
            img[:] = [b,g,r]

    cv2.destroyAllWindows()

#maniputaion()

