import cv2
from ultralytics import YOLO

model = YOLO('runs/detect/train/weights/best.pt')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    for r in results:
        boxes = r.boxes.xyxy
        confs = r.boxes.conf
        cls = r.boxes.cls

        for box, conf, cl in zip(boxes, confs, cls):
            if conf > 0.5:
                x1, y1, x2, y2 = map(int, box)
                label = f'{model.names[int(cl)]} {conf:.2f}'
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('Real-Time Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
