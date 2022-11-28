import json
from country import Country
from datetime import datetime

class Covid19Analyzer:

  def __init__(self):

    # This is your database. Keys are the country codes.
    self.db = {}

    with open("data.json") as f:
      data = json.load(f)

      for record in data['records']:
      
        #################################################
        #             YOUR CODE GOES HERE               #
        #################################################
        if record["geoId"] not in self.db.keys():
          self.db[record["geoId"]] = Country(record["countriesAndTerritories"],record["popData2020"])
        self.db[record["geoId"]].save_daily_data(record["dateRep"], record["cases"], record["deaths"])

    ## END OF LOADING DATA.JSON

    with open("agecases.json") as f:
      agecases = json.load(f)

      for record in agecases:


    #################################################
    #             YOUR CODE GOES HERE               #
    #################################################
        if self.db[record["country_code"]].population_by_agegroup[record["age_group"]] == -1:
          self.db[record["country_code"]].population_by_agegroup[record["age_group"]] = record["population"]
        if int(record["year_week"].split("-")[1]) in range(10,18) and int(record["year_week"].split("-")[0]) == 2021:
          self.db[record["country_code"]].save_weekly_data(record["age_group"], record["year_week"], record["new_cases"])



  def process_big_data(self):

    most_exp_age_group_cnts = {}
    least_exp_age_group_cnts = {}

    top_case_cnt = 0
    top_death_cnt = 0
    top_case_country = ""
    top_death_country = ""

    #################################################
    #             YOUR CODE GOES HERE               #
    #################################################
    dict_of_country_deaths = {}
    dict_of_country_cases = {}
    dict_of_age_cases = {}
    for country in self.db.values():
      case, death = country.total_cases_and_deaths_per_1m()
      dict_of_country_deaths[country.name] = death
      dict_of_country_cases[country.name] = case
      for age_group in country.weekly_records.keys():
        x = dict_of_age_cases.get(age_group, 0)
        sum = 0
        for week in country.weekly_records[age_group]:
          sum += week["new_cases"]
        y = sum
        dict_of_age_cases[age_group] = x + y

    def keywithmaxval(d):
      v = list(d.values())
      k = list(d.keys())
      return k[v.index(max(v))]
      # source of this nested function: https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
    def keywithminval(d):
      v = list(d.values())
      k = list(d.keys())
      return k[v.index(min(v))]
      # source of this nested function: https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
    top_case_cnt = max(dict_of_country_cases.values())
    top_death_cnt = max(dict_of_country_deaths.values())
    top_case_country = keywithmaxval(dict_of_country_cases)
    top_death_country = keywithmaxval(dict_of_country_deaths)
    most_age_group = keywithmaxval(dict_of_age_cases)
    least_age_group = keywithminval(dict_of_age_cases)


    return top_death_country, top_death_cnt, top_case_country, top_case_cnt, most_age_group, least_age_group


  def print_summary(self):

    """
    Prints a tabulated summary of the processed data.

    :return:
    """
    print(f"Listing {len(self.db.keys())} countries.")

    for keys, values in self.db.items():
      print("===================================================")

      values.print_summary()


if __name__ == "__main__":
  analyzer = Covid19Analyzer()
  top_death_country, top_death_cnt, top_case_country, top_case_cnt, most_age_group, least_age_group = analyzer.process_big_data()

  print("Deaths per 1M Highest Country: ", top_death_country, " with ", top_death_cnt, " deaths/million")
  print("Cases per 1M Highest Country: ", top_case_country, " with ", top_case_cnt, " cases/million")
  print("Most Exposed Age Group In EU: ", most_age_group)
  print("Least Exposed Age Group In EU: ", least_age_group)

  analyzer.print_summary()