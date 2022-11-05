
data for yolo 700 - v4 2022-11-01 12:25pm
==============================

This dataset was exported via roboflow.com on November 1, 2022 at 3:27 AM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

It includes 698 images.
Yoloheejun01 are annotated in YOLO v5 PyTorch format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 416x416 (Stretch)
* Grayscale (CRT phosphor)

The following augmentation was applied to create 1 versions of each source image:
* 50% probability of horizontal flip
* 50% probability of vertical flip
* Equal probability of one of the following 90-degree rotations: none, clockwise, counter-clockwise, upside-down
* Randomly crop between 0 and 25 percent of the image
* Random rotation of between -15 and +15 degrees
* Random shear of between -15° to +15° horizontally and -15° to +15° vertically
* Random Gaussian blur of between 0 and 2 pixels


