import pandas as pd
import os

# Load Excel file from 'dataset' folder
df = pd.read_csv('train_solution_bounding_boxes.csv')

# Image dimensions (update if different)
IMAGE_WIDTH = 676
IMAGE_HEIGHT = 380

# Output directory inside 'dataset'
OUTPUT_DIR = 'dataset/labels_yolo'
os.makedirs(OUTPUT_DIR, exist_ok=True)

for _, row in df.iterrows():
    image_name = row['image']  # Assuming 'image' column has filenames
    txt_name = os.path.splitext(image_name)[0] + '.txt'
    
    # Extract coordinates
    xmin, ymin, xmax, ymax = row['xmin'], row['ymin'], row['xmax'], row['ymax']
    
    # Convert to YOLO format
    x_center = ((xmin + xmax) / 2) / IMAGE_WIDTH
    y_center = ((ymin + ymax) / 2) / IMAGE_HEIGHT
    width = (xmax - xmin) / IMAGE_WIDTH
    height = (ymax - ymin) / IMAGE_HEIGHT
    
    # Class id = 0 (single class scenario)
    yolo_line = f"0 {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n"
    
    # Save label file
    with open(os.path.join(OUTPUT_DIR, txt_name), 'a') as f:
        f.write(yolo_line)

print(f"YOLO labels saved in '{OUTPUT_DIR}'")
