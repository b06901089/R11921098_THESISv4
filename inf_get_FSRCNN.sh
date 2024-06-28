
source $1

start=$2
end=$3
inter=$4
LR_folder=$5
HR_folder=$6
log=$7
pyenv=$8

conda activate ${pyenv}

# Get FSRCNN4x inference results
for i in $(seq $start $end);
do
    python sisr.py --img_dir ${inter}/Inter4K_frame/60fps/${LR_folder}/$i --out_dir ${inter}/Inter4K_frame/60fps/FSRCNN4x_${LR_folder}/$i

    python custom_inference.py --gt_dir ${inter}/Inter4K_frame/60fps/${HR_folder}/$i --sr_dir ${inter}/Inter4K_frame/60fps/FSRCNN4x_${LR_folder}/$i
    cd mAP && python main.py -na -np
    cd ..
    cp mAP/output/output.txt My_output/FSRCNN4x_${LR_folder}_${i}.txt

    echo $i
done
python get_average_psnr.py --gt ${inter}/Inter4K_frame/60fps/${HR_folder}/ --sr ${inter}/Inter4K_frame/60fps/FSRCNN4x_${LR_folder}/ --txt $log

# Remove FSRCNN4x data to save space
# rm -rf ${inter}/Inter4K_frame/60fps/FSRCNN4x_${LR_folder}