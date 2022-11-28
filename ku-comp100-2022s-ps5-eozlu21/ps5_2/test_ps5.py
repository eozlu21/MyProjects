from country import Country


def prep_country():

  country_obj = Country(name="Turkey", population=80000000)
  country_obj.save_daily_data("01/01/2021", 30000, 250)
  country_obj.save_daily_data("02/01/2021", 25000, 300)
  country_obj.save_daily_data("03/01/2021", 30000, 270)
  country_obj.save_daily_data("04/01/2021", 40000, 260)
  country_obj.save_daily_data("05/01/2021", 25000, 250)
  country_obj.save_daily_data("06/01/2021", 29000, 300)
  country_obj.save_daily_data("07/01/2021", 36000, 200)

  country_obj.save_daily_data("08/05/2021", 46000, 240)
  country_obj.save_daily_data("09/05/2021", 39000, 250)
  country_obj.save_daily_data("10/05/2021", 49000, 300)
  country_obj.save_daily_data("11/01/2021", 37000, 260)
  country_obj.save_daily_data("12/01/2021", 40000, 350)
  country_obj.save_daily_data("13/01/2021", 46000, 350)
  country_obj.save_daily_data("14/01/2021", 48000, 280)

  country_obj.save_weekly_data("<15yr", "2021-01", 15000)
  country_obj.save_weekly_data("<15yr", "2021-01", 40000)

  country_obj.save_weekly_data("15-24yr", "2021-01", 80000)
  country_obj.save_weekly_data("15-24yr", "2021-02", 100000)

  country_obj.save_weekly_data("25-49yr", "2021-01", 30000)
  country_obj.save_weekly_data("25-49yr", "2021-02", 50000)

  country_obj.save_weekly_data("50-64yr", "2021-01", 50000)
  country_obj.save_weekly_data("50-64yr", "2021-02", 60000)

  country_obj.save_weekly_data("65-79yr", "2021-01", 20000)
  country_obj.save_weekly_data("65-79yr", "2021-02", 25000)

  country_obj.save_weekly_data("80+yr", "2021-01", 20000)
  country_obj.save_weekly_data("80+yr", "2021-02", 30000)

  country_obj.population_by_agegroup["<15yr"] = 15000000
  country_obj.population_by_agegroup["15-24yr"] = 10000000
  country_obj.population_by_agegroup["25-49yr"] = 20000000
  country_obj.population_by_agegroup["50-64yr"] = 15000000
  country_obj.population_by_agegroup["65-79yr"] = 15000000
  country_obj.population_by_agegroup["80+yr"] = 5000000

  return country_obj

def test_get_total_cases():

  country_obj = prep_country()
  pred_cases = country_obj.get_total_cases()

  fail = False
  if pred_cases != 520000:
    fail = True
    print("Problem in test_get_total_cases()")

  assert not fail

  if fail:
    return 0
  else:
    print("Success in  test_get_total_cases()")
    return 5


def test_get_total_deaths():

  country_obj = prep_country()
  pred_deaths = country_obj.get_total_deaths()

  fail = False
  if pred_deaths != 3860:
    fail = True
    print(pred_deaths)
    print("Problem in test_get_total_deaths()")

  assert not fail

  if fail:
    return 0
  else:
    print("Success in  test_get_total_deaths()")
    return 5

def test_sort_records_by():

  country_obj = prep_country()
  param = "cases"
  pred_idxs = country_obj.sort_records_by(param)

  print(country_obj.daily_records)

  fail = False
  if pred_idxs != [1, 4, 5, 0, 2, 6, 10, 8, 3, 11, 7, 12, 13, 9]:
    fail = True
    print("Problem in test_sort_records_by()")
  assert not fail

  if fail:
    return 0
  else:
    print("Success in  test_sort_records_by()")
    return 5


def test_exposure_per_age_group():

  country_obj = prep_country()

  out = country_obj.find_least_exposed_age_group()
  out2 = country_obj.find_most_exposed_age_group()

  fail = False
  if out != '65-79yr' or out2 != '15-24yr':
    fail = True
    print("Problem in test_exposure_per_age_group")

  assert not fail

  if fail:
    return 0
  else:
    print("Success in  test_sort_records_by()")
    return 5


def test_death_distr():

  country_obj = prep_country()

  deaths, out_dict = country_obj.distribute_deaths_to_age_groups()

  fail = False
  if out_dict != {'<15yr': 98, '15-24yr': 482, '25-49yr': 214, '50-64yr': 785, '65-79yr': 401, '80+yr': 1875}:
    fail = True
    print("Problem in test_death_distr")

  assert not fail

  if fail:
    return 0
  else:
    print("Success in  test_death_distr()")
    return 5


def test_total_cases_and_deaths_per_1m():

  country_obj = prep_country()
  cases, deaths = country_obj.total_cases_and_deaths_per_1m()

  fail = False
  if cases != 6500 or deaths != 48:
    fail = True
    print("Problem in test_death_distr")

  assert not fail

  if fail:
    return 0
  else:
    print("Success in  test_death_distr()")
    return 5
prep_country()
test_get_total_deaths()
test_get_total_cases()
test_exposure_per_age_group()
test_total_cases_and_deaths_per_1m()
test_sort_records_by()