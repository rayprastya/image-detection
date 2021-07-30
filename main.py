import cv2
import pyscreeze
import numpy as np
import find_pic as fp
from time import sleep

def wait_icon(wait,do_every,sensitivity,times,min_icon,icon):
    try:
        wait_count = 0
        if wait == 'appear':
            for i in range(times+1):
                sleep(do_every)
                iconss = locate_multi_icon(icon, float(sensitivity) * 0.01)
                total_icons = len(iconss)
                if (total_icons < int(min_icon)) & (wait_count < int(times)):
                    print(icon+ " :No icon found, continue to detect")
                    wait_count += 1

                elif (total_icons < int(min_icon)) & (wait_count >= int(times)):
                    print("Erorr Icon Can't be found")
                    return False
                else:
                    print("Icon found")
                    wait_count = 0
                    return True

        elif wait == 'disappear':
            for i in range(times+1):
                sleep(do_every)
                iconss = locate_multi_icon(icon, float(sensitivity) * 0.01)
                total_icons = len(iconss)
                if total_icons > 0 and wait_count < int(times):
                    wait_count += 1

                elif wait_count >= int(times):
                    print("Error Icon Still Here")
                    return False

                elif total_icons == 0:
                    print(icon+ " :No icon found, continue")
                    wait_count = 0
                    return True

        return False

    except:
        print("error")
    
def locate_multi_icon(icon,thres):
    #img2_path = 'print_screen.png' # Print screen
    img2 = pyscreeze.screenshot()
    np_img2 = np.array(img2)
    opencv_img2 = cv2.cvtColor(np_img2, cv2.COLOR_RGB2BGR)
    img1_path =  icon         # queryImage
    Searchbutton = fp.SearchMultiIcon(img1_path,opencv_img2,thres)

    # minVal, maxVal = app_global.edge_detection_parameters
    Searchbutton.search_multi_icon()

    return Searchbutton.centre_icon

###########################################

sensitivity = input('input sensitivity : ')
icon = input('input icon: ')
wait = 'appear'
do_every = 2
times = 2
min_icon = 1

print(wait_icon(wait,do_every,sensitivity,times,min_icon,icon))
