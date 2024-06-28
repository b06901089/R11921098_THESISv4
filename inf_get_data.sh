
source $1

start=$2
end=$3
inter=$6
res=$7
name=$8
log=$9
pyenv=${10}

conda activate ${pyenv}

python resolution_changes.py --$4 $5 --start $start --end $end --inter $inter --res $res --name $name --log $log
python video2image.py --start $start --end $end --inter $inter --res $res --name $name --log $log
