from pupil_apriltags import Detector
import cv2
import numpy as np
import time
import winsound
vid = cv2.VideoCapture(0)# define a video capture object

delay=0.1
id_to_color = {'24': 103,
               '25': 119,
               '26': 111,
               '27': 121,
               '28': 114,
               '32': 98
               }


at_detector = Detector(families='tag36h11',
                       nthreads=1,
                       quad_decimate=1.0,
                       quad_sigma=0.0,
                       refine_edges=1,
                       decode_sharpening=0.25,
                       debug=0)
def scambia():
    return 1

    
def scan():
    tutto=[]
    
    for i in range(6):
        winsound.PlaySound('sound.wav',winsound.SND_FILENAME)
        time.sleep(delay)
        
        
        cenX=[]
        cenY=[]
        faccia=[]
        sticker=[]
        tags=[]
        #input("Sto aspettando...")
        while(len(tags)<9):
            # Capture the video frame  
            _, color_img = vid.read() 
            # Display the resulting frame 
            img = cv2.cvtColor(color_img,cv2.COLOR_BGR2GRAY)
            tags = at_detector.detect(img, estimate_tag_pose=False, camera_params=None, tag_size=None)
            
        for tag in tags:
            centro=tag.center
            cenX.append(centro[0])
            cenY.append(centro[1])
            sticker.append([id_to_color[str(tag.tag_id)],centro])
            faccia.append(centro)
            
            
            for idx in range(len(tag.corners)):
                '''cv2.line(
                    color_img,
                    tuple(tag.corners[idx - 1, :].astype(int)),
                    tuple(tag.corners[idx, :].astype(int)),
                    (0, 0, 0),
                )'''
                cv2.putText(
                    color_img,
                    str(id_to_color[str(tag.tag_id)]),
                    org=(
                        tag.corners[0, 0].astype(int) + 10,
                        tag.corners[0, 1].astype(int) + 10,
                    ),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.5,
                    color=(0, 255, 0),
                )
            
        scambi=1
        while(scambi>0):
            scambi=0
            #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
            if faccia[0][0]>faccia[1][0]:
                faccia[1],faccia[0]=faccia[0],faccia[1]
                sticker[1],sticker[0]=sticker[0],sticker[1]
                scambi = scambia()
                continue

            if faccia[1][0]>faccia[2][0]:
                faccia[1],faccia[2]=faccia[2],faccia[1]
                sticker[1],sticker[2]=sticker[2],sticker[1]
                scambi = scambia()
                continue
            #345
            if faccia[3][0]>faccia[4][0]:
                faccia[4],faccia[3]=faccia[3],faccia[4]
                sticker[4],sticker[3]=sticker[3],sticker[4]
                scambi = scambia()
                continue
            if faccia[4][0]>faccia[5][0]:
                faccia[4],faccia[5]=faccia[5],faccia[4]
                sticker[4],sticker[5]=sticker[5],sticker[4]
                scambi = scambia()
                continue
            #678
            if faccia[6][0]>faccia[7][0]:
                faccia[7],faccia[6]=faccia[6],faccia[7]
                sticker[7],sticker[6]=sticker[6],sticker[7]
                scambi = scambia()
                continue
            if faccia[7][0]>faccia[8][0]:
                faccia[7],faccia[8]=faccia[8],faccia[7]
                sticker[7],sticker[8]=sticker[8],sticker[7]
                scambi = scambia()
                continue
            #diag3
            if faccia[0][0]>faccia[4][0]:
                faccia[0],faccia[4]=faccia[4],faccia[0]
                sticker[0],sticker[4]=sticker[4],sticker[0]
                scambi = scambia()
                continue
            if faccia[4][0]>faccia[8][0]:
                faccia[4],faccia[8]=faccia[8],faccia[4]
                sticker[8],sticker[4]=sticker[4],sticker[8]
                scambi = scambia()
                continue
                
            if faccia[6][0]>faccia[4][0]:
                faccia[6],faccia[4]=faccia[4],faccia[6]
                sticker[6],sticker[4]=sticker[4],sticker[6]
                scambi = scambia()
                continue
            if faccia[4][0]>faccia[2][0]:
                faccia[2],faccia[4]=faccia[4],faccia[2]
                sticker[2],sticker[4]=sticker[4],sticker[2]
                scambi = scambia()
                continue
            #diag2
            if faccia[3][0]>faccia[1][0]:
                faccia[3],faccia[1]=faccia[1],faccia[3]
                sticker[3],sticker[1]=sticker[1],sticker[3]
                scambi = scambia()
                continue
            if faccia[1][0]>faccia[5][0]:
                faccia[5],faccia[1]=faccia[1],faccia[5]
                sticker[5],sticker[1]=sticker[1],sticker[5]
                scambi = scambia()
                continue
                
            if faccia[7][0]>faccia[5][0]:
                faccia[5],faccia[7]=faccia[7],faccia[5]
                sticker[5],sticker[7]=sticker[7],sticker[5]
                scambi = scambia()
                continue
            if faccia[3][0]>faccia[7][0]:
                faccia[3],faccia[7]=faccia[7],faccia[3]
                sticker[3],sticker[7]=sticker[7],sticker[3]
                scambi = scambia()
                continue
            #altri
            
            


            
            #YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
            if faccia[0][1]>faccia[3][1]:
                faccia[0],faccia[3]=faccia[3],faccia[0]
                sticker[0],sticker[3]=sticker[3],sticker[0]
                scambi = scambia()
                continue
            if faccia[3][1]>faccia[6][1]:
                faccia[3],faccia[6]=faccia[6],faccia[3]
                sticker[3],sticker[6]=sticker[6],sticker[3]
                scambi = scambia()
                continue
            #147
            if faccia[1][1]>faccia[4][1]:
                faccia[1],faccia[4]=faccia[4],faccia[1]
                sticker[1],sticker[4]=sticker[4],sticker[1]
                scambi = scambia()
                continue
            if faccia[4][1]>faccia[7][1]:
                faccia[4],faccia[7]=faccia[7],faccia[4]
                sticker[4],sticker[7]=sticker[7],sticker[4]
                scambi = scambia()
                continue
            #258
            if faccia[2][1]>faccia[5][1]:
                faccia[2],faccia[5]=faccia[5],faccia[2]
                sticker[2],sticker[5]=sticker[5],sticker[2]
                scambi = scambia()
                continue
            if faccia[5][1]>faccia[8][1]:
                faccia[5],faccia[8]=faccia[8],faccia[5]
                sticker[5],sticker[8]=sticker[8],sticker[5]
                scambi = scambia()
                continue
            #diag3
            if faccia[0][1]>faccia[4][1]:
                faccia[0],faccia[4]=faccia[4],faccia[0]
                sticker[0],sticker[4]=sticker[4],sticker[0]
                scambi = scambia()
                continue
            if faccia[4][1]>faccia[8][1]:
                faccia[8],faccia[4]=faccia[4],faccia[8]
                sticker[8],sticker[4]=sticker[4],sticker[8]
                scambi = scambia()
                continue

            if faccia[2][1]>faccia[4][1]:
                faccia[2],faccia[4]=faccia[4],faccia[2]
                sticker[2],sticker[4]=sticker[4],sticker[2]
                scambi = scambia()
                continue
            if faccia[4][1]>faccia[6][1]:
                faccia[6],faccia[4]=faccia[4],faccia[6]
                sticker[6],sticker[4]=sticker[4],sticker[6]
                scambi = scambia()
                continue
            #diag2
            if faccia[1][1]>faccia[3][1]:
                faccia[1],faccia[3]=faccia[3],faccia[1]
                sticker[1],sticker[3]=sticker[3],sticker[1]
                scambi = scambia()
                continue
            if faccia[1][1]>faccia[5][1]:
                faccia[1],faccia[5]=faccia[5],faccia[1]
                sticker[1],sticker[5]=sticker[5],sticker[1]
                scambi = scambia()
                continue

            if faccia[3][1]>faccia[7][1]:
                faccia[7],faccia[3]=faccia[3],faccia[7]
                sticker[7],sticker[3]=sticker[3],sticker[7]
                scambi = scambia()
                continue
            if faccia[5][1]>faccia[7][1]:
                faccia[7],faccia[5]=faccia[5],faccia[7]
                sticker[7],sticker[5]=sticker[5],sticker[7]
                scambi = scambia()
                continue
        #controllare indentazione:
        for k in sticker:
            tutto.append(k[0])#tutto è una faccia
        
        #cv2.imshow("Detected tags", color_img)
        #fine for(6)

    return tutto

if __name__=="__main__":
    print(scan())
    #print(scan())
    
