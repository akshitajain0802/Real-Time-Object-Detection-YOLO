from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # You can use yolov8m.pt or yolov8l.pt for better accuracy

model.train(data='data.yaml', epochs=100, imgsz=640)
print("Training complete. Check runs/detect/train for results.")
