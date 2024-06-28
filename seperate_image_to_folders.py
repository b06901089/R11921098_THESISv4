import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--img_dir', type=str)
parser.add_argument('--out_dir', type=str)
parser.add_argument('--image_per_folder', type=int)

args = parser.parse_args()

img_dir = args.img_dir
out_dir = args.out_dir

if not os.path.isdir(out_dir):
    os.makedirs(out_dir)

images = sorted(os.listdir(img_dir))

image_per_folder = args.image_per_folder
sub_folder_idx = 1
image_count = 0

for i in range(len(images)):

    sub_folder_path = os.path.join(out_dir, '{:02d}'.format(sub_folder_idx))
    if not os.path.isdir(sub_folder_path):
        os.makedirs(sub_folder_path)

    os.system('cp {} {}'.format(os.path.join(img_dir, images[i]), os.path.join(sub_folder_path, '{:04d}.png'.format(image_count))))

    image_count = image_count + 1
    if image_count >= image_per_folder:
        image_count = 0
        sub_folder_idx = sub_folder_idx + 1