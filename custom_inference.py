# python custom_inference.py && cd mAP && python main.py -na -np && cd ..

import argparse
import torch
import cv2
import os
import numpy as np

parser = argparse.ArgumentParser()

parser.add_argument('--gt_dir', type=str)
parser.add_argument('--sr_dir', type=str)
parser.add_argument('--nogt', type=bool, default=False)
parser.add_argument('--scale', type=bool, default=False)

args = parser.parse_args()

GT_folder = args.gt_dir
SR_folder = args.sr_dir

# Model
model = torch.hub.load("ultralytics/yolov5", "yolov5x6")  # or yolov5n - yolov5x6, custom

# Images
GT_images = sorted(os.listdir(GT_folder))
SR_images = sorted(os.listdir(SR_folder))
assert len(GT_images) == len(SR_images)

for gt, sr in zip(GT_images, SR_images):

    assert gt == sr

# Inference
GT_output = './mAP/input/ground-truth/'
SR_output = './mAP/input/detection-results/'

if not args.nogt:
     
    os.system('rm -f {}*txt'.format(GT_output))
    for gt in GT_images:

        gt_img = cv2.imread(os.path.join(GT_folder, gt))[..., ::-1]
        results = model(gt_img)

        txt_path = os.path.join(GT_output, gt[:-3]+'txt')
        f = open(txt_path, 'w')

        for i in range(results.xyxy[0].shape[0]):

            detection = results.xyxy[0][i]
            f.write('{} {} {} {} {}\n'.format(detection[5], detection[0], detection[1], detection[2], detection[3]))


        f.close()

os.system('rm -f {}*txt'.format(SR_output))
for sr in SR_images:

    sr_img = cv2.imread(os.path.join(SR_folder, sr))[..., ::-1]
    results = model(sr_img)

    txt_path = os.path.join(SR_output, sr[:-3]+'txt')
    f = open(txt_path, 'w')

    for i in range(results.xyxy[0].shape[0]):

        detection = results.xyxy[0][i]

        if not args.scale:
            f.write('{} {} {} {} {} {}\n'.format(detection[5], detection[4], detection[0], detection[1], detection[2], detection[3]))
        else: 
            f.write('{} {} {} {} {} {}\n'.format(detection[5], detection[4], detection[0]*4, detection[1]*4, detection[2]*4, detection[3]*4))

    f.close()