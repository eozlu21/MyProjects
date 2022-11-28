class Country:

  def __init__(self, name, population):

    self.name = name
    self.population = population
    self.population_by_agegroup = {'<15yr': -1, '15-24yr':-1, '25-49yr':-1, '50-64yr':-1, '65-79yr':-1, '80+yr':-1}
    self.daily_records = []
    self.weekly_records = {'<15yr' : [], '15-24yr': [], '25-49yr': [], '50-64yr': [], '65-79yr':[], '80+yr':[]}

  def daily_records_to_string(self, idxs):

    output_str = ""
    for idx in idxs:
      record = self.daily_records[idx]
      output_str += f"Date: {record['date']}, Cases: {record['cases']}, Deaths: {record['deaths']} \n"

    return output_str

  def save_daily_data(self, date, cases, deaths):

    """
    Saves daily data.
    :param date: (string) e.g. (27/03/2021).
    :param cases: (int) e.g.(3221)
    :param deaths: (int) e.g. (231)
    :return: None
    """

    self.daily_records.append({'date': date, 'cases': cases, 'deaths': deaths})

  def save_weekly_data(self, age_group, year_week, new_cases):

    self.weekly_records[age_group].append({'year_week': year_week, 'new_cases': new_cases}),

  def get_total_cases(self):

    #################################################
    #             YOUR CODE GOES HERE               #
    #################################################

    total_cases = 0
    for daily_record in self.daily_records:
      total_cases += daily_record["cases"]
    return total_cases

  def get_total_deaths(self):

    #################################################
    #             YOUR CODE GOES HERE               #
    #################################################

    total_deaths = 0
    for daily_record in self.daily_records:
      total_deaths += daily_record["deaths"]
    return total_deaths

  def total_cases_and_deaths_per_1m(self):

    #################################################
    #             YOUR CODE GOES HERE               #
    #################################################

    case_per_1mil = (self.get_total_cases()/int(self.population))*1000000
    death_per_1mil = (self.get_total_deaths()/int(self.population))*1000000
    return int(case_per_1mil), int(death_per_1mil)

  def sort_records_by(self, param):

    # Gives you a list of cases or deaths depending on param
    nums = [record[param] for record in self.daily_records]

    #################################################
    #             YOUR CODE GOES HERE               #
    #################################################
    temp_nums = nums
    index_list = [i for i in range(len(nums))]
    def insertionSort(l1,index_list):
      for i in range(1, len(l1)):   
          key = l1[i]
          key2 = index_list[i]
          j = i-1
          while j >=0 and key < l1[j] :
                  l1[j+1] = l1[j]
                  index_list[j+1] = index_list[j]
                  j -= 1
          l1[j+1] = key
          index_list[j+1] = key2
    insertionSort(nums, index_list)
    return index_list
    

  def find_top_k_cases(self, k):

    idxs = self.sort_records_by("cases")[-k:]
    out = self.daily_records_to_string(idxs)

    return out

  def find_top_k_deaths(self, k):

    idxs = self.sort_records_by("cases")[-k:]
    out = self.daily_records_to_string(idxs)

    return out

  def calc_exposure_per_age_group(self):

    #################################################
    #             YOUR CODE GOES HERE               #
    #################################################

    returning_dict = {}
    for age_group in self.weekly_records.keys():
      sum = 0
      for week in self.weekly_records[age_group]:
        sum += week["new_cases"]
      returning_dict[age_group] = sum/self.population_by_agegroup[age_group]
    return returning_dict

  def find_most_exposed_age_group(self):

    #################################################
    #             YOUR CODE GOES HERE               #
    #################################################

    def keywithmaxval(d):
     v = list(d.values())
     k = list(d.keys())
     return k[v.index(max(v))]
     #source of this nested function: https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
    return keywithmaxval(self.calc_exposure_per_age_group())

  def find_least_exposed_age_group(self):

    #################################################
    #             YOUR CODE GOES HERE               #
    #################################################

    def keywithminval(d):
     v = list(d.values())
     k = list(d.keys())
     return k[v.index(min(v))]
     #source of this nested function: https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
    return keywithminval(self.calc_exposure_per_age_group())

  def calc_prob_of_cases_per_age_group(self):

    #################################################
    #             YOUR CODE GOES HERE               #
    #################################################

    # def get_total_cases_for_age_group(age_group):
    #   sum = 0
    #   for week in self.weekly_records[age_group]:
    #     sum += week["new_cases"]
    #   return sum

      
    # returning_dict = {}
    # sum_of_all_test_cases = 0
    # for age_group in self.weekly_records.keys():
    #   sum_of_all_test_cases += get_total_cases_for_age_group(age_group)
    # for age_group in self.weekly_records.keys():
    #   returning_dict[age_group] = get_total_cases_for_age_group(age_group)/sum_of_all_test_cases
    # return returning_dict
    prob_of_cases_per_age_group = self.calc_exposure_per_age_group()
    weight = sum(prob_of_cases_per_age_group.values())
    for key, value in prob_of_cases_per_age_group.items():
      prob_of_cases_per_age_group[key] = value/weight
    return prob_of_cases_per_age_group    


  def distribute_deaths_to_age_groups(self):
    case_probs = self.calc_prob_of_cases_per_age_group()
    death_probs = [0.05, 0.05, 0.1, 0.2, 0.25, 0.35]
    conditionals = {}

    #################################################
    #             YOUR CODE GOES HERE               #
    #################################################
    new_dict = {}
    total_deaths = self.get_total_deaths()
    returning_dict = {}
    for i,(age_group, probability) in enumerate(case_probs.items()):
      new_dict[age_group] = probability*death_probs[i]
    weight_adjustment = sum(new_dict.values())
    for age_group,probs in new_dict.items():
      val = (total_deaths*probs/weight_adjustment)
      if (val + 0.5) == int(val):
        returning_dict[age_group] = int(val) - 1
      else:
        returning_dict[age_group] = int(val)
    return total_deaths, returning_dict

  def print_summary(self):


    print("Country name: ", self.name)
    print("Showing data between: ", self.daily_records[-1]['date'], " - ", self.daily_records[0]['date'] )
    cases1m, deaths1m = self.total_cases_and_deaths_per_1m()
    print(f"Total cases per 1M: {cases1m}, total deaths per 1M: {deaths1m}")
    print("Most exposed age group: ", self.find_most_exposed_age_group())
    print("Least exposed age group: ", self.find_least_exposed_age_group())
    print('')
    print("Top 5 Cases:")
    print(self.find_top_k_cases(5))
    print("Top 5 Deaths:")
    print(self.find_top_k_deaths(5))

    deaths, distribution = self.distribute_deaths_to_age_groups()
    print("Total deaths: ", deaths)
    print("Estimated distribution: ", distribution)