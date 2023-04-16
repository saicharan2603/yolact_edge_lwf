from utils.extract_subset import extract_subset


valPath = './data/coco/annotations/instances_val2017.json'
trainPath = './data/coco/annotations/instances_train2017.json'

dumpValPath = './data/coco/annotations/instances_val2017_subset.json'
dumpTrainPath = './data/coco/annotations/instances_train2017_subset.json'

categories = [62, 79] # chair and oven

extract_subset(valPath, dumpValPath, categories)
# extract_subset(trainPath, dumpTrainPath, categories)

