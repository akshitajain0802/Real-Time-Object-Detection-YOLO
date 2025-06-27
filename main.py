from ultralytics import YOLO

# Load pre-trained model or your own checkpoint
model = YOLO('yolov8n.pt')

# Train the model
model.train(data='dataset/data.yaml', epochs=1, imgsz=640)

# You can also validate
model.val()
