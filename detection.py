class Detection_tools:
    def gray_values_finder(self,img_path):

        self.img_path = img_path
        import cv2
        import numpy as np
        import time

        def nothing(x):
            pass

        img = cv2.imread(self.img_path)

        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.namedWindow('mask', cv2.WINDOW_NORMAL)


        cv2.createTrackbar('H','frame',0,180,nothing)
        cv2.createTrackbar('S','frame',0,255,nothing)
        cv2.createTrackbar('V','frame',0,255,nothing)

        cv2.createTrackbar('HL','frame',0,180,nothing)
        cv2.createTrackbar('SL','frame',0,255,nothing)
        cv2.createTrackbar('VL','frame',0,255,nothing)

        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


        while True:

            hl = cv2.getTrackbarPos('HL','frame')
            sl = cv2.getTrackbarPos('SL','frame')
            vl = cv2.getTrackbarPos('VL','frame')
            h = cv2.getTrackbarPos('H','frame')
            s = cv2.getTrackbarPos('S','frame')
            v = cv2.getTrackbarPos('V','frame')

            lower = np.array([hl,sl,vl])
            upper = np.array([h,s,v])
            mask = cv2.inRange(hsv,lower,upper)

            cv2.imshow('mask',mask)

            time.sleep(0.1)

            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break

        cv2.destroyAllWindows()

    def gray_to_mask(self,img_path,hsv_lower,hsv_upper):

        self.img_path = img_path
        self.hsv_lower = hsv_lower
        self.hsv_upper = hsv_upper

        import cv2
        import numpy as np

        img = cv2.imread(self.img_path)

        cv2.namedWindow('mask', cv2.WINDOW_NORMAL)
        cv2.namedWindow('img', cv2.WINDOW_NORMAL)


        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


        lower = np.array(self.hsv_lower)
        upper = np.array(self.hsv_upper)

        # mask = cv2.bitwise_or(mask1, mask2)

        mask = cv2.inRange(hsv,lower,upper)


        contours, hier = cv2.findContours(mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        contours = sorted(contours, key = cv2.contourArea,reverse=True)

            
        for i in range(len(contours)): 
            if len(contours[i]) > 10:
                cv2.drawContours(img,[contours[i]],0,(0,255,0),-1)
                cv2.drawContours(img,[contours[i]],0,(0,0,255),1)
            # c = hier[0][i][2]
            # if c == -1 and len(contours[i]) > 0:
            #     cv2.drawContours(img,[contours[i]],0,(0,0,255),-1)

        cv2.imshow('mask',mask)

        cv2.imshow('img',img)


        cv2.waitKey(0)
        cv2.destroyAllWindows() 


    def gray_to_boxes(self,img_path,hsv_lower,hsv_upper):

        self.img_path = img_path
        self.hsv_lower = hsv_lower
        self.hsv_upper = hsv_upper

        import cv2
        import numpy as np

        img = cv2.imread(self.img_path)

        cv2.namedWindow('mask', cv2.WINDOW_NORMAL)
        cv2.namedWindow('img', cv2.WINDOW_NORMAL)


        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


        lower = np.array(self.hsv_lower)
        upper = np.array(self.hsv_upper)

        # mask = cv2.bitwise_or(mask1, mask2)

        mask = cv2.inRange(hsv,lower,upper)

        # Threshold the image
        thresh = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)[1]

        # Find contours in the image
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key = cv2.contourArea,reverse=True)

        # Loop over the contours
        for contour in contours:
            if len(contour) > 10:
                # Find the bounding rectangle
                x, y, w, h = cv2.boundingRect(contour)
                
                # Calculate the coordinates of the corners
                x1, y1 = x, y
                x2, y2 = x + w, y
                x3, y3 = x + w, y + h
                x4, y4 = x, y + h
                
                # Draw the bounding rectangle on the image
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                
                # # Draw the corners on the image
                # cv2.circle(img, (x1, y1), 5, (0, 0, 255), -1)
                # cv2.circle(img, (x2, y2), 5, (0, 0, 255), -1)
                # cv2.circle(img, (x3, y3), 5, (0, 0, 255), -1)
                # cv2.circle(img, (x4, y4), 5, (0, 0, 255), -1)

        # Show the image
        cv2.imshow('mask',mask)
        cv2.imshow('img', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    
    def gray_to_yolo(self,image_path,yolo_path):

        self.image_path = image_path
        self.yolo_path = yolo_path

        import cv2

        img = cv2.imread(self.image_path, 0)

        ret,thresh = cv2.threshold(img,127,255,0)

        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        coords = []
        for contour in contours:
            x,y,w,h = cv2.boundingRect(contour)
            # Convert coordinates to YOLO format
            x_center = (x + w/2) / img.shape[1]
            y_center = (y + h/2) / img.shape[0]
            width = w / img.shape[1]
            height = h / img.shape[0]
            # Add the coordinates to the list
            coords.append((x_center, y_center, width, height))

        with open(self.yolo_path, 'w') as f:
            for coord in coords:
                f.write(f'0 {coord[0]} {coord[1]} {coord[2]} {coord[3]}\n')

# test1 = Detection_tools()
# # test1.gray_to_mask('open_map.png',(150,2,240),(150,3,240))
# test1.gray_to_boxes('open_map.png',(150,2,240),(150,3,240))