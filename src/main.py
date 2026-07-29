import cv2
import time

from calibration import Calibration
from cursor import Cursor
from detector import HandDetector
from smoothing import Smoother
from gestures import GestureRecognizer


cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)



detector = HandDetector()
cursor = Cursor()
calibration = Calibration()
smoother = Smoother(0.20)
gesture = GestureRecognizer()


prev_time = 0

last_gesture = "NONE"

dragging = False



while True:

    success, frame = cap.read()

    if not success:
        break


    frame = cv2.flip(frame, 1)


    frame, hands = detector.detect(frame)


    current_gesture = "NONE"



    if hands:

        frame_h, frame_w, _ = frame.shape


        # Punta del dedo índice
        index_tip = hands[0][8]

        _, x, y = index_tip



        # Detectar gesto
        current_gesture = gesture.detect(hands[0])



        # Coordenadas cámara -> pantalla

        screen_x, screen_y = calibration.map_point(
            x,
            y,
            frame_w,
            frame_h
        )


        # Suavizado

        smooth_x, smooth_y = smoother.smooth(
            screen_x,
            screen_y
        )



        # Mover cursor siempre

        cursor.move(
            smooth_x,
            smooth_y
        )



        # ==========================
        # CLICS
        # ==========================

        if current_gesture != last_gesture:


            if current_gesture == "LEFT_CLICK":

                cursor.left_click()



            elif current_gesture == "RIGHT_CLICK":

                cursor.right_click()



        # ==========================
        # DRAG
        # ==========================

        if current_gesture == "DRAG" and not dragging:

            cursor.press_down()
            dragging = True



        elif current_gesture != "DRAG" and dragging:

            cursor.press_up()
            dragging = False



        # Dibujar punta índice

        cv2.circle(
            frame,
            (x, y),
            12,
            (0, 0, 255),
            -1
        )



        cv2.putText(
            frame,
            f"Gesture: {current_gesture}",
            (20,160),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,255),
            2
        )


        cv2.putText(
            frame,
            f"Screen: {smooth_x}, {smooth_y}",
            (20,120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,255),
            2
        )



    else:

        # Si desaparece la mano
        # soltamos el drag por seguridad

        if dragging:

            cursor.press_up()
            dragging = False



        last_gesture = "NONE"



    last_gesture = current_gesture



    # ==========================
    # FPS
    # ==========================

    current_time = time.time()


    fps = (
        1 / (current_time - prev_time)
        if prev_time
        else 0
    )


    prev_time = current_time



    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )


    cv2.putText(
        frame,
        f"Hands: {len(hands)}",
        (20,80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255,0,0),
        2
    )



    cv2.imshow(
        "HandVision Air Mouse",
        frame
    )



    if cv2.waitKey(1) & 0xFF == 27:
        break



# Seguridad: soltar mouse si termina

if dragging:

    cursor.press_up()



detector.close()

cap.release()

cv2.destroyAllWindows()