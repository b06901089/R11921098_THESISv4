
source $1

start=$2
end=$3
inter=$4
LQ_folder=$5
HQ_folder=$6
log=$7
pyenv=$8

conda activate ${pyenv}

for i in $(seq $start $end);
do
    python custom_inference.py --gt_dir ${inter}/Inter4K_frame/60fps/${HQ_folder}/${i} --sr_dir ${inter}/Inter4K_frame/60fps/${LQ_folder}/${i}
    cd mAP && python main.py -na -np
    cd ..
    cp mAP/output/output.txt My_output/${LQ_folder}_${i}.txt

    echo $i
done
python get_average_psnr.py --gt ${inter}/Inter4K_frame/60fps/${HQ_folder}/ --sr ${inter}/Inter4K_frame/60fps/${LQ_folder}/ --txt $log