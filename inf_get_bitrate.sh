
source $1

start=$2
end=$3
inter=$4
name=$5
log=$6
pyenv=$7

conda activate ${pyenv}

for i in $(seq $start $end);
do
    ffprobe -v error -print_format json -show_entries stream=bit_rate ${inter}/Inter4K/60fps/${name}/$i.mp4>My_output/${name}_$i.json
done
python get_bitrates_from_json.py --input My_output/${name}_.json --start $start --end $end --log $log
