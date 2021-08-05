# Data Analysis Project

## Introduction

Assorted Python scripts to scrape reddit posts, analyze datasets, filter pertinent data, and compute [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) scores. This information is then processed and outputted as concise JSON.

- In ./scripts: collect.py, collect_posts.py, and clean.py fetch reddit data and then filter out the extra metadata to only display the post title
- In ./scripts: compile_word_count.py and compute_pony_lang.py take large csv datasets of character dialogue in a show and display word counts by character, episode, etc.
- In ./scripts: compute_tfidf.py takes a collected or formatted dataset and computes the TF-IDF for the entire set. This script also removes stop words for a more pertinent analysis
- In ./scripts: filter_to_csv.py takes a JSON formatted set and removes entries without specific words (in this case, Trump or Biden)
- In ./scripts: trimmer.py also removes specific terms from a specific column from the csv data

## Technologies

Project is created with:

- Python version: 3.8
- bokeh library from python
- pandas library from python
- 'requests' library for the official reddit api

## Project Status

- v1.0: initial upload and commit. To do: clean up script names, establish a natural process flow between scripts.

## Setup & Launch

The script itself has helper functions built in that show you the necessary flags for input/output destinations etc.
Further installation instructions pending....
