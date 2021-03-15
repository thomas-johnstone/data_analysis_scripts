from os import remove
import os.path as osp
import json
import argparse
import math
import itertools

script_dir = osp.dirname(__file__)

def main():
    
    # LOAD FILE USING INPUT AND OUTPUT FLAGS, REQUIRE THE INPUT TO BE IN DATA, WRITE OUTPUT TO DATA
    parser = argparse.ArgumentParser(description = 'Compute TF-IDF from JSON list of words spoken by individual pony.')
    parser.add_argument('-p', help = 'Optional flag to compute based on new TF-IDF definition.', action = "store_true", required=False)
    parser.add_argument('input_file', help = 'JSON list with word frequency by pony in raw numbers.')
    parser.add_argument('num_words', help = 'TF-IDF score for each pony.')
    
    args = parser.parse_args()
    new_compute = args.p
    input_file = args.input_file
    num_words = args.num_words
    result = {}; data = {}; word_count = {}; use_count = {}
    result['Twilight Sparkle'] = {}; result['Applejack'] = {}; result['Pinkie Pie'] = {}
    result['Rarity'] = {}; result['Rainbow Dash'] = {}; result['Fluttershy'] = {}
    total_words = 0

    with open(input_file) as json_file:
        data = json.load(json_file)

    # PARSE THE DICTIONARY TO GET WORDS & COMPUTE TF-IDF
    for pony in data:
        for key, value in data[pony].items():
            # COUNTS TOTAL WORDS SPOKEN
            total_words += value
            #total_words += 1 ????
            # INITIALIZE A DICTIONARY FOR EACH WORD
            word_count[key] = 0
            use_count[key] = 0
    for pony in data:
        for key, value in data[pony].items():
            # CALCULATE THE FREQUENCY OF THE WORDS AND ADD TO THE DICTIONARY WITH WORD COUNT
            word_count[key] += value
            # INCREMENT A USE COUNT IF THIS PONY SAYS THE WORD
            use_count[key] += 1
    for pony in data:
        for key, value in data[pony].items():
            # CALCULATE THE IF-IDF USING THE METHOD BASED ON THE FLAG, APPEND TO RESULT DICTIONARY
            if new_compute == False:
                idf = (math.log(total_words / word_count[key]))
                tfidf_score = (value) * (idf)
            else:
                idf = (math.log(6 / use_count[key]))
                tfidf_score = (value) * (idf)
            result[pony][key] = tfidf_score

    # FORMAT AND DISPLAY AS DICTIONARY IN DESIRED OUTPUT
    for pony in result:
        # SORT THE VALUES IN THE NESTED DICTIONARY FROM HIGHEST TO LOWEST
        result[pony] = {key:value for key, value in sorted(result[pony].items(), key = lambda item:item[1], reverse = True)}
        # CROP THE NESTED DICTIONARY (EACH PONY'S TF-IDF) DOWN TO A NUMBER PROVIDED BY INPUT
        result[pony] = dict(itertools.islice(result[pony].items(), int(num_words)))

    final = {}
    for pony in result:
        key_iterable = result[pony].keys()
        key_list = list(key_iterable)
        final[pony] = key_list
    print(json.dumps(final))

if __name__ == '__main__':
    main()