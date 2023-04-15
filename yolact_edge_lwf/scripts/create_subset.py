from yolact_edge_lwf.utils.extract_subset import extract_subset

valPath = './annotations/instances_val2017.json'
trainPath = './annotations/instances_train2017.json'

dumpValPath = './annotations/instances_val2017_subset.json'
dumpTrainPath = './annotations/instances_train2017_subset.json'

categories = [62, 79] # chair and oven

extract_subset(valPath, dumpValPath, categories)
extract_subset(trainPath, dumpTrainPath, categories)

