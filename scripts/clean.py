import sys
import argparse
import os.path as osp
import json
import sys
from datetime import datetime, timezone

script_dir = osp.dirname(__file__)

def main():

    # LOAD FILE USING INPUT AND OUTPUT FLAGS, REQUIRE THE INPUT TO BE IN DATA, WRITE OUTPUT TO DATA
    parser = argparse.ArgumentParser(description = 'Process JSON files.')
    parser.add_argument('-i', help = 'JSON file to be analyzed and cleaned.', required = True)
    parser.add_argument('-o', help = 'Name of the cleaned JSON file.', required = True)

    args = parser.parse_args()
    input_file = osp.join(script_dir, '..', 'data', f'{args.i}.json')
    output_file = osp.join(script_dir, '..', 'data', f'{args.o}.json')
    print(f'input_file =  {input_file}')
    print(f'output_file =  {output_file}')

    data = []

    #LOAD EACH LINE OF THE JSON TO CLEAN
    with open(input_file) as input:
        for line in input:
            try:
                data.append(json.loads(line))
            except ValueError:
                continue

    #REPLACE TITLE_TEXT WITH TITLE
    for title in data:
        for k,v in list(title.items()):
            if k == 'title_text':
                title['title'] = title.pop('title_text')

    #CORRECT THE VALID DATES TO THE DESIRED FORM
    for date in data:
        for k,v in list(date.items()):
            if k == 'createdAt':
                try:
                    fix = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S%z')
                    date['createdAt'] = str(fix.replace(tzinfo = timezone.utc))
                    date['createdAt'] = date['createdAt'].replace(" ", "T")
                    date['fixed'] = date.pop('createdAt')
                except ValueError:
                    continue

    #REMOVE THE EXTRA TITLES + DATES
    data = ([dic for dic in data if dic.get('title', False)])
    data = ([dic for dic in data if dic.get('fixed', False)])
    for date in data:
        date['createdAt'] = date.pop('fixed')

    #WRITE THE OUTPUT FILE TO DATA
    output_file = open(output_file, 'w')
    for index in data:
        json.dump(index, output_file)
        output_file.write("\n")

if __name__ == '__main__':
    main()