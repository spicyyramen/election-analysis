# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The iwnner of the election based on popular vote



# add our dependencies
import csv
import os

# assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# open the election results and read the file
with open(file_to_load) as election_data:

    # to do: read and analyze the data here
    # read the file object with the reader function
    file_reader = csv.reader(election_data)
    # the variable file_reader is referencing the file object which is stored in memory
    ## to pull the data out of the file object we can iterate through the file_reader variable and print each row
    ## including the headers, or column names

    # print the header row
    headers = next(file_reader)
    print(headers)

