import json
import os

def generate_concatenated_info_file(bbox_path, mask_path, info_file):

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
        annotations[i]['bbox'] = bbox_data[i]['bbox']
    
    # update the info file
    info['annotations'].extend(annotations)

    for i in range(len(info['annotations'])):
        info['annotations'][i]['id'] = i + 1
    

    # write the info file
    with open(os.path.splitext(info_file)[0]+'_lwf.json', 'w') as f:
        json.dump(info, f)

if __name__ == '__main__':
    generate_concatenated_info_file('./results/bbox_detections.json', './results/mask_detections.json', './data/LVIS/annotations/lvis_v1_val_subset.json')
    



