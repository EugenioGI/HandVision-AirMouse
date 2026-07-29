import math


class GestureRecognizer:

    def __init__(self):
        pass


    def distance(self, p1, p2):
        """
        Distancia euclidiana entre dos puntos
        """

        return math.sqrt(
            (p2[0] - p1[0]) ** 2 +
            (p2[1] - p1[1]) ** 2
        )


    def finger_up(self, landmarks, tip, pip):
        """
        Comprueba si un dedo está levantado

        tip = punta del dedo
        pip = articulación media
        """

        return landmarks[tip][2] < landmarks[pip][2]


    def fingers_state(self, landmarks):

        fingers = []


        # Pulgar
        if landmarks[4][1] < landmarks[3][1]:
            fingers.append(1)
        else:
            fingers.append(0)


        # Índice
        fingers.append(
            1 if self.finger_up(
                landmarks,
                8,
                6
            )
            else 0
        )


        # Medio
        fingers.append(
            1 if self.finger_up(
                landmarks,
                12,
                10
            )
            else 0
        )


        # Anular
        fingers.append(
            1 if self.finger_up(
                landmarks,
                16,
                14
            )
            else 0
        )


        # Meñique
        fingers.append(
            1 if self.finger_up(
                landmarks,
                20,
                18
            )
            else 0
        )


        return fingers



    def pinch_detected(self, landmarks):
        """
        Detecta pulgar tocando índice
        """

        thumb = landmarks[4]
        index = landmarks[8]


        dist = self.distance(
            thumb[1:],
            index[1:]
        )


        return dist < 35



    def detect(self, landmarks):

        fingers = self.fingers_state(landmarks)


        # ✊ Puño cerrado primero
        if fingers == [0,0,0,0,0]:

            return "DRAG"


        # 🖐 Mano abierta

        if fingers == [1,1,1,1,1]:

            return "OPEN"


        # ✌️ Click derecho

        if fingers == [0,1,1,0,0]:

            return "RIGHT_CLICK"


        # 🤏 Click izquierdo

        if self.pinch_detected(landmarks):

            return "LEFT_CLICK"


        return "MOVE"