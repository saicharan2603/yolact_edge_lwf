import json
import os

def extract_subset(file_path, categories):
    """Read the json file and extract the subset of images that belong to the
    specified categories.

    Args:
        file_path: Path to the json file.
        categories: List of category id's to extract.

    """

    # Read the coco json file
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Extract the image_ids that belong to the specified categories
    image_ids = []
    for annotation in data['annotations']:
        if annotation['category_id'] in categories:
            image_ids.append(annotation['image_id'])
    
    # Remove duplicate image_ids
    image_ids = list(set(image_ids))

    # Extract the annotations that belong to the specified categories
    annotations = []
    for annotation in data['annotations']:
        if annotation['image_id'] in image_ids:
            if annotation['category_id'] in categories:
                annotation['category_id'] = categories.index(annotation['category_id']) + 1
                annotations.append(annotation)

    # extract the categories
    category_list = []
    for category in data['categories']:
        if category['id'] in categories:
            category['id'] = categories.index(category['id']) + 1
            category_list.append(category)

    # Extract the images that belong to the specified categories
    images = []
    for image in data['images']:
        if image['id'] in image_ids:
            images.append(image)
    
    # dump the subset
    subset = {}
    subset['info'] = data['info']
    subset['licenses'] = data['licenses']
    subset['images'] = images
    subset['annotations'] = annotations
    subset['categories'] = category_list

    dump_path = os.path.splitext(file_path)[0]+'_subset.json'

    with open(dump_path, 'w') as f:
        json.dump(subset, f)
    
    # print the report of extraction
    print('Number of images extracted: ', len(images))
    print('Number of annotations extracted: ', len(annotations))
    print('Number of categories extracted: ', len(categories))
    print('Subset dumped at: ', dump_path)
    
    

