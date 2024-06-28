import os
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--start', type=int)
parser.add_argument('--end', type=int)
parser.add_argument('--name', type=str)
parser.add_argument('--log', type=str)
args = parser.parse_args()

start = args.start
end = args.end

targets = [args.name, f'BI4x_{args.name}', f'FSRCNN4x_{args.name}', f'BasicVSRplusplus_VSRx4_{args.name}']

for t in targets:

    avg_mAP = 0
    count = 0
    for i in range(start, end+1):

        path = 'My_output/{}_{}.txt'.format(t, i)

        if not os.path.isfile(path):
            break

        # with open(path, 'r') as f, open(args.log, 'a') as ff:

        #     for line in f.readlines():

        #         result = re.search("mAP = ", line)

        #         if result:

        #             # print(line[6:-2])

        #             avg_mAP += float(line[6:-2])
        #             count += 1
                
        #         ff.write(line)

        with open(path, 'r') as f:

            for line in f.readlines():

                result = re.search("mAP = ", line)

                if result:

                    avg_mAP += float(line[6:-2])
                    count += 1
    
    if not os.path.isfile(path):
        continue

    print(avg_mAP/count, count)
    with open(args.log, 'a') as f:
        f.write('\n\n')
        f.write('##########\n')
        f.write(f'{t}, average mAP: {avg_mAP/count}, video count: {count}\n')
        f.write('##########\n')