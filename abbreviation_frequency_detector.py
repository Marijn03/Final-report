# Marijn Jongsma
# 29-03-2022
# abbreviation_frequency_detector.py
# This program takes all the files ending on ".out.gz" from the current directory, 
# selects from these files the British and American tweets, tokenizes these tweets and 
# returns a csv file with the frequency and relative frequency in the GB and US tweets 
# and a csv file with the amount of British and American tweets 

import csv 
import os
import gzip
import json
import nltk
import pandas as pd
from collections import Counter

def get_GB_tweets(file_name):
    """ deletes from a gzip file the retweets in the twitter data, searches for 
    the place key in the dictionary and returns only British tweets that has GB as value 
    inside the place key and 
    """
    tweet_list = []
    with gzip.open(file_name, "r") as inp:
        for dictionary in inp:
            twitter_dict = json.loads(dictionary)
            if twitter_dict['text'][:2]!= 'RT':
                for key, value in twitter_dict.items():
                    if key == "place" and value != None and twitter_dict['lang'] == "en":
                        for key, value in value.items():
                            if value == "GB":
                                tweet_list.append(twitter_dict['text'])
        return tweet_list

def get_US_tweets(file_name):
    """ deletes from a gzip file the retweets in the twitter data, searches for 
    the place key in the dictionary and returns only American tweets that has US as value 
    inside the place key 
    """
    tweet_list = []
    with gzip.open(file_name, "r") as inp:
        for dictionary in inp:
            twitter_dict = json.loads(dictionary)
            if twitter_dict['text'][:2]!= 'RT':
                for key, value in twitter_dict.items():
                    if key == "place" and value != None and twitter_dict['lang'] == "en":
                        for key, value in value.items():
                            if value == "US":
                                tweet_list.append(twitter_dict['text'])
        return tweet_list

def word_counter(query, text_file):
    '''counts de occurences of a word in a text file'''
    count = 0 
    for token in text_file:
        if token.lower() == query:
            count = count + 1
    return count

def tokenize_text(text_file):
    '''tokenizes the text from a text file'''
    return nltk.word_tokenize(text_file)                    

def create_csv_file_results(word_lst, US_tokenized_text, GB_tokenized_text):
    '''takes tokenized American and British tweets and a word list as argument 
    and writes the frequency and relative frequency of each word to a csv file
    '''
    fields = ['Words', 'Frequency in US', 'Frquency in GB']
    rows = []
    
    for word in word_lst:
        word_row = {'Words': word, 
                    'Frequency in US': word_counter(word, US_tokenized_text), 
                    'Frquency in GB': word_counter(word, GB_tokenized_text)}
        rows.append(word_row)

    with open('results.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    
    count = 0  
    lst_total_freq_US = []
    for row in rows:
        count = count + 1
        if (count % 2) != 0:
            total_frequency_US = rows[count-1]['Frequency in US'] + rows[count]['Frequency in US']
            lst_total_freq_US.extend([total_frequency_US, total_frequency_US])

    relative_frequencies_US = []
    for i in range(len(lst_total_freq_US)):
        relative_frequencies_US.append("{0:.1f}%".format((rows[i]['Frequency in US']/lst_total_freq_US[i]) * 100, 1))
    
    count = 0  
    lst_total_freq_GB = []
    for row in rows:
        count = count + 1
        if (count % 2) != 0:
            total_frequency_GB = rows[count-1]['Frquency in GB'] + rows[count]['Frquency in GB']
            lst_total_freq_GB.extend([total_frequency_GB, total_frequency_GB])

    relative_frequencies_GB = []
    for i in range(len(lst_total_freq_GB)):
        relative_frequencies_GB.append("{0:.1f}%".format((rows[i]['Frquency in GB']/lst_total_freq_GB[i]) * 100, 1))
    
    df = pd.read_csv('results.csv')  
    df['Relative frequency in US'] = relative_frequencies_US
    df['Relative frequency in GB'] = relative_frequencies_GB
    df.to_csv('results.csv', index=False)

def create_csv_file_data():
    '''creates a csv file with the amount of tweets from the US and GB'''
    with open('GB_tweets.txt', 'r') as inp_GB, open('US_tweets.txt', 'r') as inp_US:
        count_GB_tweets = 0  
        for line in inp_GB.readlines():
            if not line.isspace():
                count_GB_tweets = count_GB_tweets + 1
        count_US_tweets = 0

        for line in inp_US.readlines():
            if not line.isspace():
                count_US_tweets = count_US_tweets + 1
        
        df = pd.DataFrame([['Amount of tweets', count_US_tweets, count_GB_tweets]], columns=['Total', 'US', 'GB'])
        df.to_csv('data.csv', index=False)

def main():
    with open('GB_tweets.txt', 'w') as out_GB, open('US_tweets.txt', 'w') as out_US:
        for file in os.listdir('.'):
            if file.endswith(".out.gz"):
                out_US.write(str("\n".join(get_US_tweets(os.path.join('.', file)))))
                out_GB.write(str("\n".join(get_GB_tweets(os.path.join('.', file)))))

    with open('GB_tweets.txt', 'r') as inp_GB, open('US_tweets.txt', 'r') as inp_US:
        US_file = inp_US.read()
        GB_file = inp_GB.read()
        US_tokenized_text = tokenize_text(US_file)
        GB_tokenized_text = tokenize_text(GB_file)

        word_lst = ['you','u','are','r','your','ur']
        create_csv_file_results(word_lst, US_tokenized_text, GB_tokenized_text)
        create_csv_file_data()
        
        
if __name__ == '__main__':
    main()

