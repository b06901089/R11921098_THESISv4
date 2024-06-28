import argparse
import torch
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import math
from collections import defaultdict

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--img_dir', type=str)

    args = parser.parse_args()

    # Video Index (include start and end)
    start = 1
    end = 100

    # Model
    model = torch.hub.load("ultralytics/yolov5", "yolov5x6")

    # Data
    GT_folder = args.img_dir

    # Storage
    d = defaultdict(list)

    # Get image size sample (video resolution)
    FR_folder = os.path.join(GT_folder, str(start))
    images = sorted(os.listdir(FR_folder))
    idx = images[0]
    img = cv2.imread(os.path.join(FR_folder, idx))[..., ::-1]
    (img_h, img_w, img_c) = img.shape

    # Image size catagory (percentage)
    small = 1/3
    medium = 3

    # Iterate through every single videos
    for vid in range(start, end+1):

        # print(vid)

        # # Storage
        # d = defaultdict(list)

        FR_folder = os.path.join(GT_folder, str(vid))

        images = sorted(os.listdir(FR_folder))

        for idx in images:

            img = cv2.imread(os.path.join(FR_folder, idx))[..., ::-1]
            results = model(img)

            for i in range(results.xyxy[0].shape[0]):

                detection = results.xyxy[0][i]

                # class x_min, y_min, x_max, y_max
                size = (detection[2] - detection[0]) * (detection[3] - detection[1])
                # get normalized area
                normalized_size = size.item() / (img_h * img_w)
                # get rounded percentage
                normalized_size = round(normalized_size, 3) * 100

                if normalized_size < small:
                    d[detection[5].item()].append(0)
                elif normalized_size < medium:
                    d[detection[5].item()].append(1)
                else:
                    d[detection[5].item()].append(2)


    # Get count for each size
    count_list = [0] * 3

    for keys in d:
        for val in d[keys]:
            count_list[int(val)] += 1

    x = ['S', 'M', 'L']
    y = count_list

    plt.bar(x, y)
    plt.xlabel('Size')
    plt.ylabel('Number')
    plt.title(f'object size distribution for {img_h}p')
    plt.savefig(f'plot/ob_dis_{img_h}p.png', dpi=200, transparent=True)
    plt.clf()

    # Write txt
    with open(f'plot/ob_dis_{img_h}p.txt', 'w') as f:
        for cat, count in zip(x, y):
            f.write(f'{cat}, {count}\n')

    # Get class name
    name = []
    with open('coco-classes.txt') as f:
        for line in f.readlines():
            name.append(line[:-1])

    # Get count for each class
    count_list = [0] * 80

    for keys in d:
        count_list[int(keys)] = len(d[keys])

    # x = [*range(1, 81, 1)]
    x = name
    y = count_list

    plt.bar(x, y)
    plt.xticks(x, rotation=45, fontsize=3, ha='right')
    plt.xlabel('Class')
    plt.ylabel('Number')
    plt.title(f'object class distribution for {img_h}p')
    plt.savefig(f'plot/cl_dis_{img_h}p.png', dpi=800, transparent=True)
    plt.clf()

    # Write txt
    with open(f'plot/cl_dis_{img_h}p.txt', 'w') as f:
        for cat, count in zip(x, y):
            f.write(f'{cat}, {count}\n')
