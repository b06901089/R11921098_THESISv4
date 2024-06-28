import argparse
import cv2
import numpy as np
import torch
import os

from torch import nn
from torchvision.io import read_image

parser = argparse.ArgumentParser()
parser.add_argument('--gt', type=str)
parser.add_argument('--sr', type=str)
parser.add_argument('--txt', type=str)
args = parser.parse_args()

with open(args.txt, 'a') as f:
    if args.sr.split('/')[-1] != '':
        sr_method = args.sr.split('/')[-1]
    else:
        sr_method = args.sr.split('/')[-2]
    f.write(f'{sr_method}:\n')

avg_psnr = 0
count = 0

gt_sub_dirs = sorted(os.listdir(args.gt))
sr_sub_dirs = sorted(os.listdir(args.sr))

assert len(gt_sub_dirs) == len(sr_sub_dirs)

for gt_sub, sr_sub in zip(gt_sub_dirs, sr_sub_dirs):

    # print(gt_sub, sr_sub)

    gt_sub = os.path.join(args.gt, gt_sub)
    sr_sub = os.path.join(args.sr, sr_sub)

    gt_sub_imgs = sorted(os.listdir(gt_sub))
    sr_sub_imgs = sorted(os.listdir(sr_sub))

    if len(gt_sub_imgs) != len(sr_sub_imgs):
        # print(gt_sub, sr_sub)
        # print('length:', len(gt_sub_imgs), len(sr_sub_imgs))
        with open(args.txt, 'a') as f:
            f.write('{}, {}\n'.format(gt_sub, sr_sub))
            f.write('length: {}, {}\n'.format(len(gt_sub_imgs), len(sr_sub_imgs)))

    # assert len(gt_sub_imgs) == len(sr_sub_imgs)

    for gt_img, sr_img in zip(gt_sub_imgs, sr_sub_imgs):

        gt_img = cv2.imread(os.path.join(gt_sub, gt_img))
        sr_img = cv2.imread(os.path.join(sr_sub, sr_img))

        sqaure_dif = (gt_img - sr_img) ** 2
        mse = np.mean(sqaure_dif)
        psnr = 10 * np.log10(255 ** 2 / mse)
        avg_psnr = avg_psnr + psnr
        count = count + 1

# print(avg_psnr/count)
with open(args.txt, 'a') as f:
    f.write('frame count: {}\n'.format(count))
    f.write('average PSNR: {}\n'.format(avg_psnr/count))
    f.write('\n')