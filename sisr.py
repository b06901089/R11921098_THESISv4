import os
import cv2
import argparse
import numpy as np
import torch
import pathlib

from torch import nn
from fsrcnn.fsrcnn_model import FSRCNN

parser = argparse.ArgumentParser()

parser.add_argument('--img_dir', type=str)
parser.add_argument('--out_dir', type=str)

args = parser.parse_args()

my_device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
sr_model_4x = FSRCNN(4).to(my_device)
checkpoints = torch.load('fsrcnn/fsrcnn_x4-T91-97a30bfb.pth.tar', map_location=lambda storage, loc: storage)
sr_model_4x.load_state_dict(checkpoints['state_dict'])
sr_model_4x.eval()
sr_model_4x.half()

import imgproc
def RGBimg2srRGBimg_4x(img):

    lr_image = img.astype(np.float32) / 255.0
    lr_ycbcr_image = imgproc.bgr2ycbcr(lr_image, use_y_channel=False)
    lr_y_image, lr_cb_image, lr_cr_image = cv2.split(lr_ycbcr_image)
    lr_y_tensor = imgproc.image2tensor(lr_y_image, range_norm=False, half=True).to(my_device).unsqueeze_(0)
    with torch.no_grad():
        sr_y_tensor = sr_model_4x(lr_y_tensor).clamp_(0, 1.0)
    sr_y_image = imgproc.tensor2image(sr_y_tensor, range_norm=False, half=True)
    sr_y_image = sr_y_image.astype(np.float32) / 255.0
    hr_cb_image = cv2.resize(lr_cb_image, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
    hr_cr_image = cv2.resize(lr_cr_image, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
    sr_ycbcr_image = cv2.merge([sr_y_image, hr_cb_image, hr_cr_image])
    sr_image = imgproc.ycbcr2bgr(sr_ycbcr_image)
    sr_image *= 255.0
    return sr_image

img_dir = args.img_dir
out_dir = args.out_dir

p = pathlib.Path(out_dir)
p.mkdir(parents=True, exist_ok=True)

imgs = sorted(os.listdir(img_dir))

for i in imgs:
    img = cv2.imread(os.path.join(img_dir, i))
    img = RGBimg2srRGBimg_4x(img)
    cv2.imwrite(os.path.join(out_dir, i), img)