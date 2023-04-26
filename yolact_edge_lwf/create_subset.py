from utils.extract_subset import extract_subset


# valPath = './data/coco/annotations/instances_val2017.json'
# trainPath = './data/coco/annotations/instances_train2017.json'

trainPath = './data/LVIS/annotations/lvis_v1_train.json'
valPath = './data/LVIS/annotations/lvis_v1_val.json'

categories = [2] # air conditioner

extract_subset(valPath, categories)
extract_subset(trainPath, categories)

