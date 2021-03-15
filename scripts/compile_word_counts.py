from os import remove
import os.path as osp
import json
import argparse
import csv

script_dir = osp.dirname(__file__)

def main():
    
    # LOAD FILE USING INPUT AND OUTPUT FLAGS, REQUIRE THE INPUT TO BE IN DATA, WRITE OUTPUT TO DATA
    parser = argparse.ArgumentParser(description = 'Compute word count from CSV input.')
    parser.add_argument('-o', '--output_file',  help = 'JSON with word counts.', required=True)
    parser.add_argument('input_file',  help = 'CSV to compute word count from.')

    args = parser.parse_args()
    input_file = args.input_file
    output_file = open(f'{args.output_file}', 'w')
    result = {}
    twilight = {}; applejack = {}; rarity = {}; pinkie = {}; rainbow = {}; fluttershy = {}
    twilight_full = []; applejack_full = []; rarity_full = []; pinkie_full = []; rainbow_full = []; fluttershy_full = []
    twilight_count = []; applejack_count = []; rarity_count = []; pinkie_count = []; rainbow_count = []; fluttershy_count = []
    special_characters = ['(', ')', '[', ']', ',', '-', '.', '?', '!', ':', ';', '#', '&']

    # COMPUTE THE FREQUENCY GIVEN A CSV STORED IN INPUT
    with open(input_file, mode = 'r') as csvFile:
        csv_reader = csv.reader(csvFile)
        # SPLIT THE DIALOGUE ROW ON SPACES
        for row in csv_reader:
            csv_words = row[3].split(" ")
            for word in csv_words:
                # DEPENDING ON WHO IS SPEAKING, 'CLEAN' THE WORD AND ADD IT TO THAT CHARACTER'S WORD LIST
                if (row[2] == 'Twilight Sparkle'):
                    # CHARACTER BY CHARACTER, REMOVE SPECIAL CHARACTERS AND RETURN LOWER CASE WORD FOR UNIFORMITY
                    cleanword = ""
                    for character in word:
                        for special_character in special_characters:
                            if character == special_character:
                                character = ''
                        cleanword += character
                    twilight_full.append(cleanword.lower())
                if (row[2] == 'Applejack'):
                    cleanword = ""
                    for character in word:
                        for special_character in special_characters:
                            if character == special_character:
                                character = ''
                        cleanword += character
                    applejack_full.append(cleanword.lower())
                if (row[2] == 'Rarity'):
                    cleanword = ""
                    for character in word:
                        for special_character in special_characters:
                            if character == special_character:
                                character = ''
                        cleanword += character
                    rarity_full.append(cleanword.lower())
                if (row[2] == 'Pinkie Pie'):
                    cleanword = ""
                    for character in word:
                        for special_character in special_characters:
                            if character == special_character:
                                character = ''
                        cleanword += character
                    pinkie_full.append(cleanword.lower())
                if (row[2] == 'Rainbow Dash'):
                    cleanword = ""
                    for character in word:
                        for special_character in special_characters:
                            if character == special_character:
                                character = ''
                        cleanword += character
                    rainbow_full.append(cleanword.lower())
                if (row[2] == 'Fluttershy'):
                    cleanword = ""
                    for character in word:
                        for special_character in special_characters:
                            if character == special_character:
                                character = ''
                        cleanword += character
                    fluttershy_full.append(cleanword.lower())

    # CALCULATE THE FREQUENCY OF EVERY WORD BASED BY PONY
    for word in twilight_full:
        # CHECK TO SEE IF THE WORD IS ALPHA
        if (word.isalpha()):
            # COUNT THE INSTANCES OF THE WORD IN THE FULL SPEECH OF THE PONY
            calculation = twilight_full.count(word)
            # APPEND TO THE LIST THE WORD AND ITS COUNT
            twilight_count.append((word, calculation))
    for word in applejack_full:
        if (word.isalpha()):
            calculation = applejack_full.count(word)
            applejack_count.append((word,calculation))
    for word in rarity_full:
        if (word.isalpha()):
            calculation = rarity_full.count(word)
            rarity_count.append((word,calculation))
    for word in pinkie_full:
        if (word.isalpha()):
            calculation = pinkie_full.count(word)
            pinkie_count.append((word,calculation))
    for word in rainbow_full:
        if (word.isalpha()):
            calculation = rainbow_full.count(word)
            rainbow_count.append((word,calculation))
    for word in fluttershy_full:
        if (word.isalpha()):
            calculation = fluttershy_full.count(word)
            fluttershy_count.append((word,calculation))

    # REMOVE WORDS THAT DO NOT MEET THE THRESHOLD OF MINIMUM FIVE USES AND PUT INTO ITS OWN DICTIONARY
    for word in twilight_count:
        # CHECK IF THE SECOND VALUE OF THE TUPLE IN EACH DICTIONARY ENTRY IS GREATER THAN 5
        if word[1] > 4:
            # ADD TO THE DICTIONARY OF TWILIGHT WITH THE KEY WORD[0], AS IN THE WORD ITSELF
            twilight[word[0]] = word[1]
    for word in applejack_count:
        if word[1] > 4:
            applejack[word[0]] = word[1]
    for word in rarity_count:
        if word[1] > 4:
            rarity[word[0]] = word[1]
    for word in pinkie_count:
        if word[1] > 4:
            pinkie[word[0]] = word[1]
    for word in rainbow_count:
        if word[1] > 4:
            rainbow[word[0]] = word[1]
    for word in fluttershy_count:
        if word[1] > 4:
            fluttershy[word[0]] = word[1]

    # FORMAT AND DISPLAY AS SINGLE DICTIONARY FOR OUTPUT
    result['Twilight Sparkle'] = twilight
    result['Applejack'] = applejack
    result['Rarity'] = rarity
    result['Pinkie Pie'] = pinkie
    result['Rainbow Dash'] = rainbow
    result['Fluttershy'] = fluttershy

    output_file.write(json.dumps(result, indent = 4))

if __name__ == '__main__':
    main()