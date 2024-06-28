import os
import cv2
import argparse
import numpy as np

parser = argparse.ArgumentParser()

parser.add_argument('--img_dir', type=str)
parser.add_argument('--out_dir', type=str)

args = parser.parse_args()

img_dir = args.img_dir
out_dir = args.out_dir

if not os.path.isdir(out_dir):
    os.makedirs(out_dir)

imgs = sorted(os.listdir(img_dir))

for i in imgs:
    img = cv2.imread(os.path.join(img_dir, i))
    img = cv2.resize(img, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(os.path.join(out_dir, i), img)