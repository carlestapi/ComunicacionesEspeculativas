# -*- coding: utf-8 -*-
import numpy as np
import cv2
import sys


cap = cv2.VideoCapture(1)

while(True):
    #grabar cuadro por cuadro
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Mostrar el resultado de la comversion
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#liberar
cap.release()
cv2.destroyAllWindows()
