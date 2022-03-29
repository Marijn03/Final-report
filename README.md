# The frequency of abbreviations counter on the Twitter corpus

In this GitHub you can find the code to find the frequency of abbreviations in a corpora. In order to get the amount of tweets and frequency of the abbreviations on Twitter, please follow the steps below.  

## Installation
Acces to my repository:
```
git clone https://github.com/Marijn03/Final-report.git
```

## Get all .gz files from the English corpus from 2016 and 2015
Search for .gz files of the English corpus from 2016 and 2015, and put them all in a .txt file on your home directory in the corpus. This can be done by using the following command in the commandline on your home directory in the corpus:
```
find /net/corpora/twitter2_en/Tweets/2015 /net/corpora/twitter2_en/Tweets/2016 -type f -name "*.out.gz" | cut -d'/' -f8 > selected_files.txt
```

## Move the selected_files.txt file from the home directory on the corpora to your local directory

Go to the local directory, where you want to put the file from the corpora.
```
cd path
```
In order to put the file from corpus on your local directory, you have to run the following code with your own student number on the command line in your local directory:
  
```
scp -r (student_number)@karora.let.rug.nl:/home/student_number/selected_files.txt .
```
You will have to give your password in order to give permission for this command.  

## Get random files 
Go to the local directory, where you have put the selected_files.txt file that contains the names of the gz_files of the corpus from the 2016 and 2015:
```
cd path
```

In order to get a list of 10 random selected files, you will have to put the following command on the commandline in the local directory:

```
python3 random_files_selector.py selected_files.txt
```
The result is that in the local directory a file (random_selected_files.txt) has now been created with 10 unique randomly chosen gz_files. 

## Find the random selected files
In order to find the random selected files in the corpus, you must use the command:

```
find /net/corpora/twitter2_en/Tweets -type f -name file.out.gz

```

Don’t forget to replace “file.out.gz” with the wanted file

## Get random selected files on local directory
To put the random selected files to your local directory you have to put the path from “find the random selected files” in the following code as well as your student number.
```
scp -r (student_number)@karora.let.rug.nl:path .
```
Don't forget to go to the directory where you want to put the file and replace "path". 

## Get the tweets GB, tweets US and .csv files with the frequency of abbreviations and the data 

First you need to go to the directory, where the .out.gz files are located. 
```
cd path
```

In order to get the tweets from GB and the US, the results.csv file and data.csv file with the frequencies of the abbreviations on your local directory put the following command on the commandline in the local directory.

```
python3 abbreviation_frequency_detector.py
```
