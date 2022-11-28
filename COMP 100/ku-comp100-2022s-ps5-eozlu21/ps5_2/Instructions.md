# COVID19 Database
## Deadline: 05/06/2022 - 23:00


## Overview
In this assignment, our goal is to analyze COVID-19 data provided by European Centre for Disease Prevention and Control. We will use data containing 30 countries' populations (as well as the age groups), daily/weekly cases (together with age groups), and daily deaths.

We will practice file reading, parsing, sorting data, and object-oriented programming. 

In the end, we will be able to calculate (per country):

* Cases/deaths per 1M,
* Exposure per age group, and the most/least infected age groups,
* Probability of belonging a new case to an age group,
* The distribution of deaths according to age groups

Finally, we will report extreme cases according to these statistics. 

## Q1) Reading a File and Storing Data (30 pts)

You can access the COVID-19 data using [this link] (https://www.ecdc.europa.eu/en/publications-data/data-daily-new-cases-covid-19-eueea-country). We will be working on these two datasets:

* (data.json) The daily number of new reported COVID-19 cases and deaths by EU/EEA country: The data file contains information on newly reported COVID-19 cases and deaths in EU/EEA countries. Each entry contains the corresponding data for a certain day per country. You can also look at [this document] (https://www.ecdc.europa.eu/sites/default/files/documents/Description-and-disclaimer_daily_reporting.pdf) to get more information.
  
* (agecases.json) 14-day age-specific notification rate of new COVID-19 cases: It contains information on the 14-day notification rate of newly reported COVID-19 cases per 100,000 population by age group, week and country. Each entry  contains the corresponding data for a certain week and a country. You can also look at [this document](https://www.ecdc.europa.eu/sites/default/files/documents/2020-11-26_Variable_Dictionary_and_Disclaimer_national_age_case_data.docx) to get more information.
    
There are lots of options for the file format such as XLSX, CSV, JSON and XML. We are going to use JSON format, which stores the data as a structured format in a text-based and human-readable files.

### Q1.1) Saving Daily Cases

Go to __init__ function of Covid19Analyzer under at covid_db.py file. Our first goal is to read a .json file and convert it to some data structure that can be used within Python.

* Using a `with open` statement, read and load the *data.json* file using `json.load()` function. This loader returns you a nested lists of dicts under the `records` key. After that, you have a list of records.
  
* Iterate over the list of records. Each record corresponds to a dictionary, which includes the following information:

```
      {
         "dateRep" : "15/05/2021",
         "day" : "15",
         "month" : "05",
         "year" : "2021",
         "cases" : 721,
         "deaths" : 14,
         "countriesAndTerritories" : "Austria",
         "geoId" : "AT",
         "countryterritoryCode" : "AUT",
         "popData2020" : "8901064",
         "continentExp" : "Europe"
      }

```

Refer to the documentation that we linked before for the definitions of the keys and the values.

* Inorder to store and process this data, we're going to use the power of object-oriented programming. In `Covid19Analyzer` class, there is an empty dictionary object called `self.db`. While iterating over the records, you must create a `Country` object with the parameters `name` (the full name of the country) and the `population` (int) if it doesn't exist and save it to
the dictionary `self.db` with the key `geoID` as the representative of a unique country code. This way, we can access each country through our database dictionary.

* We're going to save each record to a relevant `Country` object by using `save_daily_data()`, which takes three arguments: `date` (string), `cases` (int), and `deaths` (int) and appends the data to `daily_records` list as a dictionary. Here, we are going to process the data from March 7, 2021 to May 3, 2021 (both are not included.)

* You can create specific dates by using [datetime library](https://docs.python.org/3/library/datetime.html) of python. Adding, subtracting and comparing dates with standard operators are valid. This is called operator overloading in programming languages. 
To build a datetime object, you should decompose the string in a record given by `dateRep` key to days, month, and year.

**Hint**: You can check `strptime` function.

Once you have finished storing the data, you can move to the next part.

### Q1.2) Saving Weekly Cases

Similar to the first part, we are going to save weekly case data, but this time, by also including an age-group information as well. Again, each record contains information about a specific country:

```
	{
		"country" : "Austria",
		"country_code" : "AT",
		"year_week" : "2020-13",
		"age_group" : "<15yr",
		"new_cases" : 156,
		"population" : 1283060,
		"rate_14_day_per_100k" : 16.7,
		"source" : "TESSy COVID-19, national weekly data"
	}

```

Our goal is to extract `country_code`, `year_week`, `age_group` and `population`. This time, the `Country` objects is ready in the database `db` from before.

We first need to save populations of age groups per country if it is not set before. We placed -1 as the sentinel values for age groups in the dictionary `population_by_agegroup`. Do not forget to convert this to an integer.

This time, we are going to use `save_weekly_data` function to save our data, which takes `age_group` (str), `year_week` (str), `new_cases` (int) as arguments. Here, the timestamps are in the year-week format. In order to align the dates that are given in the first part,
you should only include the weeks between 9 and 18 (both are not included) of 2021.

Note that some countries do not include this data such as France and Luxembourg.

## Q2) Country Class (55 pts)

### Q2.1) Total Cases and Total Deaths (10 pts)

In order to understand how bad the pandemic is for each country, we need to implement these functions first:

* `get_total_cases()`: Calculates the number of total cases that are stored in `daily_records`.
* `get_total_deaths()`: Calculates the number of total deaths that are stored in `daily_records`.
* `total_cases_and_deaths_per_1m()`: Scales the number of total deaths and cases to 1M population.

**Hint**: You can use `get_total_cases` and `get_total_deaths` functions as a shortcut.

With these functions, we will be able to compare each country based on 1M population.  

### Q2.2) Age Group Analysis (10 pts)

At this step, our goal is to implement functions to analyze age groups. First, we are going to
calculate exposure (infection rate) per age group in `calc_exposure_per_age_group()` function and return the rates as a dictionary. 

To calculate the infection rate, all you need to do is to divide the number of total cases of an age group by the population of the age group. An example output:

```

{'<15yr': 0.017913464038181382, '15-24yr': 0.04201250553342187, '25-49yr': 0.03855293226103967, 
'50-64yr': 0.03147054552624966, '65-79yr': 0.011292551441701803, '80+yr': 0.005146315722740376}

```

which shows for example, 1.79 percent of `<15yr` old citizens are tested positive for COVID-19. Therefore, this function will give us information about which age group is affected the most and the least. So, we can extend our functionality to find the most and the least exposed age group. Implement the functions `find_most_exposed_age_group()` and 
`find_least_exposed_age_group()` and return the age group as a string.

### Q2.3) Distributing The Number of Deaths to Age Groups (15 pts)

Then, we will make some estimations. In our weekly data, we do not have the number of deaths per age group. To have
an estimation, first we need to calculate the probabilities of a new case belonging to age groups. Implement, 
`calc_prob_of_cases_per_age_group()` function, which divides the total number of cases per age group by the total number of cases and returns the result as a dictionary as in the following:


```
{'<15yr': 0.1222859590983134, '15-24yr': 0.28679765802568175, '25-49yr': 0.26318093962981876, 
'50-64yr': 0.21483314644347676, '65-79yr': 0.07708841130739452, '80+yr': 0.035131237187663845}
```

Here, we calculated a statistic of distributing cases to age groups. To convert this distribution to deaths, scientists have a prior info about weighting the cases, given as a list:

```
death_probs = [0.05, 0.05, 0.1, 0.2, 0.25, 0.35]
```

Here, each entry gives a normalized weighting of probability of deaths with respect to age groups. Scale the output of the `calc_prob_of_cases_per_age_group()` by these weights. You should multiply each weight with the calculated probability of cases per age group, then scale it back so that the total probability sums to 1.

Finally, get the total number of deaths with the `get_total_deaths` function and multiply with each probability value to distribute the number of total deaths to the age groups. 

### Q2.4) Sorting: Finding Top-K Cases and Top-K Deaths (20 pts)

In this part, our goal is to find the dates where the number of deaths and the number of cases is the highest. This approach will help us to understand what are the peak dates for a specific country. In this section, we provide some functionality for you. Analyze
the functions `find_top_k_cases` and `find_top_k_deaths`. They both make use of `sort_records_by` function to find the sorted version of the cases and deaths and prints them after with a string converter function `daily_records_to_string`. The only
remaining thing is some sorting mechanism which can sort a list of numbers and returns the indices according to the original list that would give the sorted list.

Implement the function `sort_records_by(param)`. Here, `param` determines what type of record (`cases` or `deaths`) that are going to be sorted. You can implement any sorting algorithm you want. Using an implemented function for sorting (e.g. `sorted()`) is not allowed.

## Q3) Processing Big Data (15 pts)

Go back to `Covid19Analyzer` class and implement `process_big_data()` function to find the following information: 

* The most and the least exposed age groups in EU.
* The country which has the highest deaths per 1M, together with the number.
* The country which has the highest cases per 1M, together with the number.

After implementing these, run covid_db.py. The program will print these information and  all of the summaries of the countries. 