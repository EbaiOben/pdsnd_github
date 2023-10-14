import time
import pandas as pd
#import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}

#added to verify user input for these options
MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
WEEKDAYS = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('\nWould you like to view data for chicago, new york city, or washington)?\n')
    while city.lower() not in CITY_DATA.keys():
        print("\nOops! looks like you entered an invalid city name")
        city = input('Re-enter your city of choice: chicago, new york city, washington?\n')

    print("\nYou've chosen to explore data for {}\n".format(city.lower()))
    data_filter = input("Would you like to filter the data just by month, day or both or none?\n")

    while data_filter.lower().strip() not in ['day', 'month', 'both', 'none']:
        print("Invalid data filter option\n")
        data_filter = input("Would you like to filter the data just by month, day or both or not at all(none)?\n")

    #All data, no filtering
    if data_filter.lower().strip() == 'none':
        month = 'all'
        day = 'all'

    #filtering just for month
    if data_filter.lower().strip() == 'month':
        day = 'all'
        # TO DO: get user input for month (all, january, february, ... , june)
        month = input('\nEnter a month of choice from: all, january, february, ... , june.\n')

        while month.lower().strip() not in MONTHS :
            print("\nInvalid month option")
            month = input('Re-enter your month of choice from: all, january, february, ... , june.\n')


    #filtering just for weekday
    if data_filter.lower().strip() == 'day':
        month = 'all'
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('\nEnter a week day of choice; all, monday, tuesday, ... sunday.\n')

        while data_filter.lower().strip() not in WEEKDAYS :
            print("\nInvalid weekday option ")
            day = input('Re-enter your weekday of choice from: all, monday, tuesday, ... sunday.\n')

    if data_filter.lower().strip() == 'both':
        # TO DO: get user input for month (all, january, february, ... , june)
        month = input('\nEnter a month of choice from: all, january, february, ... , june.\n')

        while  month.lower().strip() not in MONTHS :
            print("\nInvalid month option")
            month = input('Re-enter your month of choice from: all, january, february, ... , june.\n')

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('\nEnter a week day of choice; all, monday, tuesday, ... sunday.\n')

        while  day.lower().strip() not in WEEKDAYS :
            print("\nInvalid weekday option ")
            day = input('Re-enter your weekday of choice from: all, monday, tuesday, ... sunday.\n')

    print("\nExploring data of city: {} with a selected month option: {} and weekday: {}\n".format(city.lower(), month.lower(), day.lower()))

    print('-'*40)
    return city.lower(), month.lower(), day.lower()


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
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all' :
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all' :
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = MONTHS[df['month'].mode()[0]]
    print("\nThe most common month of travel is: \n", common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("\nThe most common week day of travel is: \n", common_day)

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("\nThe most common start hour is: \n", common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("\n The most commonly used start station is: \n", common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("\n The most commonly used end station is: \n", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_stations = (df['Start Station'] + ' ' + ['End Station']).mode()[0]
    print("Most combination of start station and end station trip is: \n", common_stations )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is: \n", total_travel_time)

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is: \n", avg_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city): #city parameter added to handle the fact that gender and birth year columns ain't found in washington DB
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print("\nThe count per user type is: \n", user_type_count )

    # TO DO: Display counts of gender
    if city != 'washington': #gender and birth year columns not in washington DB
        gender_count = df['Gender'].value_counts()
        print("\nThe count per gender type is: \n", gender_count )

        # TO DO: Display earliest, most recent, and most common year of birth
        print("\nThe earliest year of birth is: \n", df['Birth Year'].min())
        print("\nThe most recent year of birth is: \n", df['Birth Year'].max())
        print("\nThe most common year of birth is: \n", df['Birth Year'].mode()[0])

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        raw_data = input('\n Would you like to view raw data?, Enter yes or no\n')
        if raw_data.lower().strip() != 'yes':
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower().strip() != 'yes':
                break
            else:
                main()

        else:
            count = 1
            row_range = 5
            pd.set_option('display.max_columns', 10)
            print("\n Displaying raw data\n", df.head(row_range))
            more_data = input('\nWould you like to view more data rows? Enter yes or no\n')

            if more_data.lower().strip() != 'yes':
                restart = input('\nWould you like to restart? Enter yes or no.\n')
                if restart.lower().strip() != 'yes':
                    break
                else:
                    main()

            else:
                while more_data.lower().strip() == 'yes':
                    count += 1
                    pd.set_option('display.max_columns', 10)
                    print("\n Displaying more raw data rows \n", df.head(row_range*count))
                    more_data = input('\n Would you like to view more data rows? Enter yes or no\n')

                    if more_data.lower().strip() != 'yes':
                        restart = input('\nWould you like to restart? Enter yes or no.\n')
                        if restart.lower().strip() != 'yes':
                            break
                        else:
                            main()



if __name__ == "__main__":
	main()
