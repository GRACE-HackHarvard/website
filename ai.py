import cv2

def detect_light_capture(ret, frame):
    ret, _ = ret, frame

    if not ret:
        print("No First Frame.")
        return
    
    if not ret:
        return

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    threshold = 150 
    _, thresholded = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        max_contour = max(contours, key=cv2.contourArea)

        moments = cv2.moments(max_contour)
        cx = int(moments["m10"] / moments["m00"]) if moments["m00"] else 0
        cy = int(moments["m01"] / moments["m00"]) if moments["m00"] else 0

        # cv2.circle(gray, (cx, cy), 10, (0, 255, 0), -1)

        return cx, cy

    # cv2.imshow("yay", gray)

    # cap.release()
    # cv2.destroyAllWindows()
