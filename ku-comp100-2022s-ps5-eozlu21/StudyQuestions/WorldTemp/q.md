## History of Earth's Temperature

According to the [climate.gov](https://www.climate.gov/news-features/videos/history-earths-temperature-1880),
"*temperatures measured on land and at sea for more than a century show that Earth's globally averaged surface temperature is experiencing a long-term warming trend. Though warming has not been uniform across the planet, more areas are warming than cooling.*"

In the `WorldTemp` folder, we downloaded some regional anomalies in temperature with respect to the 1910 to 2000 average as a time series over the years from [this source](https://www.ncdc.noaa.gov/cag/global/time-series/globe/land/ytd/12/1880-2013?trend=true&trend_base=10&firsttrendyear=1976&lasttrendyear=2013). 

In Q4.py, we provide a function to load a regional data as a list of lists `all_region_temps`. 

1. Unfortunately for us, these anomalies follow an upward trend, or in other words, they are *almost* sorted in increasing order. Almost sorted means that there is a steady increase in the temperature anomaly but the numbers are not exactly in increasing order over the years. Propose and implement an efficient sort algorithm for a region by assuming that anomalies are sorted across short periods of time such as decades. Anomalies within a decade might be unsorted but all the anomalies in a decade is guaranteed to be less than all the other anomalies in the following decades as shown in the example below. In other words, an anomaly in a region is at most 10 years away from its original position in the whole sorted data. Given the number of measurements as `N` and the length of the period as `p`, e.g. `p = 10` in case of a decade, report the time complexity of your algorithm in terms of `N` and `p`, please be as exact as possible.

A small example with 4 decades of artificial data where each decade is unsorted within itself but 
- the first decade values are smaller than the second, the third, and the fourth decade values, 
- the second decade values are smaller than the third and the fourth decade values,
- and the third decade values are smaller than the fourth decade values.

```
  [4, 3, 6, 8, 5, 10, 1, 9, 7, 2, 
   13, 16, 19, 15, 20, 12, 17, 18, 11, 14, 
   27, 23, 26, 28, 25, 30, 21, 24, 29, 22,
   42, 47, 44, 50, 45, 48, 41, 46, 43, 49]
```

**Hint:** You can call the the `merge_sort` provided for you, maybe *multiple times*.

2. Given a set of sorted regional measurements, we are interested in combining them into a single global measurement. Propose an efficient algorithm to combine `r` sorted regional measurements where each is length `N`, and report its time complexity in terms of `N` and `r`.

**Hint:** Think about the `merge` of the `merge_sort`. If you keep merging sorted regions in pairs, you reach r/2 regions in the first pass, r/4 regions in the second pass, r/8 in the third and so on. How many passes do you need to make like that?


