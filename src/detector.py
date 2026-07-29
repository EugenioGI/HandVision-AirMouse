import cv2
import mediapipe as mp


class HandDetector:

    def __init__(
        self,
        max_num_hands=1,
        min_detection_confidence=0.3,
        min_tracking_confidence=0.3
    ):

        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=max_num_hands,
            model_complexity=0,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )

        self.frame_count = 0
        self.last_results = None


    def detect(self, frame):

        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )


        self.frame_count += 1


        # Ejecutar MediaPipe cada 2 frames
        if self.frame_count % 2 == 0:

            self.last_results = self.hands.process(rgb)


        results = self.hands.process(rgb)


        hands_data = []


        if results and results.multi_hand_landmarks:

            h, w, _ = frame.shape


            for hand_landmarks in results.multi_hand_landmarks:

                landmarks = []


                for idx, lm in enumerate(hand_landmarks.landmark):

                    x = int(lm.x * w)
                    y = int(lm.y * h)

                    landmarks.append(
                        (idx, x, y)
                    )


                hands_data.append(landmarks)


        return frame, hands_data



    def close(self):

        self.hands.close()