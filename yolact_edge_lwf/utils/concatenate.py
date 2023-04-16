import json

# defining the path to the json files
bbox_path = './results/bbox_detections.json'
mask_path = './results/mask_detections.json' 

def generate_concatenated_info_file(info_file, new_classes):

    # read the json files
    with open(bbox_path, 'r') as f:
        bbox_data = json.load(f)
    
    with open(mask_path, 'r') as f:
        mask_data = json.load(f)

    # open the info file
    with open(info_file, 'r') as f:
        info = json.load(f)
    
    # concatenate the annotations
    annotations = mask_data

    for i in range(len(mask_data)):
        annotations[i]['bbox'] = mask_data[i]['bbox']
    
    
    



