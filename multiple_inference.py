import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--img_dir', type=str)
parser.add_argument('--out_dir', type=str)

args = parser.parse_args()

img_dir = args.img_dir
out_dir = args.out_dir

sub_dirs = sorted(os.listdir(img_dir))

for sub_dir in sub_dirs:

    output_sub = os.path.join(out_dir, sub_dir)
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    input_sub = os.path.join(img_dir, sub_dir)

    cmd =   'python \
            BasicVSR_PlusPlus/demo/restoration_video_demo.py \
            BasicVSR_PlusPlus/configs/basicvsr_plusplus_reds4.py \
            BasicVSR_PlusPlus/chkpts/basicvsr_plusplus_c64n7_8x1_600k_reds4_20210217-db622b2f.pth \
            {} \
            {} \
            --filename-tmpl {{:04d}}.png \
            --max-seq-len 15'.format(input_sub, output_sub)

    os.system(cmd)

###

sub_dirs = sorted(os.listdir(out_dir))

count = 0

for sub_dir in sub_dirs:

    images_dir = os.path.join(out_dir, sub_dir)
    
    images = sorted(os.listdir(images_dir))

    for image in images:

        os.system('mv {} {}'.format(os.path.join(images_dir, image), os.path.join(out_dir, '{:04d}.png'.format(count))))

        count = count + 1

    os.system('rm -rf {}'.format(os.path.join(out_dir, sub_dir)))