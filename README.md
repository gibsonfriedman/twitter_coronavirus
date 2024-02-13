# Coronavirus Tweet Analysis

This project contains multiple visualizations of 1.1 billion geotagged tweets from 2020. These visualizations examine the frequency of hashtags related to COVID-19 from the year 2020.

## Summary

The steps to gather the data and generate these visualization were:
### The MapReduce Technique:
	1. First partitioning the dataset into zip files for each day in 2020.
	1. Mapping the dataset using `map.py` counting the number of times a hashtag was used each day. This then grouped tweets by the language or the origin country of the geotag, and saved this data in the `outputs` folder in `.zip` file.
	1. Reducing the dataset with `reduce.py` to combine all of the `.zip` files into two final files, `reduced.country` and `reduced.lang`.

### Visualizations
	1. Using the mapped and reduced data, it was then visualized into 5 graphs using matplotlib.
	1. `visualize.py` was used to create four bar graphs with the top 10 languages or countries that tweets were written in.
	1. `alternative_reduce.py` was used to filter by one or more hashtags and then output a line graph showing how often those hashtags were used throughout the year.

## Visualizations

### Graphs made with `visualize.py`

#### Graph 1
This graph shows the top 10 geotagged countries of origin of tweets that used the #coronavirus in 2020.
<img src=https://github.com/gibsonfriedman/twitter_coronavirus/blob/master/coronavirus_country.png>

#### Graph 2
This graph shows the top 10 languages of tweets that used the #coronavirus in 2020.
<img src=https://github.com/gibsonfriedman/twitter_coronavirus/blob/master/coronavirus_lang.png>

#### Graph 3
This graph shows the top 10 geotagged countries of origin of tweets that used the #코로나바이러스 in 2020.
<img src=https://github.com/gibsonfriedman/twitter_coronavirus/blob/master/코로나바이러스_country.png>

#### Graph 4
This graph shows the top 10 languages of tweets that used the #코로나바이러스 in 2020.
<img src=https://github.com/gibsonfriedman/twitter_coronavirus/blob/master/코로나바이러스_lang.png>

#### Graph 5
This graph shows the frequency of the use of the hashtags corona, covid19, coronavirus, and covid2019 throughout 2020.
<img src=https://github.com/gibsonfriedman/twitter_coronavirus/blob/master/hashtags.png>
