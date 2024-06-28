import argparse
import os
import glob
from multiprocessing import Pool
import time

resolution_map = {
    '4K':   [3840, 2160],
    '2K':   [2560, 1440],
    '1440p':[2560, 1440],
    '1080p':[1920, 1080],
    '720p': [1280, 720],
    '540p': [960, 540],
    '360p': [640, 360],
    '270p': [480, 270],
    '180p': [320, 180],
}

def transcode(param):

    filename = param[0]
    name = param[1]
    width = param[2]
    height = param[3]
    FPS_path = param[4]
    UHD_path = param[5]
    args = param[6]

    preset = 'medium'

    if not os.path.isdir(os.path.join(args.inter, f'Inter4K/60fps/{name}')):
        os.makedirs(os.path.join(args.inter, f'Inter4K/60fps/{name}'), exist_ok=True)
    if os.path.isfile(os.path.join(args.inter, f'Inter4K/60fps/{name}/{filename}')):
        print('Error: Files with same names already exist, please remove them and try it again!')
        return
    
    if args.crf != -1:
        os.system(f'ffmpeg -i {UHD_path}/{filename} -c:v libx264 -preset {preset} -vf scale={width}:{height} -crf {args.crf} ../../Datasets/Inter4K/Inter4K/60fps/{name}/{filename}')
    elif args.qp != -1:
        os.system(f'ffmpeg -i {UHD_path}/{filename} -c:v libx264 -preset {preset} -vf scale={width}:{height} -qp {args.qp} ../../Datasets/Inter4K/Inter4K/60fps/{name}/{filename}')
    else:
        print('Error: Incorrect Parameter Settings!')

parser = argparse.ArgumentParser()
parser.add_argument('--crf', type=int, default=-1)
parser.add_argument('--qp', type=int, default=-1)
parser.add_argument('--start', type=int, default=1)
parser.add_argument('--end', type=int, default=1)

parser.add_argument('--inter', type=str, default=None)
parser.add_argument('--res', type=str, default=None)
parser.add_argument('--name', type=str, default=None)
parser.add_argument('--log', type=str, default=None)
args = parser.parse_args()

resolutions = {}
if args.res in resolution_map:
    resolutions[args.name] = resolution_map[args.res]
else:
    print('Error: Incorrect Parameter (resolution) Settings!')
    with open(args.log, 'a') as f:
        f.write('Error: Incorrect Parameter (resolution) Settings!\n')

FPS_path = os.path.join(args.inter, 'Inter4K/60fps')
UHD_path = os.path.join(FPS_path, 'UHD')
raw_path = os.path.join(UHD_path, '*.mp4')

start_time = time.time()
for file in glob.glob(raw_path):
    filename = file.split('/')[-1]

    if int(filename.split('.')[0]) >= args.start and int(filename.split('.')[0]) <= args.end:

        targets = [[filename, 
                    key, 
                    resolutions[key][0], 
                    resolutions[key][1], 
                    FPS_path, 
                    UHD_path,
                    args,] for key in resolutions.keys()]

        with Pool(16) as p:
            print(p.map(transcode, targets))
end_time = time.time()
with open(args.log, 'a') as f:
    f.write("execution time for video transcode: %s seconds " % (end_time - start_time))