import os.path as osp
import json
import argparse

script_dir = osp.dirname(__file__)

def main():
    
    # LOAD THE JSON WITH THE REDDIT DATA
    parser = argparse.ArgumentParser(description = 'Process JSON files.')
    parser.add_argument('input_file',  help = 'JSON file with Reddit title length to be averaged.')
    
    args = parser.parse_args()
    input_file = osp.join(script_dir, '..', 'data', f'{args.input_file}.json')
    print(f'input_file = {input_file}')
    f = open(input_file, 'r')

    # FILTER DOWN THE DATA FROM THE JSON IN ORDER TO GET JUST TITLE KEY CHARACTER LENGTH
    data = []
    d2 = []

    for line in f:
        data.append(json.loads(line))

    for titles in data:
        d2.append(titles['data']['title'])
    
    d2 = [len(i) for i in d2]

    # AVERAGE THE RESULT TO TWO DECIMAL PLACES
    print(round((sum(d2)/len(d2)), 2))

if __name__ == '__main__':
    main()