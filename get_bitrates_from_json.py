import argparse
import json

parser = argparse.ArgumentParser()

parser.add_argument('--input', type=str)
parser.add_argument('--start', type=int)
parser.add_argument('--end', type=int)
parser.add_argument('--log', type=str)

args = parser.parse_args()

avg_bitrates = 0

for i in range(args.start, args.end+1):

    # Opening JSON file
    f = open(args.input[:-5]+str(i)+args.input[-5:])
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    
    # Iterating through the json
    # list
    for j in data['streams']:
        avg_bitrates += int(j['bit_rate'])
    
    # Closing file
    f.close()

avg_bitrates /= (args.end-args.start+1)

# print('bitrates: {}'.format(avg_bitrates))
# print('bitrates: {}K'.format(avg_bitrates/1000))
print('bitrates: {}M'.format(avg_bitrates/1000000))

with open(args.log, 'a') as f:
    f.write('bitrates: {}M\n\n'.format(avg_bitrates/1000000))