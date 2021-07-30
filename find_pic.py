import cv2
import pyscreeze
import numpy as np
# import a

class SearchMultiIcon(object):
    def __init__(self, img1_path, img2, thres,ref_x = 0, ref_y=0):

        self.img1_path = img1_path
        #self.img2_path = img2_path
        self.img2 = img2
        self.ref_x = ref_x
        self.ref_y = ref_y
        self.rect_icon = []
        self.centre_icon = []
        self.thres = thres


    def search_multi_icon(self, minVal=100, maxVal=200):
        minVal = minVal
        maxVal = maxVal

        screen_rgb = self.img2
        screen_gray = cv2.cvtColor(screen_rgb, cv2.COLOR_BGR2GRAY)
        icon_gray = cv2.imread(self.img1_path,0)
        
        screen_canny = cv2.Canny(screen_gray, minVal, maxVal)
        icon_canny = cv2.Canny(icon_gray, minVal, maxVal)
        
        w, h = icon_gray.shape[::-1]
        res = cv2.matchTemplate(screen_canny,icon_canny,cv2.TM_CCOEFF_NORMED)
        threshold = self.thres
        loc = np.where( res >= threshold)
        rect_list = []
        centre_list = []
        for pt in zip(*loc[::-1]):
            cv2.rectangle(screen_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
            rect_list.append([pt[0],pt[1], w,h])
            centre_list.append([pt[0]+(w/2),pt[1]+(h/2)])
        self.rect_icon = rect_list
        self.centre_icon = centre_list
        
    def search_multi_icon_transpost(self, minVal=100, maxVal=200):
        minVal = minVal
        maxVal = maxVal
        #screen_rgb = cv2.imread(self.img2_path)
        screen_rgb = self.img2
        screen_gray = cv2.cvtColor(screen_rgb, cv2.COLOR_BGR2GRAY)
        icon_gray = cv2.imread(self.img1_path,0)
        
        screen_canny = cv2.Canny(screen_gray, minVal, maxVal)
        icon_canny = cv2.Canny(icon_gray, minVal, maxVal)
        
        w, h = icon_gray.shape[::-1]
        res = cv2.matchTemplate(screen_canny,icon_canny,cv2.TM_CCOEFF_NORMED)
        threshold = self.thres
        loc = np.where( res >= threshold)
        rect_list = []
        centre_list = []
        for pt in zip(*loc[::-1]):
            cv2.rectangle(screen_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
            rect_list.append([pt[0]+self.ref_x,pt[1]+self.ref_y, w,h])
            centre_list.append([pt[0]+(w/2)+self.ref_x,pt[1]+(h/2)+self.ref_y])
        self.rect_icon = rect_list
        self.centre_icon = centre_list

