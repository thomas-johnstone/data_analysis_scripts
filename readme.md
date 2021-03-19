# Data Analysis Project

## Introduction:
Assorted Python scripts to scrape reddit posts, analyze datasets, filter pertinent data, and compute TF-IDF scores. This information is then processed and outputted as concise JSON.
* collect, collect_posts, and clean fetch reddit data and then filter out the extra metadata to only display the post title
* compile_word_count and compute_pony_lang take large csv datasets of character dialogue in a show and display word counts by character, episode, etc.
* compute_tfidf takes a 'collected' dataset and computes the [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) for the entire set. This script also removes stop words for a more pertinent analysis
* filter_to_csv takes a JSON formatted set and removes entries without specific words (in this case, Trump or Biden)
* trimmer also removes specific terms from a specific column of the data

## Technologies:
Project is created with:
* Python version: 3.8
* bokeh library
* pandas library
* requests library for reddit api

## Project Status:
* v1.0: initial upload and commit. To do: complete readme, clean up script names, establish a natural process flow between scripts.

## Setup & Launch:
To run this project, run Python3 scripts locally using...

```
$ cd ../lorem
$ npm install
$ npm start
```

The script itself has helper functions built in that show you the necessary flags for input/output destinations etc.
