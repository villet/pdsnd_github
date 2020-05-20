from datetime import datetime
from datetime import timedelta
import time
import sys
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS_OF_WEEK = ['monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    # Info text
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get user input for city
    city = get_city_input()

    # Get user input for time filter
    filter_type = get_filter_input()

    # Get user input for month

    month = 'all' # defaults to no filter
    if filter_type in ('month', 'both'):
        month = get_month_input()

    day = 'all' # defaults to no filter
    # Get user input for day of week (dow)
    if filter_type in ('day', 'both'):
        day = get_dow_input()

    # Wait for 2 seconds so the user can read the output
    time.sleep(2)

    print('-' * 40)

    return city, month, day


def get_city_input():
    """
    Asks user a city and validates the input against CITY_DATA dict

    Returns:
        (str) city - name of the city to analyze
    """

    # Info text
    print('\nBegin by selecting a city. \nThe options are ', end='')
    print_list(CITY_DATA)
    print('\nOr type "x" to exit the program.')

    # Process input
    city = None
    valid_input = False
    while not valid_input:
        city = input('Enter your choice: ').lower()
        if city == 'x':
            exit_with_message()
        elif CITY_DATA.get(city):
            valid_input = True
        else:
            print('\nInvalid input:', city, '\nThe options are ', end='')
            print_list(CITY_DATA)
            print('\nOr type "x" to exit the program.')

    # Confirm input
    print('\n->', city.title(), 'selected as the city.\n')

    return city


def get_filter_input():
    """
    Asks user a type of filtering and validates the input

    Returns:
        (str) filter_type - name of time filtering
    """

    print('Would you like to filter the data by month, day, both, or not at all?')
    print('Type "none" for no time filter.', end=' ')
    print('Or type "x" to exit the program.')

    # Process input
    filter_type = None
    valid_input = False
    while not valid_input:
        filter_type = input('Enter your choice: ').lower()
        if filter_type == 'x':
            exit_with_message()
        elif filter_type == 'month':
            print('\n->', filter_type.title(),
                  'selected. Data will be filtered by a month.\n')
            valid_input = True
        elif filter_type == 'day':
            print('\n->', filter_type.title(),
                  'selected. Data will be filtered by a week of day.\n')
            valid_input = True
        elif filter_type == 'both':
            print('\n->', filter_type.title(),
                  'selected. Data will be filtered both by a month, and a week of day.\n')
            valid_input = True
        elif filter_type == 'none':
            print('\n->', filter_type.title(),
                  'selected. No time filter will be applied.\n')
            valid_input = True
        else:
            print('\nInvalid input:', filter_type)
            print('The options are month, day, both, or none.', end=' ')
            print('\nOr type "x" to exit the program.')

    return filter_type

def get_month_input():
    """
    Asks user a month and validates the input against available months

    Returns:
        (str) month - name of the month to filter by
    """

    # Info text
    print('Choose a month to apply the time filter.\nThe options are', end=' ')
    print_list(MONTHS)
    print('\nOr type "x" to exit the program.')

    # Process input
    month = None
    valid_input = False
    while not valid_input:
        month = input('Enter your choice: ').lower()

        if month == 'x':
            exit_with_message()
        elif month in MONTHS:
            valid_input = True
        else:
            print('\nInvalid input:', month, '\nThe options are', end=' ')
            print_list(MONTHS)
            print('\nOr type "x" to exit the program.')

    # Confirm input
    print('\n->', month.title(), 'selected. Data will be filtered by the selected month.\n')

    return month


def get_dow_input():
    """
    Asks users a day of week (dow) and validates the input

    Returns:
        (str) day - name of the day of week to filter by
    """

    # Info text
    print('Choose a week of day to apply the time filter.\nThe options are', end=' ')
    print_list(DAYS_OF_WEEK)
    print('\nOr type "x" to exit the program.')

    # Process input
    day = None
    valid_input = False
    while not valid_input:
        day = input('Enter a day of week: ').lower()

        if day == 'x':
            exit_with_message()
        elif day in DAYS_OF_WEEK:
            valid_input = True
        else:
            print('\nInvalid input:', day, '\nThe options are', end=' ')
            print_list(DAYS_OF_WEEK)
            print('\nOr type "x" to exit the program.')

    # Confirm input
    print('\n->', day.title(), 'selected. Data will be filtered by the selected week of day.\n')

    return day


def print_list(items):
    """
    Prints word list separated by commas and "or" before the last word

    Args:
        (list/dict) items - words to be combined
    """

    for i, item in enumerate(items):
        if i == len(items) - 1:
            print(item.title(), end=".")
        elif i == len(items) - 2:
            print(item.title(), end=", or ")
        else:
            print(item.title(), end=", ")


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        dframe - Pandas DataFrame containing city data filtered by month and day
    """

    # Load data file into a dataframe
    dframe = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    dframe['Start Time'] = pd.to_datetime(dframe['Start Time'])
    dframe['End Time'] = pd.to_datetime(dframe['End Time'])

    # Extract month and day of week and create new columns
    dframe['month'] = dframe['Start Time'].dt.month
    dframe['day_of_week'] = dframe['Start Time'].dt.day_name()

    # Filter by month if applicable
    if month != 'all':
        month = MONTHS.index(month) + 1
        dframe = dframe[dframe['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        dframe = dframe[dframe['day_of_week'] == day.title()]

    return dframe


def time_stats(dframe, month, day):
    """
    Displays statistics on the most frequent times of travel.

    Args:
        (df) dframe - bikeshare usage data
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    top_month = dframe['month'].mode()[0]
    top_month_occ = dframe['month'].value_counts().max()
    print('Most frequent travel month:', MONTHS[top_month - 1].title(), end=' ')

    # - Adding thousand separator to numbers [3]
    if month == 'all':
        print('(count: {:,}'.format(top_month_occ) + ')')
    else:
        print('(count: {:,}'.format(top_month_occ) + ') NOTE: month filter applied')

    # Display the most common day of week
    top_dow = dframe['day_of_week'].mode()[0]
    top_dow_occ = dframe['day_of_week'].value_counts().max()
    print('Most frequent travel day of week:', top_dow, end=' ')

    if day == 'all':
        print('(count: {:,}'.format(top_dow_occ) + ')')
    else:
        print('(count: {:,}'.format(top_dow_occ) + ') NOTE: day of week filter applied')

    # Display the most common start hour
    dframe['hour'] = dframe['Start Time'].dt.hour
    top_hour = dframe['hour'].mode()[0]
    top_hour_occ = dframe['hour'].value_counts().max()

    # - Converting to 12h format
    top_hour = datetime.strptime(str(top_hour), '%H').strftime('%-I %p')
    print('Most frequent travel start hour:', top_hour, end=' ')
    print('(count: {:,}'.format(top_hour_occ) + ')')

    print("\nThis took %.2f seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(dframe):
    """
    Displays statistics on the most popular stations and trip.

    Args:
        (df) dframe - bikeshare usage data
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    top_start_station = dframe['Start Station'].mode()[0]
    top_start_station_occ = dframe['Start Station'].value_counts().max()
    print('Most frequent start station:', top_start_station, end=' ')
    print('(count: {:,}'.format(top_start_station_occ) + ')')

    # Display most commonly used end station
    top_end_station = dframe['End Station'].mode()[0]
    top_end_station_occ = dframe['End Station'].value_counts().max()
    print('Most frequent end station:', top_end_station, end=' ')
    print('(count: {:,}'.format(top_end_station_occ) + ')')

    # Display most frequent combination of start station and end station trip
    # - Grouping Start and End Station columns [2]
    top_trip = dframe.groupby(['Start Station', 'End Station']).size().idxmax()
    top_trip_occ = dframe.groupby(['Start Station', 'End Station']).size().max()
    print('Most frequent trip:', top_trip[0], '-', top_trip[1], end=' ')
    print('(count: {:,}'.format(top_trip_occ) + ')')

    print("\nThis took %.2f seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(dframe):
    """
    Displays statistics on the total and average trip duration.

    Args:
        (df) dframe - bikeshare usage data
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = dframe['Trip Duration'].sum()
    total_travel_time = timedelta(seconds=int(total_travel_time))
    print('Total travel time:', end=' ')
    print_duration(total_travel_time)

    # Display mean travel time
    average_travel_time = dframe['Trip Duration'].mean()
    average_travel_time = timedelta(seconds=int(average_travel_time))
    print('Average travel time:', end=' ')
    print_duration(average_travel_time)

    print("\nThis took %.2f seconds." % (time.time() - start_time))
    print('-'*40)

def print_duration(duration):
    """
    Prints timedelta in more human readable format.

    Args:
        (timedelta/float/int) duration - time in days hh:mm:ss or s (float/int)
    """

    # Process if days are present [4]
    try:
        if duration.days > 0:
            if duration.days != 1:
                print('{:,}'.format(duration.days), 'days ', end='')
            else:
                print('%s day ' % duration.days, end='')
    except AttributeError:
        pass

    # Process hours, minutes and seconds [5]
    hours, minutes, seconds = 0, 0, 0

    try:
        # - If hours>0 (hh:mm:ss format)
        seconds = duration.seconds
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
    except AttributeError:
        # - If hours=0 (seconds float/int format)
        seconds = duration

    if hours != 1:
        print('%s hrs ' % hours, end='')
    else:
        print('%s hr ' % hours, end='')

    if minutes != 1:
        print('%s mins ' % minutes, end='')
    else:
        print('%s min ' % minutes, end='')

    if seconds != 1:
        print('%s secs' % seconds)
    else:
        print('%s sec' % seconds)


def user_stats(dframe):
    """
    Displays statistics on bikeshare users.

    Args:
        (df) dframe - bikeshare usage data
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User type distribution:')
    user_types = dict(dframe['User Type'].value_counts())
    print_distribution(user_types)

    # Display counts of gender (if available)
    if 'Gender' in dframe.columns:
        print('\nGender distribution:')
        gender_types = dict(dframe['Gender'].value_counts())
        print_distribution(gender_types)
    else:
        print('\nNOTE: Gender data not available for the selected city.')

    # Display earliest, most recent, and most common year of birth (if available)
    if 'Birth Year' in dframe.columns:
        print('\nYear of birth:')
        print('- Oldest user was born in %d' % dframe['Birth Year'].min())
        print('- Youngest user was born in %d' % dframe['Birth Year'].max())
        print('- Most common birth year is %d' % dframe['Birth Year'].mode()[0])
    else:
        print('\nNOTE: Year of birth data not available for the selected city.')

    print("\nThis took %.2f seconds." % (time.time() - start_time))
    print('-'*40)


def print_distribution(dist_data):
    """
    Prints a formatted distribution list

    Args:
        (dict) dist_data - distribution of data entries
    """

    for key in dist_data.keys():
        print('- ' + key + ': {:,}'.format(dist_data[key]))

def raw_trip_data(city):
    """
    Shows raw trip data at 5 rows at the time

    Args:
        (str) city - name of the city
    """

    # Info text
    print('\nWould you like to see raw trip data? Type "yes" or "no".')
    print('Or type "x" to exit the program.')

    # Process input for first selection
    answer = None
    valid_input = False
    dframe_raw = None

    while not valid_input:
        answer = input('Enter your choice: ').lower()
        if answer == 'x':
            exit_with_message()
        elif answer == 'yes':
            print('\n-> Yes selected. Showing first five trips.\n')
            # Load original data file into new dataframe
            dframe_raw = pd.read_csv(CITY_DATA[city])
            valid_input = True
        elif answer == 'no':
            print('\n-> No selected. Skipping trip data output.')
            valid_input = True
        else:
            print('\nInvalid input:', answer, '\nThe options are "yes" or "no".')
            print('Or type "x" to exit the program.')

    # Process and show output for next inputs
    first_shown_row = 0
    while answer == 'yes':
        # Print five rows at the times [6]
        print(dframe_raw[first_shown_row:first_shown_row + 5]
              .to_json(orient='records', indent=2, date_format='iso'))

        print('\nWould you like to see more data? Type "yes" or "no"')
        print('Or type "x" to exit the program.')

        valid_input = False
        while not valid_input:
            answer = input('Enter your choice: ').lower()
            if answer == 'x':
                exit_with_message()
            elif answer == 'yes':
                print('\n-> Yes selected. Showing next five trips.\n')
                valid_input = True
            elif answer == 'no':
                print('\n-> No selected. Exiting trip data output.')
                valid_input = True
            else:
                print('\nInvalid input:', answer, '\nThe options are "yes" or "no".')
                print('Or type "x" to exit the program.')

        first_shown_row += 5

def exit_with_message():
    """ Exit program with a message """

    print('\nExiting program. Goodbye!')
    sys.exit(0)


def main():
    while True:
        city, month, day = get_filters()
        dframe = load_data(city, month, day)

        time_stats(dframe, month, day)
        station_stats(dframe)
        trip_duration_stats(dframe)
        user_stats(dframe)
        raw_trip_data(city)

        print('\nWould you like to restart? Enter "yes" or "no".')
        restart = input('Enter your choice: ')
        if restart.lower() != 'yes':
            exit_with_message()
        else:
            print('\n-> Restart selected.\n')


if __name__ == "__main__":
    main()
