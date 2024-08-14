import cv2
import numpy as np

#Connected camera
cap = cv2.VideoCapture(0)

#Line position
linePos_1 = 380
linePos_2 = 430
lineColor_set = 255

while True:
    ret, frame = cap.read()

    find_line = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    retval, find_line = cv2.threshold(find_line, 0, 255, cv2.THRESH_OTSU)
    colorPos_1 = find_line[linePos_1]
    colorPos_2 = find_line[linePos_2]

    try:
        lineColorCount_Pos1 = np.sum(colorPos_1 == lineColor_set)
        lineColorCount_Pos2 = np.sum(colorPos_2 == lineColor_set)

        lineIndex_Pos1 = np.where(colorPos_1 == lineColor_set)
        lineIndex_Pos2 = np.where(colorPos_2 == lineColor_set)

        if lineColorCount_Pos1 == 0:
            lineColorCount_Pos1 = 1
        if lineColorCount_Pos2 == 0:
            lineColorCount_Pos2 = 1

        leftPos_1 = lineIndex_Pos1[0][lineColorCount_Pos1 - 1]
        rightPos_1 = lineIndex_Pos1[0][0]
        centerPos_1 = int((leftPos_1 + rightPos_1)/2)

        leftPos_2 = lineIndex_Pos2[0][lineColorCount_Pos2 - 1]
        rightPos_2 = lineIndex_Pos2[0][0]
        centerPos_2 = int((leftPos_2 + rightPos_2)/2)

        center = int((centerPos_1 + centerPos_2)/2)
    except:
        center = None
        pass

    print(center)

    #Some variable could be underfined
    try:
        cv2.line(frame, (leftPos_1, (linePos_1+30)), (leftPos_1, (linePos_1-30)), (255, 128, 64), 1)
        cv2.line(frame, (rightPos_1, (linePos_1+30)), (rightPos_1, (linePos_1-30)), (64, 128, 255), 1)
        cv2.line(frame, (0, linePos_1), (640, linePos_1), (255, 255, 64), 1)

        cv2.line(frame, (leftPos_2, (linePos_2 + 30)), (leftPos_2, (linePos_2 - 30)), (255, 128, 64), 1)
        cv2.line(frame, (rightPos_2, (linePos_2 + 30)), (rightPos_2, (linePos_2 - 30)), (64, 128, 255), 1)
        cv2.line(frame, (0, linePos_2), (640, linePos_2), (255, 255, 64), 1)

        cv2.line(frame, ((center - 20), int((linePos_1 + linePos_2)/2)), ((center+20), int((linePos_1 + linePos_2)/2)), (0, 0, 0), 1)
        cv2.line(frame, ((center), int((linePos_1 + linePos_2)/2 + 20)), ((center), int((linePos_1 + linePos_2)/2 - 20)), (0, 0, 0), 1)
    except:
        pass

    cv2.imshow('Frame', frame)
    cv2.imshow('Frame Find Line', find_line)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()