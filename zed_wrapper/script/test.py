#!/usr/bin/env python
​
import sys
import pyzed.sl as sl
import cv2
​
def main( ):
    init = sl.InitParameters()
    init.camera_resolution = sl.RESOLUTION.RESOLUTION_VGA
    init.depth_mode = sl.DEPTH_MODE.DEPTH_MODE_NONE
    init.camera_fps = 15 
    if (len(sys.argv) > 1) :
        ip = "127.0.0.1" 
        init.set_from_stream(ip,30000)
    else :
        exit(1)
    cam = sl.Camera()
    status = cam.open(init)
    if status != sl.ERROR_CODE.SUCCESS:
        print("fooooo")
        print(repr(status))
        exit(1)
    runtime = sl.RuntimeParameters()
    mat = sl.Mat()
    key = ' '
    print("  Quit : CTRL+C\n")
    while key != 113:
        err = cam.grab(runtime)
        if (err == sl.ERROR_CODE.SUCCESS) :
            cam.retrieve_image(mat, sl.VIEW.VIEW_LEFT)
            cv2.imshow("ZED", mat.get_data())
            key = cv2.waitKey(1)
        else :
            key = cv2.waitKey(1)
​
    cam.disable_streaming()
    #cam.close()
    
if __name__ == "__main__":
    main()