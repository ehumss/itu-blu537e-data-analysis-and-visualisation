####################################################################################################
#
#      ISTANBUL TECHNICAL UNIVERSITY
#      BLU 537E - Data Analysis & Visualization
#      Assignment 01
#
#      Author      :  Nese Gunes
#      Student ID  :  504161544
#      User ID     :  gunesn17
#
####################################################################################################
#
#      PROBLEM 1
#
#      A store charges $12 per item if you buy less than 10 items. 
# 
#      If you buy between 10 and 99 items, the cost is $10 per item.
#
#      If you buy 100 or more items, the cost is $7 per item.
#
#      Write a program that takes how many items are bought as an input and prints the total cost.
#
####################################################################################################

NUMBER_OF_ITEMS_TYPE_1 = 10;
NUMBER_OF_ITEMS_TYPE_2 = 100;

CHARGE_TYPE_1 = 12;
CHARGE_TYPE_2 = 10;
CHARGE_TYPE_3 = 7;

def problem1(number_of_items):    
    # Initially set total cost to zero.
    cost = 0;
    # If you buy less than "NUMBER_OF_ITEMS_TYPE_1", store charges "CHARGE_TYPE_1" per item.
    if (number_of_items < NUMBER_OF_ITEMS_TYPE_1):
        cost = number_of_items * CHARGE_TYPE_1;
    # Store charges "CHARGE_TYPE_2" per item for the given condition.
    elif (number_of_items >= NUMBER_OF_ITEMS_TYPE_1 and number_of_items < NUMBER_OF_ITEMS_TYPE_2):
        cost = number_of_items * CHARGE_TYPE_2;
    # If you buy more than "NUMBER_OF_ITEMS_TYPE_2", store charges "CHARGE_TYPE_3" per item.
    elif (number_of_items >= NUMBER_OF_ITEMS_TYPE_2):
        cost = number_of_items * CHARGE_TYPE_3;
    
    print("{} items are bought, the total cost is: {}.".format(number_of_items, cost));
        
    return;

####################################################################################################
#
#      PROBLEM 2
#
#      Write a program that generates a list of 20 random numbers between 1 and 100.
#
#     (a) Print the list.
#     (b) Print the average of the elements in the list.
#     (c) Print the largest and smallest values in the list.
#     (d) Print the second largest and second smallest entries in the list
#     (e) Print how many even numbers are in the list.
#
####################################################################################################

import random;

def problem2():
    # Create a list.
    list = [];
    
    # Insert 20 random numbers between 1 and 100, to the list.
    for i in range(1, 20):
        list.append(random.randint(1, 100));
    
    # PART (a): Print the list.
    print("Part (a): A list of 20 random numbers between 1 and 100 is generated.\n");
    print(list);
    print("\n***********************************************************\n");
    
    # PART (b): Print the average of the elements in the list.
    print("Part (b): The average of the elements in the list is evaluated.\n");
    sum = 0;
    for i in list:
        sum += i;
    print("The Average: {}".format(sum/20));
    print("\n***********************************************************\n");
       
    # PART (c): Print the largest and the samllest values in the list.
    print("Part (c): The largest and the smallest values in the list are found.\n");
    max = list[0];
    min = list[0];
    
    for i in list:
        if max < i:
            max = i;
        elif min > i:
            min = i;
            
    print("The largest value is: {}".format(max));
    print("The smallest value is: {}".format(min));    
    print("\n***********************************************************\n");
    
    # PART (d): Print the second largest and the second smallest entries in the list.
    print("Part (d): Second largest and the second smallest entries are found.\n");
    second_max = list[0];
    second_min = list[0];
    
    for i in list:
        if second_max < i and i != max:
            second_max = i;
        elif second_min > i and i != min:
            second_min = i;
            
    print("The second largest value is: {}".format(second_max));
    print("The second smallest value is: {}".format(second_min)); 
    print("\n***********************************************************\n");
    
    # PART (e): Print how many even numbers are in the list.
    print("Part (e): Total number of even numbers in the list is evaluated.\n");
    count = 0;
    
    for i in list:
        if i % 2 == 0:
            count += 1;
            
    print("Count of Even Numbers: {}".format(count));
    print("\n***********************************************************\n");
    
    return;

####################################################################################################
#
#       PROBLEM 3
#
#       You are given a file named “blood-pressure.csv” which contains blood pressure measurement for some patients.
#
#       The first column is for patient id and the second column is for blood pressure measurement in the format of mean[min-max] values.
#
#       Write a function that takes this file as an input and do the folowing tasks:
#
#       (a) Prints the lowest and highest blood pressure measurements amongs the patients. The output should be 108 and 180.
#       (b) Prints the average of the mean values.
#
####################################################################################################

MAX_INTEGER = 65535
MIN_INTEGER = -65535 

import csv
import re

def problem3(file):
    
    max = MIN_INTEGER;
    min = MAX_INTEGER;
    sum = 0;
    number_of_rows = 0;
    
    # Open the CSV file using Python's built-in library: csv
    with open(file, mode='r') as csv_file:
        # Read the file as a dictionary.
        csv_reader = csv.DictReader(csv_file)
        # Now, we have a dictinary: 
        # [('id', '1'), ('Blood pressure systolic (mmHg) mean[min-max]', '135[113-166]')],
        # [('id', '2'), ('Blood pressure systolic (mmHg) mean[min-max]', '140 [110-155]')], etc.
        
        # Part (a): Print the lowest and the highest blood pressure measurements among the patients.
        # The output should be: 108 and 180.
        
        for row in csv_reader:
            # Given the 'Blood ... [min-max]' key, find all the integers from the value string: '135[113-166]'.
            # Store the integers (blood pressures) in a list.
            list = [int(x) for x in re.findall('\d+', row['Blood pressure systolic (mmHg) mean[min-max]'])]
            
            # PART A: MIN-MAX
            # In every row, check the min-max values, update when necessary.
            if (list[1] > max):
                max = list[1];
            elif (list[2] > max):
                max = list[2];
            
            if (list[1] < min):
                min = list[1];
            elif (list[2] < min):
                min = list[2];
            
            # PART B: THE AVERAGE
            sum += list[0];
            number_of_rows += 1;

        
        print("PART (A): Print the lowest and the highest blood pressure measurements among the patients.\n");
        print("The Lowest Blood Pressure is : {}".format(min))
        print("The Highest Blood Pressure is: {}".format(max))
        print("\n***********************************************************\n");
        
        # Part (b): Print the average of the mean values.
        print("PART (B): Print the average of the mean values.\n")
        print("The Average is: {}".format(sum/number_of_rows));
        print("\n***********************************************************\n");
        
    return;

####################################################################################################
#
#       PROBLEM 4
#
#       You are given a csv (gdp_per_capita.csv) file for GDP per capita taken from World Bank. 
#
#       The file holds data from 1960 to 2017. Note that some data for certain years are missing.
#
#       Write a function that takes this file as an input and do the following tasks for Turkey:
#        
#       (a) Calculate the yearly percentage increase compared to previous year and the find the year that has highest increase in terms of percentage.
#       (b) Find the years that GDP per capita decreased compared to the previous year.
#
####################################################################################################

import collections
import csv
import re

def problem4(file):
    # Open the CSV file using Python's built-in module: csv
    file = open(file, mode = 'r')
    # Read the file as a dictionary.
    reader = csv.DictReader(file, delimiter=';')
    # OrderedDict([('Country Name', 'Aruba'), ('1960', ''), ('1961', ''), ('1962', ''), ('1963', ''), ('1964', ''), 
    # ('1965', ''), ('1966', ''), ('1967', ''), ('1968', ''), ('1969', ''), ('1970', ''), ('1971', ''), ('1972', ''), ... ]), etc.
    
    # Part (a): Create a dictionary to store yearly percentage increase.
    increase_in_terms_of_percentage = {}    
    
    for row in reader:
        # Part (a): For Turkey, evaluate the increase using formula: (current_gdp - previous_gdp) * 100 / (current_gdp)
        if row['Country Name'] == 'Turkey':
            # Part (a): Increase percentage is calculated for: [1961 and 2017] time interval.
            # Part (a): (There is NO increase percentage for the year 1960.)
            for i in range(2, len(reader.fieldnames)):
                increase_in_terms_of_percentage[reader.fieldnames[i]] = (float(row[reader.fieldnames[i]]) - float(row[reader.fieldnames[i - 1]])) * 100 / (float(row[reader.fieldnames[i]])) 
                # Now, we have:
                # {'1961': -78.73733197596287, '1962': 7.896086257857306, '1963': 11.753818665509044, '1964': 5.119424708452099,
                # '1965': 4.1637664070723455, '1966': 13.387860733884622, '1967': 7.696841934220605, '1968': 8.330375671997261, ..} etc.
    
    # Part (a): Calculate the yearly percentage increase compared to previous year and the find the year that has highest increase in terms of percentage.
    print("PART (A): Find the year that has highest increase in terms of percentage.\n")
    # Part (a): Using collections module, find the max increase and the year that has the max increase.
    print("The YEAR with the HIGHEST INCREASE: {}".format(collections.Counter(increase_in_terms_of_percentage).most_common(1)))
    print("\n***********************************************************\n");
    
    
    # Part (b): Find the years that GDP per capita decreased compared to the previous year.
    print("PART (B): Find the years that GDP per capita decreased compared to the previous year.\n")
    print("GDP percentage decreased in the following YEARS: \n")
    for key, value in increase_in_terms_of_percentage.items():
        if value < 0:
            print(key, end = '  ')
    print("\n\n***********************************************************\n");

####################################################################################################
#
#       PROBLEM 5
#
#       Norway_new_car_sales_by_model.csv file contains information of the new car sales in Norway between the years 2007-2017.
#
#       The dataset was obtained from www.kaggle.com web site. The dataset comprises of monthly car sale quantity for various manufacturers and models.
#
#       Make columns shows the manufacturer and Pct column shows the percent share in monlty total sales.
#
#       Using this dataset do the following tasks:
# 
#       (a) Print the number of unique manufacturers in this dataset.
#       (b) Find the manufacturer that has the highest car sales in 2010?
#
####################################################################################################

import collections
import csv

def problem5(file):
    # Open the CSV file using Python's built-in module: csv
    # To avoid UnicodeDecodeError, errors='ignore' parameter is used. 
    file = open(file, mode = 'r', encoding="utf8", errors='ignore')
    # Read the file as a dictionary.
    reader = csv.DictReader(file, delimiter = ',')
    # Now, we have a dictionary:
    # [('Year', '2007'), ('Month', '1'), ('Make', 'Volkswagen '), ('Model', 'Volkswagen Passat'), ('Quantity', '1267'), ('Pct', '10')]
    # [('Year', '2007'), ('Month', '1'), ('Make', 'Toyota '), ('Model', 'Toyota Rav4'), ('Quantity', '819'), ('Pct', '6.5')], etc.
    
    # Part (a): Create a list to store all manufacturers.
    manufacturer = []
    # Part (b): Using collections module, create a counter to be able to count the car sales of each manufacturer. 
    quantity_of_car_sales = collections.Counter()
    
    for row in reader:
        # Part (a): Add all the manufacturers to the list, without considering if it is already in the list or not.
        manufacturer.append(row['Make'])
        # Part (a): Now, we have a list as follows:
        # Part (a): ['Volkswagen ', 'Toyota ', 'Toyota ', 'Volkswagen ', 'Toyota ', 'Peugeot ', 'Skoda ', 'Toyota ', 'Ford ', 'Volvo ', ...]
         
        # Part (b): In year 2010, for each manifacturer find the number of car sales and sum them up.    
        if row['Year'] == '2010':
            quantity_of_car_sales[row['Make']] += int(row['Quantity']) 
           
    # Part (a): Using collections module, count the number of occurences of the manufacturers. 
    unique_manifacturers = collections.Counter(manufacturer)
    # Part (a): Now, the keys are unique in this list:
    # Part (a): Counter({'Toyota ': 492, 'Volkswagen ': 440, 'Volvo ': 294, 'Ford ': 246, 'Nissan ': 180, 'Audi ': 146, 
    # Part (a): 'Skoda ': 142, 'Peugeot ': 132, 'BMW ': 130, 'Mitsubishi ': 105, 'Mazda ': 80, 'Mercedes-Benz ': 63,]) etc.
    
    # PART (a): Print the number of unique manufacturers in this dataset.
    print("PART (A): Print the number of unique manufacturers in this dataset.\n")
    print("The Number of Unique Manifacturers is: {}".format(len(unique_manifacturers.keys())))
    print("\n***********************************************************\n");
    
    # PART (b): Find the manufacturer that has the highest car sales in 2010.
    print("PART (B): Find the manufacturer that has the highest car sales in 2010.\n")
    print("The MANUFACTURER with HIGHEST CAR SALES in 2010: {}".format(quantity_of_car_sales.most_common(1)))
    print("\n***********************************************************\n");

####################################################################################################
# TEST CODE
####################################################################################################

# PROBLEM ONE
problem1(1);
problem1(10);
problem1(100);

# PROBLEM TWO
problem2();

# PROBLEM THREE
problem3("blood_pressure.csv");

# PROBLEM FOUR
problem4("gdp_per_capita.csv");

# PROBLEM FIVE
problem5("norway_new_car_sales_by_model.csv");

####################################################################################################
