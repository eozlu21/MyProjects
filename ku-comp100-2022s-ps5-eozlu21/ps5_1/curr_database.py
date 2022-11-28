from curr import Currency
import datetime
from curr_parser import get_data
from triggers import LowTrigger,HighTrigger,AndTrigger,OrTrigger,NotTrigger
import numpy as np

class CurrencyDatabase:
  
  def __init__(self, start_date, end_date, trigger_list_path):

    self.start_date = self.conv2date(start_date)
    self.end_date = self.conv2date(end_date)
    self.market_open = np.zeros(self.date_cnt)
    self.currency_list = ['USD', 'AUD', 'DKK', 'EUR', 'GBP', 'CHF', 'SEK', 'CAD', 'KWD',
                            'NOK', 'SAR', 'JPY', 'BGN', 'RON', 'RUB', 'IRR', 'CNY', 'PKR']

    self.trigger_list = []
    self.analysis_list = []

    self.comp_trigger_list = []
    self.comp_analysis_list = []

    self.trigger_list_path = trigger_list_path

    self.db = {}

    for curr in self.currency_list:

      self.db[curr] = Currency(total_days=self.date_cnt, code=curr)

    # Get data from TCMB
    for i in range(self.date_cnt):

      date = self.start_date + datetime.timedelta(days=i)
      data_dict = get_data(date)

      # Check the dictionary is emtpy
      if bool(data_dict):

        # Market is open. TODO        
        self.market_open[i] = 1


      else:

        # Market is closed. TODO


      print("Database init completed.")
      print(f"Database interval: {self.start_date} - {self.end_date}")
      print(f"Fetched {self.date_cnt} days. Market is open {np.sum(self.market_open)} days.")
      print(f"There are {len(self.currency_list)} currencies.")
      print("---")

  @property
  def date_cnt(self):
    
    return # TODO

  def conv2date(self, date):

    date = # TODO

    return date

  def idx2date(self, idx):

    date = # TODO

    return date

  def date2idx(self, target_date):

    idx = # TODO

    assert idx >= 0, f'Date is out of range!'
    assert self.date_cnt >= idx, "Date is out of range!"

    return idx

  def set_triggers(self, trigger_list_path):

    with open(trigger_list_path, "r") as f:

      for line in f:

        # Read the line, parse as a list
        arg = line.rstrip().split()

        # Extract list
        trig_cls = arg[0] # Trigger class

        if trig_cls == "LOW":

          date_start_str = arg[4]
          date_end_str = arg[5]
          date_start_idx = self.date2idx(date_start_str.split('/'))
          date_end_idx = self.date2idx(date_end_str.split('/'))

          trigger = LowTrigger(func = arg[1], prop = arg[2], threshold = float(arg[3]),
                                date_start_idx=date_start_idx, date_end_idx=date_end_idx,
                                date_start_str = date_start_str, date_end_str = date_end_str)

        elif trig_cls == "HIGH":

          date_start_str = arg[4]
          date_end_str = arg[5]
          date_start_idx = self.date2idx(date_start_str.split('/'))
          date_end_idx = self.date2idx(date_end_str.split('/'))

          trigger = HighTrigger(func = arg[1], prop = arg[2], threshold = float(arg[3]),
                                date_start_idx=date_start_idx, date_end_idx=date_end_idx,
                                date_start_str = date_start_str, date_end_str = date_end_str)

        elif trig_cls == "NOT":

          trig_idx = int(arg[1])
          trigger = NotTrigger(self.trigger_list[trig_idx])

        elif trig_cls == "AND":

          trig_idx_1 = int(arg[1])
          trig_idx_2 = int(arg[2])
          trigger = AndTrigger(self.trigger_list[trig_idx_1], self.trigger_list[trig_idx_2])

        elif trig_cls == "OR":

          trig_idx_1 = int(arg[1])
          trig_idx_2 = int(arg[2])
          trigger = OrTrigger(self.trigger_list[trig_idx_1], self.trigger_list[trig_idx_2])

        print(f'Initialized trigger: {trigger}')
        self.trigger_list.append(trigger)

print("Initializing triggers complete!")
print("---")

  def run_triggers(self):

    """
    Runs triggers on a specific date interval.
    If start date is not set, it scans from the first day.
    If end date is not set, it scans to the end.
    If nothing has been set, it scans entire dataset.
    :param start_date: tuple ()
    :param end_date: tuple ()
    :return:
    """

    for trig in self.trigger_list:

        print(f'Evaluating trigger: {trig}')

        analysis = []

        for curr_code in self.currency_list:

            curr = self.db[curr_code]

            result = trig.evaluate(curr)

            if result:

                analysis.append(curr.code)

        self.analysis_list.append(analysis)

    print("Running triggers complete!")


    def analyze(self, trigger_list_path = False, debug = False):



      self.set_triggers(trigger_list_path=trigger_list_path)
      self.run_triggers()

      print(f'============Writing Report============')

      for idx, list in enumerate(self.analysis_list):

          if list:

              print(f"{idx + 1} - {self.trigger_list[idx]} is fired for: {list}")

          elif not list and debug:

              print(f"{idx + 1} - {self.trigger_list[idx]} is not fired!")


      print(f'==========End of the Report==========')
