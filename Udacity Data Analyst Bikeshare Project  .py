{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "ef8afee8-6f92-458e-af29-1413d72c08a8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "e9f448d2-749d-4f69-b5dc-8c04c8e089b5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello! Let's explore some US bikeshare data!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please Choose a city from chicago, new york city, washington to view its data. \n",
      " new york city\n",
      "Please Select a month to filter the data with, ex. january, or type 'all' to select all monthes. \n",
      " january\n",
      "Please Select a day to filter the data with, ex. sunday, or type 'all' to select all days. \n",
      " all\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--------------------------------------------------------------------------------\n",
      "You have choosed new york city, january, all\n",
      "\n",
      "Calculating The Most Frequent Times of Travel...\n",
      "\n",
      "The most common month is 1\n",
      "The most common day is Thursday\n",
      "The most common start hour is 8\n",
      "\n",
      "This took 0.00498199462890625 seconds.\n",
      "--------------------------------------------------------------------------------\n",
      "\n",
      "Calculating The Most Popular Stations and Trip...\n",
      "\n",
      "The most common used start station is  Pershing Square North\n",
      "The most common used end station is  Pershing Square North\n",
      "Most frequent combination of Start Station and End Station trip:\n",
      " Start Station          End Station                 \n",
      "E 7 St & Avenue A      Cooper Square & E 7 St          25\n",
      "N 6 St & Bedford Ave   Wythe Ave & Metropolitan Ave    21\n",
      "W 21 St & 6 Ave        9 Ave & W 22 St                 20\n",
      "Pershing Square North  E 24 St & Park Ave S            18\n",
      "dtype: int64\n",
      "\n",
      "This took 0.015961170196533203 seconds.\n",
      "--------------------------------------------------------------------------------\n",
      "\n",
      "Calculating Trip Duration...\n",
      "\n",
      "The Total travel time is 23730278\n",
      "The Mean travel time is 744.315852205006\n",
      "\n",
      "This took 0.0010075569152832031 seconds.\n",
      "--------------------------------------------------------------------------------\n",
      "\n",
      "Calculating User Stats...\n",
      "\n",
      "User Types Statistics: \n",
      "\n",
      "Subscriber    30740\n",
      "Customer        985\n",
      "Name: User Type, dtype: int64\n",
      "Male      23811\n",
      "Female     6696\n",
      "Name: Gender, dtype: int64\n",
      "Most Common Birth Year is 1985\n",
      "Earliest Birth Year is 1885\n",
      "Most Recent Birth Year is 1885\n",
      "\n",
      "This took 0.006952524185180664 seconds.\n",
      "--------------------------------------------------------------------------------\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "\n",
      "Would you like to restart? Enter yes or no.\n",
      " no\n"
     ]
    }
   ],
   "source": [
    "import time\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "CITY_DATA = {'chicago': 'chicago.csv',\n",
    "              'new york city': 'new_york_city.csv',\n",
    "              'washington': 'washington.csv'}\n",
    "\n",
    "def check_filters(input_str,input_type):\n",
    "    while True:\n",
    "        user_input = input(input_str)\n",
    "        try:\n",
    "            if user_input in ['chicago','new york city','washington'] and input_type == 'city':\n",
    "                break\n",
    "            elif user_input in ['january','february','march','april','may','june','all'] and input_type == 'month':\n",
    "                break\n",
    "            elif user_input in  ['sunday','monday','thuesday','wednesday','thursday','friday','saturday','all'] and input_type == 'day':\n",
    "                break\n",
    "            else:\n",
    "                if input_type == 'city':\n",
    "                    print('Please choose a city only from the following list [Chicago, New York City, Washington]')\n",
    "                if input_type == 'month':  \n",
    "                    print('Please choose a month only from the following list [january,february,march,april,may,june,all]')\n",
    "                if input_type == 'day':\n",
    "                    print('Please choose a day only from the following list [sunday,monday,thuesday,wednesday,thursday,friday,saturday,all]')\n",
    "        except ValueError:\n",
    "            print('Your Entry is Unacceptable, Please try again!')\n",
    "    return user_input\n",
    "\n",
    "def get_filters():\n",
    "    \"\"\"\n",
    "    Asks user to specify a city, month, and day to analyze.\n",
    "\n",
    "    Returns:\n",
    "        (str) city - name of the city to analyze\n",
    "        (str) month - name of the month to filter by, or \"all\" to apply no month filter\n",
    "        (str) day - name of the day of week to filter by, or \"all\" to apply no day filter\n",
    "    \"\"\"\n",
    "    print('Hello! Let\\'s explore some US bikeshare data!')\n",
    "    \n",
    "    city = check_filters('Please Choose a city from chicago, new york city, washington to view its data. \\n', 'city')\n",
    "    month = check_filters(\"Please Select a month to filter the data with, ex. january, or type 'all' to select all monthes. \\n\", 'month')\n",
    "    day = check_filters(\"Please Select a day to filter the data with, ex. sunday, or type 'all' to select all days. \\n\", 'day')\n",
    "    \n",
    "    print('-'*80)\n",
    "    print(f'You have choosed {city}, {month}, {day}')\n",
    "                      \n",
    "    return city, month, day\n",
    "\n",
    "def load_data(city, month, day):\n",
    "    \"\"\"\n",
    "    Loads data for the specified city and filters by month and day if applicable.\n",
    "\n",
    "    Args:\n",
    "        (str) city - name of the city to analyze\n",
    "        (str) month - name of the month to filter by, or \"all\" to apply no month filter\n",
    "        (str) day - name of the day of week to filter by, or \"all\" to apply no day filter\n",
    "    Returns:\n",
    "        df - Pandas DataFrame containing city data filtered by month and day\n",
    "    \"\"\"\n",
    "\n",
    "    # load data file into a dataframe\n",
    "    df = pd.read_csv(CITY_DATA[city])\n",
    "\n",
    "    # convert the Start Time column to datetime\n",
    "    df['Start Time'] = pd.to_datetime(df['Start Time'])\n",
    "\n",
    "    # extract month and day of week from Start Time to create new columns\n",
    "    df['month'] = df['Start Time'].dt.month\n",
    "    df['day_of_week'] = df['Start Time'].dt.strftime(\"%A\")\n",
    "    df['hour'] = df['Start Time'].dt.hour\n",
    "\n",
    "    # filter by month if applicable\n",
    "    if month != 'all':\n",
    "        # use the index of the months list to get the corresponding int\n",
    "        months = ['january', 'february', 'march', 'april', 'may', 'june']\n",
    "        month = months.index(month) + 1\n",
    "\n",
    "        # filter by month to create the new dataframe\n",
    "        df = df[df['month'] == month]\n",
    "\n",
    "    # filter by day of week if applicable\n",
    "    if day != 'all':\n",
    "        # filter by day of week to create the new dataframe\n",
    "        df = df[df['day_of_week'] == day.title()]\n",
    "\n",
    "    return df\n",
    "\n",
    "def time_stats(df):\n",
    "    \"\"\"Displays statistics on the most frequent times of travel.\"\"\"\n",
    "\n",
    "    print('\\nCalculating The Most Frequent Times of Travel...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    # display the most common month\n",
    "    common_month = df['month'].mode()[0]\n",
    "    print('The most common month is', common_month)\n",
    "\n",
    "    # display the most common day of week\n",
    "    common_day = df['day_of_week'].mode()[0]\n",
    "    print('The most common day is', common_day)\n",
    "\n",
    "    # display the most common start hour\n",
    "    common_hour = df['hour'].mode()[0]\n",
    "    print('The most common start hour is', common_hour)\n",
    "\n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*80)\n",
    "    \n",
    "def station_stats(df):\n",
    "    \"\"\"Displays statistics on the most popular stations and trip.\"\"\"\n",
    "\n",
    "    print('\\nCalculating The Most Popular Stations and Trip...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    # TO DO: display most commonly used start station\n",
    "    common_start_station = df['Start Station'].mode()[0]\n",
    "    print('The most common used start station is ',common_start_station)\n",
    "    \n",
    "    # TO DO: display most commonly used end station\n",
    "    common_end_station = df['End Station'].mode()[0]\n",
    "    print('The most common used end station is ',common_end_station)\n",
    "\n",
    "    # TO DO: display most frequent combination of start station and end station trip\n",
    "    frequent_combination = df.groupby(['Start Station','End Station'])\n",
    "    common_stations_combinations = frequent_combination.size().sort_values(ascending = False).head(4)\n",
    "    print('Most frequent combination of Start Station and End Station trip:\\n', common_stations_combinations)\n",
    "    \n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*80)\n",
    "    \n",
    "def trip_duration_stats(df):\n",
    "    \"\"\"Displays statistics on the total and average trip duration.\"\"\"\n",
    "\n",
    "    print('\\nCalculating Trip Duration...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    # TO DO: display total travel time\n",
    "    total_travel_time = df['Trip Duration'].sum()\n",
    "    print('The Total travel time is',total_travel_time)\n",
    "\n",
    "    # TO DO: display mean travel time\n",
    "    mean_travel_time = df['Trip Duration'].mean()\n",
    "    print('The Mean travel time is',mean_travel_time)\n",
    "    \n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*80)\n",
    "\n",
    "def user_stats(df,city):\n",
    "    \"\"\"Displays statistics on bikeshare users.\"\"\"\n",
    "\n",
    "    print('\\nCalculating User Stats...\\n')\n",
    "    start_time = time.time()\n",
    "\n",
    "    # TO DO: Display counts of user types\n",
    "    print('User Types Statistics: \\n')\n",
    "    x = df['User Type'].value_counts()\n",
    "    print(x)\n",
    "    # TO DO: Display counts of gender\n",
    "    if city != 'washinghton':\n",
    "        gender_counts = df['Gender'].value_counts()\n",
    "        print(gender_counts)\n",
    "    # TO DO: Display earliest, most recent, and most common year of birth\n",
    "        most_common_birthyear = int(df['Birth Year'].mode()[0])\n",
    "        print('Most Common Birth Year is',most_common_birthyear)\n",
    "        earliest_birthyear = int(df['Birth Year'].min())\n",
    "        print('Earliest Birth Year is',earliest_birthyear)\n",
    "        recent_birthyear = int(df['Birth Year'].min())\n",
    "        print('Most Recent Birth Year is',recent_birthyear)\n",
    "        \n",
    "    print(\"\\nThis took %s seconds.\" % (time.time() - start_time))\n",
    "    print('-'*80)\n",
    "    \n",
    "def main():\n",
    "    while True:\n",
    "        city, month, day = get_filters()\n",
    "        df = load_data(city, month, day)\n",
    "        time_stats(df)\n",
    "        station_stats(df)\n",
    "        trip_duration_stats(df)\n",
    "        user_stats(df,city)\n",
    "\n",
    "        restart = input('\\nWould you like to restart? Enter yes or no.\\n')\n",
    "        if restart.lower() != 'yes':\n",
    "            break\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "933287e9-a430-4514-8f8d-d5f0740fcf6b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}