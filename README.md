# Coronavirus twitter analysis

In this project, I scanned all geotagged tweets sent in 2020 (about 1.1 billion tweets) to look for hashtags related to the COVID-19 pandemic.


## Background

I began with one tweet file for each day in 2020, `geoTwitterYY-MM-DD.zip`. 
Inside each zip file were 24 text files, one for each hour of the day.
Each text file contained a single tweet per line in JSON format.

I used the MapReduce procedure to analyze these tweets and take advantage of parallel processing to scan the tweets quickly. 

## Project Steps

**Step 0: Create the mapper**

I modified the mapping file `map.py` to track the country level in addition to the provided language level. 
This step allowed me to look at usage of hashtags in different languages and in different geotagged countries. 
As such, each call to `map.py` resulted in two files, one that ends in `.lang` and one that ends in `.country` for the country dictionary.

**Step 1: Run the mapper**

I created a shell script called `runmaps.sh` to loop over each file in the dataset and run the `map.py` command on that file. I used `nohup` to run the command even after I disconnected and the `&` operator for parallel processing:
```
$ nohup sh runmaps.sh &
```

**Step 2: Reduce**

Using the resulting `outputs` files, I applied `reduce.py` file to combine all of the `.lang` files into a single file,
and all of the `.country` files into a different file.

**Step 3: Visualize**

I modified the `visualize.py` file to create bar graph of the results and stores the bar graph as a png file.
After running :

```
$ python3 ./src/visualize.py --input_path=reduced.lang --key='#coronavirus'
```

with the `--input_path` equal to both the country and lang files created in the reduce phase, and the `--key` set to `#coronavirus` and `#코로나바이러스`, this generated the following plots:

![coronavirus_country](https://github.com/lbielicki/twitter_coronavirus/blob/main/coronavirus_country.png)

![coronavirus_lang](https://github.com/lbielicki/twitter_coronavirus/blob/main/coronavirus_lang.png)

As well as:

![korean_country](https://github.com/lbielicki/twitter_coronavirus/blob/main/%EC%BD%94%EB%A1%9C%EB%82%98%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4_country.png)

![korean_lang](https://github.com/lbielicki/twitter_coronavirus/blob/main/%EC%BD%94%EB%A1%9C%EB%82%98%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4_lang.png)


**Task 4: Alternative Reduce**

Finally, I created a new file `alternative_reduce.py`. This followed a similar structure to a combined version of the `reduce.py` and `visualize.py` files. I used this file to analyze three hashtags, #coronavirus, #corona, and #covid19.

![three_hashtags]([https://github.com/lbielicki/twitter_coronavirus/blob/master/coronavirus_corona_covid19.png](https://github.com/lbielicki/twitter_coronavirus/blob/main/coronavirus_corona_covid19.png)https://github.com/lbielicki/twitter_coronavirus/blob/main/coronavirus_corona_covid19.png)
