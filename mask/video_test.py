
import mrcnn
import mrcnn.config
import mrcnn.model
import mrcnn.visualize
import cv2
import os
import cv2
import numpy as np
import os
import sys

from mrcnn import utils
from mrcnn import model as modellib



MODEL_DIR = "C:/Users/Admin/anaconda3/envs/test/Mask_RCNN/mask_rcnn_object_0002.h5"

class_names =  ['BG', 'descending life line', 'fire extinguisher']
class SimpleConfig(mrcnn.config.Config):
    # Give the configuration a recognizable name
    NAME = "coco_inference"
    
    # set the number of GPUs to use along with the number of images per GPU
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

	# Number of classes = number of classes + 1 (+1 for the background). The background class is named BG
    NUM_CLASSES = len(class_names)




config = SimpleConfig()
config.display()

model = modellib.MaskRCNN(
    mode="inference", model_dir=MODEL_DIR, config=SimpleConfig()
)
model.load_weights(MODEL_DIR, by_name=True)




def random_colors(N):
    np.random.seed(1)
    colors = [tuple(255 * np.random.rand(3)) for _ in range(N)]
    return colors


colors = random_colors(len(class_names))
class_dict = {
    name: color for name, color in zip(class_names, colors)
}


def apply_mask(image, mask, color, alpha=0.5):
    """apply mask to image"""
    for n, c in enumerate(color):
        image[:, :, n] = np.where(
            mask == 1,
            image[:, :, n] * (1 - alpha) + alpha * c,
            image[:, :, n]
        )
    return image


def display_instances(image, boxes, masks, ids, names, scores):
    """
        take the image and results and apply the mask, box, and Label
    """
    n_instances = boxes.shape[0]

    if not n_instances:
        print('NO INSTANCES TO DISPLAY')
    else:
        assert boxes.shape[0] == masks.shape[-1] == ids.shape[0]

    for i in range(n_instances):
        if not np.any(boxes[i]):
            continue

        y1, x1, y2, x2 = boxes[i]
        label = names[ids[i]]
        color = class_dict[label]
        score = scores[i] if scores is not None else None
        caption = '{} {:.2f}'.format(label, score) if score else label
        mask = masks[:, :, i]

        image = apply_mask(image, mask, color)

        image = cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
        image = cv2.putText(
            image, caption, (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 0.7, color, 2
        )

    return image


if __name__ == '__main__':
    """
        test everything
    """

    capture = cv2.VideoCapture("C:/Users/Admin/anaconda3/envs/test/Mask_RCNN/4???.mp4")

    # these 2 lines can be removed if you dont have a 1080p camera.
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 720) #1920
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) #1080
    frame_width = int(capture.get(3))
    frame_height = int(capture.get(4))
    out = cv2.VideoWriter('4???.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))


    while True:
        ret, frame = capture.read()
        frame = cv2.flip(frame,0)
        results = model.detect([frame], verbose=0)
        r = results[0]
        frame = display_instances(
            frame, r['rois'], r['masks'], r['class_ids'], class_names, r['scores']
        )
 #       frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
        
        cv2.imshow('frame', frame)
        out.write(frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

