# YolactEdge with LwF: Real-time Instance Segmentation on the Edge with Learning without Forgetting
```
██╗   ██╗ ██████╗ ██╗      █████╗  ██████╗████████╗    ███████╗██████╗  ██████╗ ███████╗    ██╗                  ███████╗
╚██╗ ██╔╝██╔═══██╗██║     ██╔══██╗██╔════╝╚══██╔══╝    ██╔════╝██╔══██╗██╔════╝ ██╔════╝    ██║   ██╗   ██╗   ██╗██╔════╝
 ╚████╔╝ ██║   ██║██║     ███████║██║        ██║       █████╗  ██║  ██║██║  ███╗█████╗      ██║   ╚██╗ ████╗ ██╔╝█████╗
  ╚██╔╝  ██║   ██║██║     ██╔══██║██║        ██║       ██╔══╝  ██║  ██║██║   ██║██╔══╝      ██║    ╚████╔═████╔╝ ██╔══╝
   ██║   ╚██████╔╝███████╗██║  ██║╚██████╗   ██║       ███████╗██████╔╝╚██████╔╝███████╗    ███████╗╚██╔╝ ╚██╔╝  ██║
   ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝   ╚═╝       ╚══════╝╚═════╝  ╚═════╝ ╚══════╝    ╚══════╝ ╚═╝   ╚═╝   ╚═╝
```

To evalute the model, put the corresponding weights file in the `./weights` directory and run one of the following commands.

weights:

|Model| &nbsp;&nbsp;&nbsp;Backbone&nbsp;&nbsp;&nbsp;&nbsp; | weights |
|:-------------:|:----:|----------------------------------------------------------------------------------------------------------------------|
| COCO base model | R-101-FPN | [download](https://drive.google.com/file/d/1EAzO-vRDZ2hupUJ4JFSUi40lAZ5Jo-Bp/view?usp=sharing) \| [mirror](https://1drv.ms/u/s!AkSxI62eEcpbiG8nFXtvgAkI-c1H?e=HyfH8Z) |
| LwF model | R-101-FPN | [download](https://iitk-my.sharepoint.com/:f:/g/personal/saicharanm22_iitk_ac_in/EsLAKkKDZz9Lg4VaLNhgbSwBB10cCDqATvk6GWG54CE9xw?e=KVIGYQ)

## Installation

See [INSTALL.md](INSTALL.md).

## Getting Started

Follow the [installation instructions](INSTALL.md) to set up required environment for running YolactEdge.

See instructions to [evaluate](https://github.com/haotian-liu/yolact_edge#evaluation) and [train](https://github.com/haotian-liu/yolact_edge#training) with YolactEdge LwF.

## Checkout `evaluation.ipynb` to run the evaluation

## Evaluation of lwf-model on old and new datasets

```Shell
# Evaluate on the entire COCO validation set before new task.
python3 eval.py --trained_model=./weights/yolact_edge_54_800000.pth --score_threshold=0.3 --top_k=100 --disable_tensorrt

# Evaluate on the lvis validation set for lwf model performance on new task.
!python3 eval.py --trained_model=weights/yolact_edge_lvis_lwf.pth --score_threshold=0.3 --config=yolact_edge_lvis_config_lwf  --disable_tensorrt

# Evaluate on the coco validation set for lwf model performance on old tasks.
!python3 eval.py --trained_model=weights/yolact_edge_lvis_lwf.pth --score_threshold=0.3 --config=yolact_edge_config_lwf  --disable_tensorrt
```

### Notes
If you want to use TensorRT optimization for realtime inference, then remove `--disable_tensorrt` option from the above code.
- Calibration is only required if you are using TensorRT optimization. 
#### Handling inference error when using TensorRT
If you are using TensorRT conversion of YolactEdge and encountered issue in PostProcessing or NMS stage, this might be related to TensorRT engine issues. We implemented a experimental safe mode that will handle these cases carefully. Try this out with `--use_tensorrt_safe_mode` option in your command. 



#### Inference without Calibration

If you want to run inference command without calibration, you can either run with FP16-only TensorRT optimization, or without TensorRT optimization with corresponding configs. Refer to `data/config.py` for examples of such configs.

```Shell
# Evaluate YolactEdge with FP16-only TensorRT optimization with '--use_fp16_tensorrt' option (replace all INT8 optimization with FP16).
python3 eval.py --use_fp16_tensorrt --trained_model=./weights/yolact_edge_54_800000.pth

# Evaluate YolactEdge without TensorRT optimization with '--disable_tensorrt' option.
python3 eval.py --disable_tensorrt --trained_model=./weights/yolact_edge_54_800000.pth
```

Use the help option to see a description of all available command line arguments:
```Shell
python eval.py --help
```


## Training

### Preproessing the Data for LwF
- Download the LVIS dataset train and validation annotations from [here](https://www.lvisdataset.org/dataset) and extract it in the `./data/LVIS/annotations` directory.
- Create a subset for new task by running the `yolact_edge_lwf/create_subset.py` script. Edit the script to extract the required subset of classes.
- run `yolact_edge_lwf/remove_annotations.py` script to create un annotated files for the new task.
- edit the `yolact_edge_lwf/config.py` file to change the number of classes and the class names. also add the required configurations for the new task.
- execute the following commands to infer the new task on the un annotated files.
```Shell
python3 eval.py --trained_model=./weights/yolact_edge_54_800000.pth --score_threshold=0.3 --disable_tensorrt --config=yolact_edge_config_lwf --output_coco_json
```
- the above command will generate a `mask.json` and `bbox.json` files in the `./results` directory.

- run the `yolact_edge_lwf\utils\concatenate.py` file by modifying the main method to get the concatenated file for training with LwF.

```Shell
# Resume training yolact_edge with a specific weight file and start from the iteration specified in the weight file's name.
python train.py --config=yolact_edge_lvis_config_lwf --resume=weights/yolact_edge_54_800000.pth

# Use the help option to see a description of all available command line arguments
python train.py --help
```

### Custom Datasets
You can also train on your own dataset by following these steps:
 - Depending on the type of your dataset, create a COCO-style (image) or YTVIS-style (video) Object Detection JSON annotation file for your dataset. The specification for this can be found here for [COCO](http://cocodataset.org/#format-data) and [YTVIS](https://github.com/youtubevos/cocoapi) respectively. Note that we don't use some fields, so the following may be omitted:
   - `info`
   - `liscense`
   - Under `image`: `license, flickr_url, coco_url, date_captured`
   - `categories` (we use our own format for categories, see below)
 - Create a definition for your dataset under `dataset_base` in `data/config.py` (see the comments in `dataset_base` for an explanation of each field):
```Python
my_custom_dataset = dataset_base.copy({
    'name': 'My Dataset',

    'train_images': 'path_to_training_images',
    'train_info':   'path_to_training_annotation',

    'valid_images': 'path_to_validation_images',
    'valid_info':   'path_to_validation_annotation',

    'has_gt': True,
    'class_names': ('my_class_id_1', 'my_class_id_2', 'my_class_id_3', ...),

    # below is only needed for YTVIS-style video dataset.

    # whether samples all frames or key frames only.
    'use_all_frames': False,

    # the following four lines define the frame sampling strategy for the given dataset.
    'frame_offset_lb': 1,
    'frame_offset_ub': 4,
    'frame_offset_multiplier': 1,
    'all_frame_direction': 'allway',

    # 1 of K frames is annotated
    'images_per_video': 5,

    # declares a video dataset
    'is_video': True
})
```
 - Note that: class IDs in the annotation file should start at 1 and increase sequentially on the order of `class_names`. If this isn't the case for your annotation file (like in COCO), see the field `label_map` in `dataset_base`.
 - Finally, in `yolact_edge_config` in the same file, change the value for `'dataset'` to `'my_custom_dataset'` or whatever you named the config object above and `'num_classes'` to number of classes in your dataset+1. Then you can use any of the training commands in the previous section.
 
