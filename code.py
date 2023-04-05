#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install opencv-python


# In[2]:


import cv2


# In[3]:


import numpy as np
import pandas as pd


# In[6]:


img = cv2.imread("C:\\Users\\Devashree\\Desktop\\T2I_b.png")
imS = cv2.resize(img, (960, 540)) 


# In[7]:


index=["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('C:\\Users\\Devashree\\Desktop\\colors.csv', names=index, header=None)


# In[8]:


clicked = False
r = g = b = xpos = ypos = 0


# In[9]:


def recognize_color(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname


# In[10]:


def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = imS[y,x]
        b = int(b)
        g = int(g)
        r = int(r)


# In[11]:


cv2.namedWindow('Color Recognition App')


# In[12]:


cv2.setMouseCallback('Color Recognition App', mouse_click)


# In[13]:


while(1):
    cv2.imshow("Color Recognition App",imS)
    if (clicked):
   
 
        cv2.rectangle(imS,(20,20), (750,60), (b,g,r), -1)
        text = recognize_color(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        
        cv2.putText(imS, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

        if(r+g+b>=600):
            cv2.putText(imS, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False
        #Break the loop when user hits 'esc' key    
    if cv2.waitKey(20) & 0xFF ==27:
        break
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




