import cv2
import numpy as np
#from math import sqrt

windowName = 'tic tac toe'
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow(windowName)
count =1

a = [[2,2,2],[2,2,2],[2,2,2]]

for i in range (106,406):
    
    cv2.line(img,(306,i),(306,i+1),(255,0,0),2)
    cv2.line(img,(206,i),(206,i+1),(255,0,0),2)
    cv2.waitKey(5)
    cv2.imshow(windowName, img)
    
for j in range (106,406):
    
    cv2.line(img,(j,206),(j+1,206),(255,0,0),2)
    cv2.line(img,(j,306),(j+1,306),(255,0,0),2)
    cv2.waitKey(5)
    cv2.imshow(windowName, img)
    
def win_check(b, m):
    l = [[[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]],[[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]],[[0,0],[1,1],[2,2]],[[2,0],[1,1],[0,2]]]
    k = 0
    for i in l:
        
       
       
        
        p = 0
        for j in i:
            c = j[0]
            d = j[1]
                
            if b[c][d] == m:
                p+=1
        if p==3:
            start = i[0]
            end = i[2]
            k+=1
    if k>0:
      
        x = [156,256,356]  
        y = [156,256,356] 
        x_1 = start[0]
        x_2 = start[1]
        y_1 = end[0]
        y_2 = end[1]
        x1 = x[x_1]
        y1 = y[y_1]
        x2 = x[x_2]
        y2 = y[y_2]
        
        if m == 1:
            cv2.line(img, (x1,x2),(y1,y2), (0, 255, 0), 3)
        else:
            cv2.line(img, (x1,x2),(y1,y2), (0, 0, 255), 3)
            
        return True
        
    else:
        return False
    
    pass

def full_board_check(a):
    k = 0
    for i in range(0,3):
      for j in range (0,3):
        if a[i][j] == 2:
            k+=1
    if k == 0:
        return True
    else:
        return False
    
    pass


def win_text(win):
    
    if win == 1:
        
        image = cv2.rectangle(img, (106,406), (406,512), (0,0,0), -1)
        cv2.imshow(windowName, image)
        font = cv2.FONT_HERSHEY_SIMPLEX 
        org = (106, 459) 
        image = cv2.putText(img, 'Player 1 has won!!', org, font, 1, (0, 0, 255), 2, cv2.LINE_AA) 
        cv2.imshow(windowName, image) 
        
    if win == 2:
        
        image = cv2.rectangle(img, (106,406), (406,512), (0,0,0), -1)
        cv2.imshow(windowName, image)
        font = cv2.FONT_HERSHEY_SIMPLEX 
        org = (106, 459) 
        image = cv2.putText(img, 'Player 2 has won!!', org, font, 1, (0, 255, 0), 2, cv2.LINE_AA) 
        cv2.imshow(windowName, image) 
        
    if win == 3:
        
        image = cv2.rectangle(img, (106,406), (406,512), (0,0,0), -1)
        cv2.imshow(windowName, image)
        font = cv2.FONT_HERSHEY_SIMPLEX 
        org = (106, 459) 
        image = cv2.putText(img, 'Match is Drawn', org, font, 1, (0, 255, 255), 2, cv2.LINE_AA) 
        cv2.imshow(windowName, image) 
        

    
  
      

def draw_shape(event, x, y, flags, param):
    
   
    if event == cv2.EVENT_LBUTTONDOWN :
        
        def isInside(circle_x, circle_y, rad, x, y): 
      
   
            if ((x - circle_x) * (x - circle_x) + (y - circle_y) * (y - circle_y) <= rad * rad): 
                return True; 
            else: 
                return False;   
    
         
    
        circlex = [156,256,356]  
        circley = [156,256,356]  
        rad = 50; 
        global a
        for i in range (0,3):
            for j in range(0,3):
                circle1_x = circlex[i]
                circle1_y = circley[j]
                if(isInside(circle1_x, circle1_y, rad, x, y)): 
                    global count
                    if(count%2 == 1):
                        if a[i][j] == 2:
                            cv2.line(img, (circle1_x-20,circle1_y-20),(circle1_x+20,circle1_y+20), (0, 0, 255), 3)  
                            cv2.line(img, (circle1_x+20,circle1_y-20),(circle1_x-20,circle1_y+20), (0, 0, 255), 3)
                            a[i][j] = 1
                        
                            
                            win1  = win_check(a, 1)
                            if win1 == True:
                                victory = 1
                                win_text(victory)
                            count+=1
                                
                                
                       
                    else:
                        if a[i][j] == 2:
                            cv2.circle(img, (circle1_x, circle1_y), 25, (0, 255, 0), 3)
                            a[i][j] = 0
                        
                            
                            win2 = win_check(a, 0)
                            if win2 == True:
                                victory = 2
                                win_text(victory)
                            count+=1
                               
                                
                            

            
        if count == 10:
            victory =3
            win_text(victory)
         
            
       
cv2.setMouseCallback(windowName, draw_shape) 


def main():


    while(True):
        cv2.imshow(windowName, img)
        
        k = cv2.waitKey(1)
        
        if k == ord('Q') :
            
            break
        if k == ord('q') :
            
            break
        if k == 27:
            break
        
            

    cv2.destroyAllWindows()

if __name__ == "__main__":
    
    main()
