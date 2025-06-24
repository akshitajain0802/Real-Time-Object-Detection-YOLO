# Real-Time-Object-Detection-YOLO
Real-Time Object Detection system using YOLOv8 for 20 unique object classes. Built with Deep Learning and Computer Vision.
This project is a Deep Learning-based Computer Vision system that performs real-time object detection using the YOLO (You Only Look Once) model. The system is trained to detect 20 unique objects using a dataset of 9000 labeled images, achieving a precision of 76.4% after applying confidence and probability thresholds.

# Features
Real-time detection from webcam or video
Trained with YOLOv8 for fast, accurate detection
Detects 20 different object categories
Uses confidence threshold filtering for improved precision
Built with Deep Learning (CNNs) and Computer Vision

# Project Structure
Real-Time-Object-Detection-YOLO/
├── dataset/               # Image dataset (optional for large datasets)
├── weights/               # Trained YOLOv8 model weights (.pt files)
├── scripts/
│   ├── train.py           # Script to train the model
│   ├── real_time_detect.py # Real-time detection with webcam
├── data.yaml              # Dataset configuration file
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
└── .gitignore

# Installation
1) Clone the repository:
git clone https://github.com/akshitajain0802/Real-Time-Object-Detection-YOLO.git
cd Real-Time-Object-Detection-YOLO

2) Install dependencies:
pip install -r requirements.txt

3)Ensure your dataset is labeled in YOLO format and data.yaml is configured.
