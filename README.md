### Date created
2020-05-20

### Changelog

#### 1.0.0 - 2020-05-20

##### Added
- First stable version of tool

## BikeShare Data Analysis Tool

### Description
The program analyzes bike share data for a given city (Chicago, New York City, or Washington, DC). The user can optionally filter the data by a month and/or a day of week.

The program outputs statistical information about:

- Popular times of travel
- Popular stations and trips
- Trip duration
- User info

The user can also optionally view the raw data about the trips.

### Data Columns

The data files for the cities are not included in the repository, but they are based on the data provided by [Motivate](https://www.motivateco.com "Motivate website"). Links to the original data files are listed in Additional Sources.

The program reads CVS files and uses the following data columns:

- Start Time (date + time)
- End Time (date + time)
- Trip Duration (in seconds)
- Start Station
- End Station
- User Type

Optional data columns for users:
- Gender
- Birth Year

### Requirements

The program requires Python version 3 with [pandas package](https://pandas.pydata.org "pandas website") which is part of [Anaconda distribution](https://www.anaconda.com "Anaconda website").

### Files used
bikeshare.py

### Additional Sources

#### Original data files

1. Chicago: https://www.divvybikes.com/system-data

2. New York City: https://www.citibikenyc.com/system-data

3. Washington, DC: https://www.capitalbikeshare.com/system-data

### Acknowledges

1. Keep a Changelog https://keepachangelog.com/en/1.0.0/

2. Markdown Syntax https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf
