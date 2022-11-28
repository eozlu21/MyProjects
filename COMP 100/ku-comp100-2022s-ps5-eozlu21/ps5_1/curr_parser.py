
import xml.etree.ElementTree as ET
from urllib.request import urlopen
import datetime


def get_data(date):

  """
  :param date: datetime object
  :return: data dictionary of currency values.
  """

  # Prepare the URL
  url = # TODO Part 1

  # Container for the date
  data_dict = {}


  # TODO Part 3
  tree = ET.parse(urlopen(url))
  root = tree.getroot()

  for currency in root.findall('Currency'):

    currency = # TODO Part 2

    # Skip it since this is not a currency.
    if code == "XDR":
        continue

    # TODO Part 2


    # Prepare a dictionary to store parsed information.
    cur_dict = {'buying': buying, 'selling': selling}

    # Save the currency dictionary to data dictionary.
    data_dict[code] = cur_dict

  # TODO Part 3

  return data_dict

if __name__ == "__main__":

  date = datetime.datetime(2020, 9, 14)
  cur_dict = get_data(date)
  print(cur_dict)

  date = datetime.datetime(2020, 1, 1)
  cur_dict = get_data(date)
