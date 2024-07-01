# R11921098_THESIS
Bandwidth-Efficient Inferencing at the Edge -- An Experimental Approach to Analyze the Effect of VSR on Compressed Video

[Demo Video part 1 - Setups](https://youtu.be/yaGjfAWvI1I)

[Demo Video part 2 - Demo run](https://youtu.be/Arcdfwvgnz8)

[Demo Video part 3 - Demo plot](https://youtu.be/g6F2YeXbqyE)

[Demo Video part 4 - Demo visualization](https://youtu.be/V4gepF-8xaE)

[Measurement Data (csv)](https://github.com/b06901089/R11921098_THESISv3/blob/main/nslab_data.csv)/
[Measurement Data (Google Sheets)](https://docs.google.com/spreadsheets/d/1Sc_uSJrqslbilyXWuuKgUcYN8FauxC2wiJDxMEutVpg/edit?usp=sharing)/
[Empty Template (Google Sheets)](https://docs.google.com/spreadsheets/d/1OiAFg_P2GxH8_gPKQVUOfqzXQ58DcqLDcpOePpG8GrE/edit?usp=sharing)

### Files Setup
---

Clone this repo
```
git clone https://github.com/b06901089/R11921098_THESISv3.git
cd R11921098_THESISv3/
```

Clone [mAP](<https://github.com/Cartucho/mAP>) inside the repo
```
git clone https://github.com/Cartucho/mAP
```

Clone [BasicVSR++](<https://github.com/ckkelvinchan/BasicVSR_PlusPlus>) inside the repo
```
git clone https://github.com/ckkelvinchan/BasicVSR_PlusPlus.git
```

Overwrite some files
```
cp restoration_video_demo.py BasicVSR_PlusPlus/demo/
cp -r chkpts/ BasicVSR_PlusPlus/
```

### Environment Setup
---

We are going to create one virtual environment with (mini/ana)conda. 
Since [BasicVSR++](<https://github.com/ckkelvinchan/BasicVSR_PlusPlus>) is built on [MMCV](https://github.com/open-mmlab/mmcv).
And MMCV depends very heavily on the version of pytorch and cuda.
We will be installing specific [Pytorch](https://pytorch.org/) versions.
If there are problems related to version mismatch or version conficts, please try to install [CUDA 11.8](https://developer.nvidia.com/cuda-11-8-0-download-archive) or [CUDA 12.1](https://developer.nvidia.com/cuda-12-1-0-download-archive).

Make sure Cuda and Nvidia driver is working
```
nvidia-smi
nvcc -V
```

Create conda environment
```
conda create --name my_env python=3.8
conda activate my_env
pip3 install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu118
```

Install requirement for [BasicVSR++](<https://github.com/ckkelvinchan/BasicVSR_PlusPlus>).
```
pip install openmim
mim install mmcv-full==1.6.0
cd BasicVSR_PlusPlus
pip install -v -e .
```

Install requirement for YOLOv5.
```
pip install -r requirements.txt
```

Install [FFmpeg](https://ffmpeg.org/).
```
pip install ffmpeg
```

Check FFmpeg version. You will need ffmpeg>=4.4 in our experience. Specific the version when installing if necessary.
```
ffmpeg
```

Install some other packages.
```
pip install psutil
pip install seaborn
```

### Dataset
---

We are using [Inter4K](<https://github.com/alexandrosstergiou/Inter4K>) dataset. 
Download the dataset with the link [https://tinyurl.com/inter4KUHD](<https://tinyurl.com/inter4KUHD>) from the official repository.
Unzip it at wherever you want to save it.
```
unzip Inter4K.zip -d Inter4K
```

For example, I unzip it under "Datasets/". The structure of the dataset should look like below:
```
Datasets/
  Inter4K/
    Inter4K/
      60fps/
        UHD/
          1.mp4
          2.mp4
          (1000 mp4s)
```

### Inference
---

Run the inference with the following command:

```
python run.py --cfg <config files>
```

For example,
```
python run.py --cfg config/inference.json
```

About the parameters in the config files, please refer to `config/parameter.py` and `config/*.json` for more information.

The results will be recorded in the log files.

![plot](https://github.com/b06901089/R11921098_THESISv3/blob/main/image/example.png?raw=true)


### Visualization

See the demo video for detailed information.

```
mkdir plot
python plot.py
```

For YOLO visualization, you will need to clone YOLO and install one additional library

```
git clone https://github.com/ultralytics/yolov5
```

Then you can simply use the scripts YOLO provided to get the bounding box rendered.

```
cd yolov5
python detect.py --weights yolov5x6.pt --source <folder path>
```

Unfortunately, library `ultralytics` that `detect.py` needs will trigger dependency issues with MMCV.
(They cannot share a same version of opencv-python. They need different versions.)
My work around is to create another conda environment and then install YOLO requirements again. For example,

```
conda create --name yolo python=3.8
conda activate yolo
pip3 install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu118
pip install -r requirements.txt
```

(`ultralytics` should be included in `requirements.txt`, but in case you need it to install manually)

```
pip install ultralytics
```

And then use this sepcific environment to run `detect.py`.


### v4 update

1. Get the object size/class frequency distribution for our test data

```
python get_object_size_distribution.py --img_dir <folder path of video frames of certain resolution> --start <start index> --end <end index>
```

Ex:

```
python get_object_size_distribution.py --img_dir ../../Datasets/Inter4K/Inter4K_frame/60fps/1080p --start 1 --end 100
```

Results will be stored under `plot/`.

2. Get execution time for video transcoding

The execution time will now simply be showed in logs. 
(i.e. Trasncode videos with different CRF/CQP and Resolution will get you the time.)
If you don't know how to transcode videos, see [Demo Video part 4 - Demo visualization](https://youtu.be/V4gepF-8xaE).
(use `run.py` with `--cfg config/get_ground_truth.json` with different `crf`, `qp`, and `res` values.)


### FAQ

1. Getting Error `Error: Files with same names already exist, please remove them and try it again!`. You have to delete the folders manually with the same folder name/path. i.e. If you want to transcode videos into a same resolution but different crf/qp values (or same values), you will need to delete your previously transcoded videos. This is because transcoded videos are stored in foldere created according to the resolution. Ex: `../../Datasets/Inter4K/Inter4K/60fps/1080p`

2. You can change the name of the config files to whatever you want, the code will read the parameter `mode` in the json files anyway.

3. FFmpeg's `preset` flag isn't an option in config files. There is a variable in `resolution_changes.py` defined as `preset`, just alter that if you wish to change it. All `preset` options can be found [here](https://trac.ffmpeg.org/wiki/Encode/H.264#Preset).

### Code Reference

```
https://github.com/alexandrosstergiou/Inter4K
https://github.com/Lornatang/FSRCNN-PyTorch
https://github.com/Cartucho/mAP
https://github.com/ckkelvinchan/BasicVSR_PlusPlus
```

All other necessary citations can be found in the original thesis. Thank you!
