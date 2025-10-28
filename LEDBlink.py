import cv2
import serial
import time
arduino = serial.Serial('COM7', 9600, timeout=1)
time.sleep(2)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera")
    exit()
led_state = "OFF"  
face_count = 0      
no_face_count = 0   
THRESHOLD = 5 
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    if len(faces) > 0:
        face_count += 1
        no_face_count = 0
        if face_count >= THRESHOLD and led_state != "ON":
            arduino.write(b'1')  
            led_state = "ON"
            print("LED ON")
    else:
        no_face_count += 1
        face_count = 0
        if no_face_count >= THRESHOLD and led_state != "OFF":
            arduino.write(b'0')  
            led_state = "OFF"
            print("LED OFF")
    status_text = f"LED {led_state}"
    cv2.putText(frame, status_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 0) if led_state=="ON" else (0, 0, 255), 2)
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
arduino.close()
cv2.destroyAllWindows()