
import cv2
import time
from ultralytics import YOLO
import smtplib
from email.mime.text import MIMEText

# Load YOLOv8 Nano model
model = YOLO("yolov8n.pt")

# Email configuration (example)
SENDER_EMAIL = "johnjonnie098@gmail.com"
RECEIVER_EMAIL = "jijoivin788@gmail.com"
PASSWORD = "helloworld"

last_alert_time = 0
ALERT_COOLDOWN = 300  # 5 minutes

cap = cv2.VideoCapture(0)  # webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_resized = cv2.resize(frame, (640, 640))
    results = model(frame_resized, conf=0.5)

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]

            if label.lower() in ["elephant", "boar", "wild boar"]:
                current_time = time.time()
                if current_time - last_alert_time > ALERT_COOLDOWN:
                    msg = MIMEText(f"{label} detected in field!")
                    msg["Subject"] = "⚠️ Animal Intrusion Alert"
                    msg["From"] = SENDER_EMAIL
                    msg["To"] = RECEIVER_EMAIL

                # server = smtplib.SMTP("smtp.gmail.com", 587)
                 #   server.starttls()
                  #  server.login(SENDER_EMAIL, PASSWORD)
                   # server.send_message(msg)
                    #server.quit()
                    print("ALERT: Wild animal detected!")

                    last_alert_time = current_time

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame_resized, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(frame_resized, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    cv2.imshow("Wild Animal Detection", frame_resized)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
