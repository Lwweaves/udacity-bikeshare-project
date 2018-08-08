"""
    References used for help and ideas(no 'copy and pasting' done) --
        - https://github.com/xhlow/udacity-bikeshare-project
        - https://github.com/philribbens/udacity-bikeshare-project
        - https://stackoverflow.com/
        - https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
"""

import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """


    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                     'Would you like to see data for Chicago, New York, or Washington?\n').title()
        if city == 'Chicago':
            city = 'chicago'
            break
        elif city == 'New York':
            city = 'new york city'
            break
        elif city == 'Washington':
            city = 'washington'
            break
        else:
            print("\nI'm sorry, I'm not sure which city you're referring to. Let's try again.")



    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nBetween January - June, which month would like to see data for? Say 'all' to see data for all months:\n").title()
        if month == 'January':
            month = 'January'
            break
        elif month == 'February':
            month = 'February'
            break
        elif month == 'March':
            month = 'March'
            break
        elif month == 'April':
            month = 'April'
            break
        elif month == 'May':
            month = 'May'
            break
        elif month == 'June':
            month = 'June'
            break
        elif month == 'All':
            month = 'All'
            break
        else:
            print("Try again. Please enter a month from January through June.")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\nWhat day of the week?: \n").lower()
        if day == 'monday':
            day = 'monday'
            break
        elif day == 'tuesday':
            day = 'tuesday'
            break
        elif day == 'wednesday':
            day = 'wednesday'
            break
        elif day == 'thursday':
            day = 'thursday'
            break
        elif day == 'friday':
            day = 'friday'
            break
        elif day == 'saturday':
            day = 'saturday'
            break
        elif day == 'sunday':
            day = 'sunday'
            break
        else:
            print("Try again. Please enter a day of the week, Monday - Sunday")


    print('-'*40)
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
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        #filter by month to create the new dataframe
        df = df[df['month'] == month]

    elif month == 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = len(months)

        #filter by month to create the new dataframe
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

    # TO DO: display the most common month
    # using 'calendar' package to easily get name of month
    common_month = df['month'].mode()[0]
    print("Most common month for travel: " + calendar.month_name[int(common_month)])

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("Most common day of the week: " + common_day)

    # TO DO: display the most common start hour
    # added formatting to show AM or PM
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    if common_start_hour < 12:
        am_pm = 'am'
    elif common_start_hour > 12:
        am_pm = 'pm'
        common_start_hour = common_start_hour - 12
    else:
        am_pm = 'pm'
        common_start_hour = 12
    print("Most common start hour: {}{}".format(common_start_hour, am_pm))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # count total number of start stations
    start_station_count = df.groupby('Start Station')['Start Station'].count()

    #order the start stations in descending order
    descending_start_station_count = start_station_count.sort_values(ascending=False)

    #display the start station with the most amount of starting trips. Along with the total number.
    pop_start_station = descending_start_station_count.index[0] + ": " + str(descending_start_station_count[0])
    print("Most commonly used start station...\n" + pop_start_station)

    print('-'*10)

    # TO DO: display most commonly used end station
    #count number of end stations using groupby method
    end_station_count = df.groupby('End Station')['End Station'].count()

    #put in descending order
    descending_end_station_count = end_station_count.sort_values(ascending=False)

    #display most popular end station and count
    pop_end_station = descending_end_station_count.index[0] + ": " + str(descending_end_station_count[0])
    print("Most commonly used end station...\n" + pop_end_station)

    print('-'*10)

    # TO DO: display most frequent combination of start station and end station trip
    # first, count total number of trip counts for each station
    trip_counts = df.groupby(['Start Station', 'End Station'])['Start Time'].count()

    # sort in descending order
    sorted_trip_stations = trip_counts.sort_values(ascending=False)


    # display the start and end stations with the most trips. Displaying first element.
    print("Most popular trip: " + "\n  The beginning station of the trip began at: " + str(sorted_trip_stations.index[0][0]) + "\n  The ending station of the trip ended at: " + str(sorted_trip_stations.index[0][1]) + "\n  There were " + str(sorted_trip_stations[0]) +  " total trips")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = round(df['Trip Duration'].sum())
    #get minutes and seconds by dividing travel time by 60
    minute, second = divmod(total_travel_time, 60)
    hour, minute = divmod(minute, 60)
    print("Total travel time: {} hours, {} minutes, {} seconds".format(hour, minute, second))

    # TO DO: display mean travel time
    avg_travel_time = round(df['Trip Duration'].mean())
    m, s = divmod(avg_travel_time, 60)
    h, m = divmod(m, 60)
    print("Average travel time: {} hours, {} minutes, {} seconds".format(h, m, s))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of different user types: \n" + str(user_types))
    print('-'*10)

    # TO DO: Display counts of gender
    if city != 'washington':
        gender_count = df['Gender'].value_counts()
        print("Counts of gender: \n" + str(gender_count))
        print('-'*10)


    elif city == 'washington':
        print("\nGender statistics not available for Washington dataset.\n")


    # TO DO: Display earliest, most recent, and most common year of birth
    # earliest birth year...
    if city != 'washington':
        earliest_birth_year = df['Birth Year'].min()
        print("Earliest year of birth: \n" + str(earliest_birth_year))
        print('--'*10)

        #most recent birth year...
        recent_birth_year = df['Birth Year'].max()
        print("Most recent birth year: \n" + str(recent_birth_year))
        print('-'*10)

        #most common year of birth...
        common_birth_year = df['Birth Year'].mode()
        print("Most common birth year: \n" + str(common_birth_year))


    elif city == 'washington':
        print("\nBirth year statistics not available for Washington dataset.\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



counter = 0
def display_data(df, counter):
    see_data = input('\nWould you like to see raw trip data?'
                    ' Type \'yes\' or \'no\'.\n')
    see_data = see_data.lower()

    if see_data == 'yes':
        print(df.iloc[counter:counter+10])
        counter += 10
        return display_data(df, counter)
    elif see_data == 'no':
        return
    else:
        print("\nTry again")
        return display_data(df, counter)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df, counter)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
