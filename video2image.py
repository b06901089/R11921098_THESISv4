import argparse
import cv2
import os

parser = argparse.ArgumentParser()

parser.add_argument('--start', type=int, default=1)
parser.add_argument('--end', type=int, default=1)

parser.add_argument('--inter', type=str, default=None)
parser.add_argument('--res', type=str, default=None)
parser.add_argument('--name', type=str, default=None)
parser.add_argument('--log', type=str, default=None)
args = parser.parse_args()

resolution_map = {
    '4K':   [3840, 2160],
    '2K':   [2560, 1440],
    '1080p':[1920, 1080],
    '720p': [1280, 720],
    '540p': [960, 540],
    '360p': [640, 360],
    '270p': [480, 270],
    '180p': [320, 180],
}

resolutions = {}

if args.res in resolution_map:
    resolutions[args.name] = resolution_map[args.res]
else:
    print('Error: Incorrect Parameter (resolution) Settings!')
    with open(p['log_name'], 'a') as f:
        f.write('Error: Incorrect Parameter (resolution) Settings!\n')

for key in resolutions.keys():

    if not os.path.isdir(os.path.join(args.inter, 'Inter4K_frame/60fps/{}'.format(key))):
        os.makedirs(os.path.join(args.inter, 'Inter4K_frame/60fps/{}'.format(key)))

    for i in range(args.start, args.end+1):
        in_file = os.path.join(args.inter, 'Inter4K/60fps/{}/{}.mp4'.format(key, i))
        out_dir = os.path.join(args.inter, 'Inter4K_frame/60fps/{}/{}'.format(key, i))

        if not os.path.isdir(out_dir):
            os.makedirs(out_dir)

        videoCapture = cv2.VideoCapture(in_file)
        fps = videoCapture.get(cv2.CAP_PROP_FPS)
        size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        fNUMS = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
 

        count = 0
        write = True
        success, frame = videoCapture.read()
        while success:
            if write:
                cv2.imwrite(os.path.join(out_dir, '{:04d}.png'.format(count)), frame)
                # write = False
            else:
                write = True
            success, frame = videoCapture.read()
            count = count + 1
 
        videoCapture.release()



# for i in [100]:
#     in_file = 'UHD_{}.mp4'.format(i)
#     out_dir = 'UHD_{}'.format(i)
    
#     if not os.path.isdir(out_dir):
#         os.makedirs(out_dir)

#     videoCapture = cv2.VideoCapture(in_file)
#     fps = videoCapture.get(cv2.CAP_PROP_FPS)
#     size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
#     fNUMS = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)


#     count = 0
#     write = True
#     success, frame = videoCapture.read()
#     while success:
#         if write:
#             cv2.imwrite(os.path.join(out_dir, '{:04d}.png'.format(count)), frame)
#             # write = False
#         else:
#             write = True
#         success, frame = videoCapture.read()
#         count = count + 1

#     videoCapture.release()
