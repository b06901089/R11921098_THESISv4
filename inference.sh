
source $1

start=$2
end=$3
inter=$4
LR_folder=$5
HR_folder=$6
log=$7

conda activate python3.8

python get_average_mAP.py --start $start --end $end --name $LR_folder --log $log

# Remove Low Quality data to save space
# rm -rf ${inter}/Inter4K/60fps/${LR_folder}
# rm -rf ${inter}/Inter4K_frame/60fps/${LR_folder}