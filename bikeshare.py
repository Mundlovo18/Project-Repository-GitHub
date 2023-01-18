import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

cities = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington).            
    while True:
        city = input('Which city you want to analyse, between Chicago, New York City and Washington: ').lower()
        if city not in cities:
            print('Invalid city name. please try Again'  )
           
        else:
            break
        
    # get user input for month (all, january, february, ... , june)
    month = input('Choose the month from January to June or choose all for no month filter: ').lower()
    if month not in months:
        month = input('Invalid month name. please try Again  ').lower()
    # get user input for day of week (all, monday, tuesday, ... sunday)n
    
    day = input('Choose the day of the week or choose all for no day name filter: ').lower()
    if day not in days:
        day = input('Invalid day of the weeek. please try Again  ').lower()
    print('-'*40)
    return city, month, day
    def raw_data(df):
        ask_user = input('Would you like to view more raw data for the city selected? \nPrint yes or no: ')

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

    # filter by month 
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week 
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month
    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month
    # find the most common month of the year (from 1 to 12)
    common_month = df['month'].mode()[0]
    print('Most Common month:', common_month)

    # display the most common day of week
    
    # extract dayofweek from the Start Time column to create a day_of_week column
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    # find the most common day of the week (from 0 to 6)
    common_day = df['day_of_week'].mode()[0]
    print('Most Frequent Day:', days[common_day])

    # display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour (from 0 to 23)
    common_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('\nMost Commonly used start station:', Start_Station)
    # display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', End_Station)
    # display most frequent combination of start station and end station trip
    print('Most Commonly used combination of start station and end station trip:')
    most_common_start_and_end_stations = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print(most_common_start_and_end_stations)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.  """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total Travel Time:', df['Trip Duration'].sum())
    # display mean travel time
    print('Mean Travel Time:', df['Trip Duration'].mean())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    while 'Gender' in df.columns:
        # Display counts of gender
        gender = df['Gender'].value_counts()
        print(gender)
        break
        
    while 'Birth Year' in df.columns:
        # Display earliest, most recent, and most common year of birth
        print('Earliest year of Birth:', df['Birth Year'].min())
        print('Most Recent year of Birth:', df['Birth Year'].max())
        print('Most Common year of Birth:', df['Birth Year'].mode()[0])
        break    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 

    # Ask user if they want to see individual trip data.
    start_data = 0
    end_data = 5
    df_length = len(df.index)
    
    while start_data < df_length:
        raw_data = input('\nWould you like to see the 5 lines of raw data (yes or no):\n').lower() 
        if raw_data == 'yes':
            
            print("\nDisplaying only 5 rows of data in esch turn.\n")
            if end_data > df_length:
                end_data = df_length
            print(df.iloc[start_data:end_data])
            start_data += 5
            end_data += 5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()