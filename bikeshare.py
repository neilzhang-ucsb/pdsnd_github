import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june','all']
days=["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday",'all']

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
    while True:
        city=str(input('Please choose the city you want to look at (chicago, new york city, washington).')).lower()
        if city in CITY_DATA.keys():
            break
        else:
            print('That is not a valid city name')

    while True:
        filt=str(input('Would you like to filter the data by month, day, or not at all (month, day, none)?')).lower()
        if filt in ['month', 'day', 'none']:
            break
        else:
            print('That is not a valid city name')  
            
    day='all'        
    month='all'
    if filt=='month':    
        # TO DO: get user input for month (all, january, february, ... , june)
        while True:
            month=str(input('Please choose the month (january to june) you want to look at, or type in \'all\' for any months.')).lower()
            if month in months:
                break
            else:
                print('That is not a valid month')
    elif filt=='day':       
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        while True:
            day=str(input('Please choose the day of week (monday to sunday) you want to look at, or type in \'all\' for any day.')).lower()
            if day in days:
                break
            else:
                print('That is not a valid day')

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
    while True:
        try:
            df = pd.read_csv(CITY_DATA[city])
            break
        except:
            print("Oops!  City file doesn't exist.  Try again...")

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Frequent Start Month:', months[popular_month-1].title())

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Frequent Start Day:', popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*45)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    df['start and end']=df['Start Station']+'  -  '+df['End Station']
    
    # TO DO: display most commonly used start station
    popular_start=df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', popular_start)
    # TO DO: display most commonly used end station
    popular_end=df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    popular_combination=df['start and end'].mode()[0]
    print('Most Commonly Used Combination of Start and End Station:', popular_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*45)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Travel Time:', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Mean Travel Time::', df['Trip Duration'].mean(skipna = True))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User Types Counts:\n', df['User Type'].value_counts(),'\n')
    
    try:
        # TO DO: Display counts of gender
        print('Gender Counts:\n', df['Gender'].value_counts(),'\n')

        # TO DO: Display earliest, most recent, and most common year of birth
        print('Earliest Year of Birth:\n', int(df['Birth Year'].min()))
        print('Most Recent Year of Birth:\n', int(df['Birth Year'].max()))
        print('Most Common Year of Birth:\n', int(df['Birth Year'].mode()[0]))
    except:
        print('Do not have Gender and Year of Birth imformation.')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """
    Asks user if they want to see 5 lines of raw data.
    Returns the 5 lines of raw data if user inputs `yes`. Iterate until user response with a `no`

    """

    count = 0

    while True:
        answer = input('Would you like to see 5 lines of raw data? Enter yes or no: ')
        # Check if response is yes, print the raw data and increment count by 5
        if answer=='yes':
            print(df[count:count+5])
            count=count+5
        # otherwise break
        else:
            break
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        df_copy=df.copy()
        
        time_stats(df_copy)
        station_stats(df_copy)
        trip_duration_stats(df_copy)
        user_stats(df_copy)
        raw_data(df)

        # Ask user whether to restart   
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
