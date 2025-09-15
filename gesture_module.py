# gesture identificator
import mediapipe as mp
import cv2

class GestureDetector:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=1)
        self.mp_draw = mp.solutions.drawing_utils

    def detect(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)
        gesture = None
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                # Aquí puedes definir tus gestos según landmarks
                # Ejemplo simple: si el pulgar está arriba → gesto "agrandar"
                gesture = "agrandar"
                self.mp_draw.draw_landmarks(frame, handLms, self.mp_hands.HAND_CONNECTIONS)
        return gesture, frame
