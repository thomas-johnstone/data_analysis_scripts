import csv

my_file_name = "output.csv"
cleaned_file_name = "clean.csv"
ONE_COLUMN = 1
remove_words = ['2018', '2019']

with open(my_file_name, 'r', newline='') as infile, \
     open(cleaned_file_name, 'w',newline='') as outfile:
    writer = csv.writer(outfile)
    for row in csv.reader(infile):
        column = row[ONE_COLUMN]
        if not any(remove_word in element for element in line for remove_word in remove_words):
            writer.writerow(line)