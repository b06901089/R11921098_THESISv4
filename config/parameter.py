# Detail explanation of other example json files
# Only 4x SR ratio is supported
# i.e. (4K, 540p), (2K, 360p), (1080p, 270p), (720p, 180p)

# resolution_map = {
#     '4K':   [3840, 2160],
#     '2K':   [2560, 1440],
#     '1080p':[1920, 1080],
#     '720p': [1280, 720],
#     '540p': [960, 540],
#     '360p': [640, 360],
#     '270p': [480, 270],
#     '180p': [320, 180],
# }

# Get Ground Truth
p = {

    'mode':     'Get Ground Truth',
    # There are mainly four modes
    #    'Get Ground Truth'
    #        get uncompressed high-resolution video and video frames
    #    'Get Low Quality'
    #        get compressed high-resolution video and video frames
    #    'Get High Quality'
    #        get compressed low-resolution video and video frames
    #    'Inference'
    #        Combination of the previous three modes
    'log':      './My_log',
    # Path to saved the logs
    'source':   '/home/aaron/miniconda3/etc/profile.d/conda.sh',
    # Path to source conda.sh
    'start':    1,
    # Start index of inference videos (1~1000)
    'end':      1,
    # End (include) index of inference videos (1~1000), End >= Start
    'crf':      0,
    # Set CRF to 0~51, should be set to 0 when generating ground truth videos. Otherwise, set to '-1' if you want to use CQP.
    'qp':       -1,
    # Set CQP to 0~51, should be set to 0 when generating ground truth videos. Otherwise, set to '-1' if you want to use CRF.
    'inter':    '../../Datasets/Inter4K',
    # Path to Root Inter4K folder
    # The structure of the folder should look like this:
    # Inter4K/
    #   Inter4K/
    #       60fps/
    #           UHD/
    # Please do not add '/' at the end of the string! Thank you!
    # Ex: '../../Datasets/Inter4K'
    # Not: '../../Datasets/Inter4K/'
    'res':      '1080p',
    # Target resolution, please refer to 'resolution_map' for more options
    # 4K, 2K, 1080p, 720p, 540p, 360p, 270p, 180p
    'GT_res':   '',
    # Resolution of ground truth
    # Not used in this mode
    'pyenv':    'vsr',
    # Conda env name
    'remove_data':  "True",
    # Remove the video frames that are applied super-resolution to save space. (True/False)
}

# Get Low Quality
p = {

    'mode':     'Get Low Quality',
    'log':      './My_log',
    'source':   '/home/aaron/miniconda3/etc/profile.d/conda.sh',
    'start':    1,
    'end':      1,
    'crf':      30,
    'qp':       -1,
    'inter':    '../../Datasets/Inter4K',
    'res':      '270p',
    'GT_res':   '1080p',
    # Resolution of ground truth
    # (i.e. 'GT_res' should equal to 4x 'res')
    'pyenv':    'vsr',
    'remove_data':  "True",
}

# Get High Quality
p = {

    'mode':     'Get High Quality',
    'log':      './My_log',
    'source':   '/home/aaron/miniconda3/etc/profile.d/conda.sh',
    'start':    1,
    'end':      1,
    'crf':      30,
    'qp':       -1,
    'inter':    '../../Datasets/Inter4K',
    'res':      '1080p',
    'GT_res':   '1080p',
    # Resolution of ground truth
    # (i.e. 'GT_res' should equal to 'res')
    'pyenv':    'vsr',
    'remove_data':  "True",
}

# Inference
p = {

    'mode':     'Inference',
    'log':      './My_log',
    # All logs of a single 'mode'='Inference' run will be stored in an indivisual folder inside 'log' folder
    'source':   '/home/aaron/miniconda3/etc/profile.d/conda.sh',
    'start':    1,
    'end':      1,
    'crf':      [0,2,5,7,10,15,20,25,30,35,40],
    # All the CRF value you want to run in a complete experiment. Otherwise, set to '-1' if you want to use CQP.
    'qp':       -1,
    # All the CQP value you want to run in a complete experiment. Otherwise, set to '-1' if you want to use CRF.
    'inter':    '../../Datasets/Inter4K',
    'res':      '270p',
    'GT_res':   '1080p',
    'pyenv':    'vsr',
    'remove_data':  "True",
}