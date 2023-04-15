import json

def extract_subset(file_path, dump_path, categories):
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
            annotations.append(annotation)

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
    subset['categories'] = data['categories']

    with open(dump_path, 'w') as f:
        json.dump(subset, f)
    
    # print the report of extraction
    print('Number of images extracted: ', len(images))
    print('Subset dumped at: ', dump_path)
    
    

