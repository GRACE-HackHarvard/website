import cv2
import matplotlib.pyplot as plt

#cv2.namedWindow("yay", cv2.WINDOW_AUTOSIZE) 
def calibrate_capture(frame):
    #print(frame)

    B, G, R = cv2.split(frame)

    l = [R, G, B]
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

    threshold = 150

    thresholded = (cv2.threshold(i, threshold, 255, cv2.THRESH_BINARY)[1] for i in l)
    contours = [cv2.findContours(i, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0] for i in thresholded]

    if all(len(x) > 0 for x in contours):
        max_contours = [max(i, key=cv2.contourArea) for i in contours]

        l = []
        for cur in max_contours:
            moments = cv2.moments(cur)
            cx = int(moments["m10"] / moments["m00"]) if moments["m00"] else 0
            cy = int(moments["m01"] / moments["m00"]) if moments["m00"] else 0
            l.append((cx, cy))
            # cv2.circle(frame, (cx, cy), 10, (0, 255, 0), -1)

        for i in range(3):
            cv2.circle(frame, l[i], 10, colors[i], -1)
        
        cv2.imshow("redyay", frame)
        cv2.waitKey(33)

        return True, l

    return False, None
    #cv2.imshow("yay", _)

def detect_light_capture(frame):
    _ = frame

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

        # cv2.circle(gray, (cx, cy), 10, (0, 255, 0), -1
        return True, cx, cy

    return False, None, None

    # cv2.imshow("yay", gray)

    # cap.release()
    # cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)
if __name__ == "__main__":
    while True:
        ret, frame = cap.read()
        if not ret:
            print("cry and be sad")
            continue

        fancy_stuff = calibrate_capture(frame)
        print(fancy_stuff)
        if (fancy_stuff[0] == False):
            continue

        fancy_stuff = fancy_stuff[1]

        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
        for i in range(3):
            cv2.circle(frame, fancy_stuff[i], 10, colors[i], -1)

        cv2.imshow("yay", frame)
        if cv2.waitKey(30) == "z":
            break