import json
import os

def remove_annotations(file_path, categories):
    """Read the json file and extract the subset of images that belong to the
    specified categories.

    Args:
        file_path: Path to the json file.
        categories: List of category id's to extract.

    """

    # Read the coco json file
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # dump the subset
    subset = {}
    subset['info'] = data['info']
    subset['licenses'] = data['licenses']
    subset['images'] = data['images']
    subset['categories'] = data['categories']

    dump_path = os.path.splitext(file_path)[0]+'_unannotated.json'

    with open(dump_path, 'w') as f:
        json.dump(subset, f)
    