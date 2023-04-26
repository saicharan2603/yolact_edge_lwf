import json
import os

def extract_subset2(file_path, coco_path):
    """Read the json file and extract the subset of images that belong to the
    specified categories.

    Args:
        file_path: Path to the json file.
        categories: List of category id's to extract.

    """

    # Read the coco json file
    with open(coco_path, 'r') as f:
        coco_data = json.load(f)
    
    # Read the coco json file
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Extract the image_ids that belong to the specified categories
    image_ids = []
    for image in coco_data['images'][:10000]:
            image_ids.append(image['id'])

    for image in data['images']:
            image_ids.append(image['id'])
    
    # Remove duplicate image_ids
    image_ids = list(set(image_ids))

    # Extract the annotations that belong to the specified categories
    annotations = []
    for annotation in coco_data['annotations']:
        if annotation['image_id'] in image_ids:
            annotations.append(annotation)

    for annotation in data['annotations']:
        annotations.append(annotation)

    # Extract the images that belong to the specified categories
    images = []
    for image in coco_data['images']:
        if image['id'] in image_ids:
            images.append(image)
    
    # dump the subset
    subset = {}
    subset['info'] = data['info']
    subset['licenses'] = data['licenses']
    subset['images'] = images
    subset['annotations'] = annotations
    subset['categories'] = data['categories']

    dump_path = os.path.splitext(file_path)[0]+'_subset.json'

    with open(dump_path, 'w') as f:
        json.dump(subset, f)
    
    # print the report of extraction
    print('Number of images extracted: ', len(images))
    print('Number of annotations extracted: ', len(annotations))
    print('Subset dumped at: ', dump_path)

import json
import os

def extract_subset(file_path, coco_path):
    """Read the json file and extract the subset of images that belong to the
    specified categories.

    Args:
        file_path: Path to the json file.
        categories: List of category id's to extract.

    """

    # Read the coco json file
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    with open(coco_path, 'r') as f:
        coco_data = json.load(f)

    image_ids = []
    for image in data['images']:
        image_ids.append(image['id'])

    annotations = data['annotations']

    for annotation in coco_data['annotations']:
        if annotation['image_id'] in image_ids:
            annotations.append(annotation)
    
    # dump the subset
    subset = {}
    subset['info'] = data['info']
    subset['licenses'] = data['licenses']
    subset['images'] = data['images']
    subset['annotations'] = annotations
    subset['categories'] = data['categories']

    dump_path = os.path.splitext(file_path)[0]+'_comb_ann.json'

    with open(dump_path, 'w') as f:
        json.dump(subset, f)
    
    # print the report of extraction
    print('Number of images extracted: ', len(subset['images']))
    print('Number of annotations extracted: ', len(annotations))
    print('Number of categories extracted: ', len(subset['categories']))
    print('Subset dumped at: ', dump_path)

extract_subset('data/LVIS/annotations/lvis_v1_val_subset.json', 'data/coco/annotations/instances_val2017.json')
extract_subset('data/LVIS/annotations/lvis_v1_train_subset.json', 'data/coco/annotations/instances_train2017.json')