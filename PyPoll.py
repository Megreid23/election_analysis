# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Import the datetime class from the datetime module
import datetime
# Use the now() attribute on the datetime class to get the present time
now = datetime.datetime.now()
# print the present time now
print("The time right now is", now)

import datetime as dt

now = dt.datetime.now()

print("The time right now is", now)

import csv
dir(csv)

# Assign a variable for the file to load and the path

file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file

with  open(file_to_load) as election_data:

# To do: perform analysis
        print(election_data)

# Close the file

