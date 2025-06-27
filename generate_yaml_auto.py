import os

labels_dir = 'dataset/labels/train'  # Folder containing label .txt files
dataset_path = 'dataset'  # Root dataset folder

# Set to True if labels/val folder exists
has_val = True  

# Find unique class IDs
class_ids = set()

for file in os.listdir(labels_dir):
    if file.endswith('.txt'):
        with open(os.path.join(labels_dir, file), 'r') as f:
            lines = f.readlines()
            for line in lines:
                if line.strip():  # skip empty lines
                    class_id = int(line.split()[0])
                    class_ids.add(class_id)

# Sort IDs and generate placeholder class names
max_class_id = max(class_ids)
class_names = [f'class_{i}' for i in range(max_class_id + 1)]

# Build data.yaml content
yaml_content = f"""path: {dataset_path}

train: images/train
"""

if has_val:
    yaml_content += "val: images/val\n"
else:
    yaml_content += "val: images/train\n"  # Fallback if no val folder

yaml_content += f"""
nc: {len(class_names)}
names: {class_names}
"""

# Save YAML
with open('data.yaml', 'w') as f:
    f.write(yaml_content)

print(f"✅ data.yaml created with {len(class_names)} classes: {class_names}")
