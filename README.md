### Date created
2020-05-20

## BikeShare Data Analysis

### Description
The program analyzes bike share data for a given city (Chicago, New York City, or Washington, DC). The user can optionally filter the data by a month and/or a day of week.

The program outputs statistical information about times, stations, trip durations and users. The user can also optionally view the raw data about the trips.

The data files for the cities are not included in the repository, but they are based on the data provided by [Motivate][1].

[1]: [https://www.motivateco.com]

### Files used
bikeshare.py

### Credits

#### Original data files

1. Chicago: https://www.divvybikes.com/system-data

2. New York City: https://www.citibikenyc.com/system-data

3. Washington, DC: https://www.capitalbikeshare.com/system-data

#### Sources

1. Convert time to 12h format
* https://stackoverflow.com/questions/13855111/how-can-i-convert-24-hour-time-to-12-hour-time
* https://strftime.org

2. Group Pandas dataframe columns
* https://stackoverflow.com/questions/53037698/how-can-i-find-the-most-frequent-two-column-combination-in-a-dataframe-in-python

3. Add a thousand separator in output
* https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-35.php

4. Ignore exceptions properly
* https://stackoverflow.com/questions/730764/how-to-properly-ignore-exceptions

5. Handling different outputs of timedelta class
* https://www.reddit.com/r/learnpython/comments/23yu5j/how_come_my_datetimetimedelta_object_has_no_hours/

6. JSON output for Pandas dataframe
* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html
