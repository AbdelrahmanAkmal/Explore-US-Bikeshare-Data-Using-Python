import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def check_filters(input_str, input_type):
    while True:
        user_input = input(input_str)
        try:
            if user_input in ['chicago', 'new york city', 'washington'] and input_type == 'city':
                break
            elif user_input in ['january', 'february', 'march', 'april', 'may', 'june',
                                'all'] and input_type == 'month':
                break
            elif user_input in ['sunday', 'monday', 'thuesday', 'wednesday', 'thursday', 'friday', 'saturday',
                                'all'] and input_type == 'day':
                break
            else:
                if input_type == 'city':
                    print('Please choose a city only from the following list [Chicago, New York City, Washington]')
                if input_type == 'month':
                    print(
                        'Please choose a month only from the following list [january,february,march,april,may,june,all]')
                if input_type == 'day':
                    print(
                        'Please choose a day only from the following list [sunday,monday,thuesday,wednesday,thursday,friday,saturday,all]')
        except ValueError:
            print('Your Entry is Unacceptable, Please try again!')
    return user_input


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city = check_filters('Please Choose a city from chicago, new york city, washington to view its data. \n', 'city')
    month = check_filters(
        "Please Select a month to filter the data with, ex. january, or type 'all' to select all monthes. \n", 'month')
    day = check_filters("Please Select a day to filter the data with, ex. sunday, or type 'all' to select all days. \n",
                        'day')

    print('-' * 80)
    print(f'You have choosed {city}, {month}, {day}')

    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime("%A")
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is', common_month)

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day is', common_day)

    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The most common start hour is', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 80)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most common used start station is ', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most common used end station is ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = df.groupby(['Start Station', 'End Station'])
    common_stations_combinations = frequent_combination.size().sort_values(ascending=False).head(4)
    print('Most frequent combination of Start Station and End Station trip:\n', common_stations_combinations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 80)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The Total travel time is', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The Mean travel time is', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 80)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User Types Statistics: \n')
    x = df['User Type'].value_counts()
    print(x)
    # TO DO: Display counts of gender
    if city != 'washinghton':
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)
        # TO DO: Display earliest, most recent, and most common year of birth
        most_common_birthyear = int(df['Birth Year'].mode()[0])
        print('Most Common Birth Year is', most_common_birthyear)
        earliest_birthyear = int(df['Birth Year'].min())
        print('Earliest Birth Year is', earliest_birthyear)
        recent_birthyear = int(df['Birth Year'].min())
        print('Most Recent Birth Year is', recent_birthyear)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 80)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()