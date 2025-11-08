import cv2
import mediapipe as mp
import serial
import time

# Initialize serial communication
arduino = serial.Serial('COM4', 9600)
time.sleep(2)

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)

finger_tips = [4, 8, 12, 16, 20]
thumb_tip = 4

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                lm_list.append((int(lm.x * w), int(lm.y * h)))

            fingers = []

            if lm_list[thumb_tip][0] > lm_list[thumb_tip - 1][0]:
                fingers.append(1)
            else:
                fingers.append(0)

            for tip in finger_tips[1:]:
                if lm_list[tip][1] < lm_list[tip - 2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            total_fingers = fingers.count(1)
            cv2.putText(frame, f'Fingers: {total_fingers}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX,
                        1.5, (255, 0, 0), 3)

            # Send to Arduino
            arduino.write(str(total_fingers).encode())

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Finger Count LED Control", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
